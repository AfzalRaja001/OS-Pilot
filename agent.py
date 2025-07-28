import subprocess
import os
from tools.get_date import get_current_date
from tools.get_file import list_files
from tools.summarize_file import summarize_file
import re

def ask_llm(prompt):
    # Handle the tool based commands
    if 'date' in prompt.lower():
        return get_current_date()
    elif 'list files' in prompt.lower():
        return list_files()
    elif 'summarize' in prompt.lower():
        matches = re.findall(r'"(.*?)"|(\S+)', prompt)

        candidates = [m[0] if m[0] else m[1] for m in matches]
        for candidate in candidates:
            if os.path.isfile(candidate) and candidate.lower().endswith((".pdf", ".txt", '.java', '.c', '.py', '.cpp', '.js', '.html', '.css', '.json', '.xml', '.ppt', '.pptx', '.xlsx', '.xls')):
                return summarize_file(candidate)

        return "Please include a valid filename to summarize."
    # otherwise send it to ollama
    result = subprocess.run(
        ['ollama', 'run', 'mistral'], 
        input = prompt.encode(),
        stdout = subprocess.PIPE,
        stderr= subprocess.PIPE
    )

    return result.stdout.decode().strip()