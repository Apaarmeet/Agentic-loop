weather_function = {
        "name" : "weather_function",
        "description" : "gets the current temperature of a given location",
        "parameters": {
            "type" : "object",
            "properties" : {
                "location" : {
                    "type" : "string",
                    "description" : "the city name e.g. san francisco "
                }
            },
            "required" : ["location"]
        }
    }

read_file = {
    "name": "read_file",
    "description": "Reads the contents of a file",
    "parameters": {
        "type":"object",
        "properties": {
            "file_path" : {
                "type": "string",
                "description" : "path of the file"
            }
        },
        "required": ["file_path"]
    }
}

write_file = {
    "name": "write_file",
    "description": "Writes the content in a file",
    "parameters": {
        "type":"object",
        "properties": {
            "file_path" : {
                "type": "string",
                "description" : "path of the file"
            },
            "content": {
                "type": "string",
                "description": "content to be wrriten in file"
            }
        },
        "required": ["file_path", "content"]
    }
}

bash_tool = {
    "name": "bash_tool",
    "description": "Runs the bash commands in terminal",
    "parameters": {
        "type":"object",
        "properties": {
            "command" : {
                "type": "string",
                "description" : "bash command for e,g, : ls, pwd, mkdir,grep, npm run dev, bun run dev, git commands"
            }
        },
        "required": ["command"]
    }
}