import subprocess
from tools.get_date import get_current_date
from tools.get_file import list_files

def ask_llm(prompt):
    # Handle the tool based commands
    if 'date' in prompt.lower():
        return get_current_date()
    elif 'list files' in prompt.lower():
        return list_files()
    
    # otherwise send it to ollama
    result = subprocess.run(
        ['ollama', 'run', 'mistral'], 
        input = prompt.encode(),
        stdout = subprocess.PIPE,
        stderr= subprocess.PIPE
    )

    return result.stdout.decode().strip()