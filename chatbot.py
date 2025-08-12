print("Welcome to ChatBot!")
print("Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi":
        print(" Bot: Hello!")
    elif user_input == "what is your name?":
        print(" Bot: I am your friendly chatbot.")
    elif user_input == "bye":
        print(" Bot: Goodbye!")
        break
    else:
        print(" Bot: Sorry, I didn't understand that.")

