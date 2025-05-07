import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]),
    (r"how are you?", ["I'm a bot, but I'm doing well! How about you?"]),
    (r"what is your name?", ["I'm a chatbot!", "You can call me ChatBot."]),
    (r"quit", ["Goodbye!", "See you later!", "Bye!"])
]

# Create Chat instance
chatbot = Chat(pairs, reflections)

# Start chatbot conversation
print("Hello! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    