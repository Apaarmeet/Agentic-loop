def fileRead(file_path):
    with open(file_path) as f:
        data = f.read()
        return data