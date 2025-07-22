import os
import fitz
import subprocess

def read_file_content(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    if ext == '.txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
        
    elif ext =='.pdf':
        doc = fitz.open(filepath)
        text = ""

        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    
def chunk_text(text, chunk_size=500):
    words = text.split()

    return [" ".join(words[i : i+chunk_size]) for i in range(0, len(words), chunk_size)]

def summarize_text_from_file(filepath):
    content = read_file_content(filepath)
    chunks = chunk_text(content)

    all_summaries = []

    for chunk in chunks:
        prompt = f"Summarize the text: \n\n{chunk}"
        result = subprocess.run(
            ['ollama', 'run', 'mistral'],
            input = prompt.encode(),
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        response = result.stdout.decode().strip()
        all_summaries.append(response)

    return "\n".join(all_summaries)    