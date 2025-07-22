import os
import json

def list_files():
    try:
        with open("config.json") as f:
            config = json.load(f)

        root_dir = config.get("root_directory", ".")
        files = os.listdir(root_dir)
        return "Files:\n" + "\n".join(files)  
    except Exception as e:
        return f"Error: {str(e)}"
