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
    tools = types.Tool(function_declarations = [weather_function, read_file, write_file, bash_tool])
    config = types.GenerateContentConfig(tools = [tools])
    contents = content


    client =  genai.Client(api_key= geminiApi)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = contents,
        config = config
    )
    return response


def agentLoop():

    userPrompt = input("what do want to make today: ")
    part=[types.Part(text = userPrompt)]
    content = [types.Content(role="user", parts= part )]

    while True:
        response = llmCall(content)

        content.append(response.candidates[0].content)

        part = response.candidates[0].content.parts[0]
        
        if part.function_call:
            fc = part.function_call
            print(f"Model requested function: {fc.name} with args {fc.args}")
            if(fc.name == weather_function["name"]): res = getWeather(fc.args["location"]); print("calling weather function")
            elif(fc.name == read_file["name"]): res = fileRead(fc.args["file_path"]); print("calling read file function")
            elif(fc.name == write_file["name"]): res = writeFile(fc.args["file_path"], fc.args["content"]); print("calling write file function")
            elif(fc.name == bash_tool["name"]): res = bash(fc.args["command"]); print("calling bash function")
            fnResponse = [types.Part(function_response=types.FunctionResponse(name=fc.name, response={"result": res}))]
            content.append(types.Content(role="user", parts= fnResponse))
            continue
        else:
            print(response.text)
            break


        

        

    
