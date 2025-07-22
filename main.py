from agent import ask_llm

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = ask_llm(user_input)
    print("🤖 Assistant:", response)