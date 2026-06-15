
def writeFile(file_path, content):
    with open(file_path, "w") as f:
        res = f.write(content)
        return res
