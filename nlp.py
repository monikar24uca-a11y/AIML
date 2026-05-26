# Simple NLP Chatbot AI Program

from nltk.chat.util import Chat, reflections

# Chat patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name ?",
        ["I am an AI chatbot."]
    ],
    [
        r"how are you ?",
        ["I am fine. How can I help you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem."]
    ],
    [
        r"bye|exit",
        ["Goodbye!", "See you later!"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatbot
print("NLP Chatbot Started (type 'bye' to exit)")

chatbot.converse()