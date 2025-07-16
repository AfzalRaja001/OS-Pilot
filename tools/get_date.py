from datetime import datetime

def get_current_date():
    today = datetime.now().strftime("%A, %d %B %Y")
    return f"Today is {today}."