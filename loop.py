from google import genai
from google.genai import types
from tool_ref import weather_function, read_file, write_file, bash_tool
from tools.weather_function import getWeather
from tools.write_file import writeFile
from tools.read_file import fileRead
from tools.bash import bash
from dotenv import load_dotenv
import os

def llmCall( content:list ):
    load_dotenv()
    geminiApi = os.getenv("GEMINI_API_KEY")
    if not geminiApi:
        print("Error: GEMINI_API_KEY not set in environment")
        return None
    tools = types.Tool(function_declarations = [weather_function, read_file, write_file, bash_tool])
    config = types.GenerateContentConfig(tools = [tools])


    client =  genai.Client(api_key= geminiApi)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents = content,
            config = config
        )
        return response
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None


def agentLoop():

    userPrompt = input("what do want to make today: ")
    part=[types.Part(text = userPrompt)]
    content = [types.Content(role="user", parts= part )]

    while True:
        response = llmCall(content)
        if response is None:
            print("LLM call failed. Exiting.")
            break

        if not response.candidates:
            print("No candidates returned. Prompt may have been blocked.")
            break

        content.append(response.candidates[0].content)

        part = response.candidates[0].content.parts[0]
        
        if part.function_call:
            fc = part.function_call
            print(f"Model requested function: {fc.name} with args {fc.args}")
            try:
                if fc.name == weather_function["name"]:
                    location = fc.args.get("location")
                    if not location:
                        res = "Error: missing 'location' argument"
                    else:
                        res = getWeather(location)
                        print("calling weather function")
                elif fc.name == read_file["name"]:
                    file_path = fc.args.get("file_path")
                    if not file_path:
                        res = "Error: missing 'file_path' argument"
                    else:
                        res = fileRead(file_path)
                        print("calling read file function")
                elif fc.name == write_file["name"]:
                    file_path = fc.args.get("file_path")
                    content_arg = fc.args.get("content")
                    if not file_path or content_arg is None:
                        res = "Error: missing 'file_path' or 'content' argument"
                    else:
                        res = writeFile(file_path, content_arg)
                        print("calling write file function")
                elif fc.name == bash_tool["name"]:
                    command = fc.args.get("command")
                    if not command:
                        res = "Error: missing 'command' argument"
                    else:
                        res = bash(command)
                        print("calling bash function")
                else:
                    res = f"Error: unknown function '{fc.name}'"
            except Exception as e:
                res = f"Error executing {fc.name}: {e}"
            fnResponse = [types.Part(function_response=types.FunctionResponse(name=fc.name, response={"result": res}))]
            content.append(types.Content(role="user", parts= fnResponse))
            continue
        else:
            print(response.text)
            break


        

        

    
