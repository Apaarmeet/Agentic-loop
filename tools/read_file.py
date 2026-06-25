def fileRead(file_path):
    try:
        with open(file_path) as f:
            data = f.read()
            return data
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except PermissionError:
        return f"Error: Permission denied reading {file_path}"
    except Exception as e:
        return f"Error reading file: {e}"