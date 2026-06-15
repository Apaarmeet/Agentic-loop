
import subprocess
def bash(command):
    res = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30, input="y/n")
    return {"stdout": res.stdout, "stderr": res.stderr}

    
    