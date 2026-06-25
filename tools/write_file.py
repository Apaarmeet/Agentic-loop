
def writeFile(file_path, content):
    try:
        with open(file_path, "w") as f:
            f.write(content)
        return f"Successfully wrote to {file_path}"
    except FileNotFoundError:
        return f"Error: Directory not found for {file_path}"
    except PermissionError:
        return f"Error: Permission denied writing to {file_path}"
    except Exception as e:
        return f"Error writing file: {e}"
