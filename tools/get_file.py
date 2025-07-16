import os
import json

def list_files():
    try:
        with open("config.json", 'r') as f:
            config = json.load(f)
            root_directory = config.get("root_directory", ".")
            files = os.listdir(root_directory)

            return "Files:\n" + "\n".join(files)
    except Exception as e:
        print(f"Error listing files: {e}")