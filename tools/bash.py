import subprocess

def bash(command):
    try:
        res = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        return {
            "stdout": res.stdout,
            "stderr": res.stderr,
            "returncode": res.returncode
        }
    except subprocess.TimeoutExpired:
        return {"error": f"Command timed out after 30s: {command}"}
    except Exception as e:
        return {"error": f"Error running command: {e}"}

    
    