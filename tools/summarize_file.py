from summarize import summarize_text_from_file

def summarize_file(filename):
    try:
        summary = summarize_text_from_file(filename)
        return f"Summary of {filename}:\n{summary}"
    except Exception as e:
        return f"Could not summarize file: {str(e)}"
