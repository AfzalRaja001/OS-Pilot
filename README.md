# OS Pilot
Project related to LLM which can act as OS level AI Assistant

# Project Structure
This project is structured to facilitate the development of an AI assistant that can interact with the operating system and perform tasks such as fetching the current date or listing files in a directory. Below is the directory structure and a brief description of each component:
PersonalAssistant/
├── main.py                  ← runs your assistant
├── agent.py                 ← LLM prompt logic
├── tools/
│   ├── __init__.py
│   ├── get_date.py          ← tool for current date
│   └── list_files.py        ← tool to fetch file info
├── indexer.py               ← builds context of your files
├── system_context.json      ← stores file info (index)
├── config.json              ← settings (root folder, etc.)


