import re

# Step 1: Define patterns and responses
patterns = {
    r"hello|hi|hey": "Hi, how can I help you?",
    r"what is your name": "I am your Python Chatbot.",
    r"how are you": "I am just a program, but I am doing fine!",
    r"bye|goodbye": "Goodbye! Have a great day!"
}

def chatbot():
    print("Chatbot: Hello! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()  # Step 2: Take user input & normalize

        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break

        matched = False
        for pattern, response in patterns.items():
            if re.search(pattern, user_input):   # Step 3: Check regex pattern
                print("Chatbot:", response)
                matched = True
                break

        if not matched:   # Step 4: Fallback response
            print("Chatbot: I don’t understand.")

# Run chatbot
chatbot()
