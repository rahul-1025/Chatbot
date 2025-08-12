print("🤖 Welcome to ChatBot!")
print("💬 Type 'bye' to end the chat.\n")

while True:
    user_input = input("👤 You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("🤖 Bot: Hello! How can I help you today?")
    elif user_input == "what is your name?":
        print("🤖 Bot: I am your friendly chatbot.")
    elif user_input == "ok,how are you":
        print("🤖 Bot: I'm just a bot, but I'm doing great! How about you?")
    elif user_input == "bye":
        print("🤖 Bot: Goodbye! Have a nice day.")
        break
    else:
        print("🤖 Bot: Sorry, I didn't understand that.")
