import re
import random

def chatbot():
    print("🤖 Chatbot: Hi! I’m your regex-powered chatbot. Say something! (type 'bye' or 'exit' to quit)\n")

    # Define rules: pattern -> list of responses
    rules = {
        r"\b(hi|hello|hey)\b": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        r"\bhow are (you|u)\b": ["I’m fine, thanks for asking!", "Doing great! And you?", "I’m just a bot, but I’m happy!"],
        r"\bwhat.*name\b": ["I’m just a simple chatbot.", "You can call me ChatBot!"],
        r"\bwho are you\b": ["I’m just a simple chatbot.", "Your friendly virtual assistant."],
        r"\b(bye|exit|goodbye)\b": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
        r"\bwhat.*time\b": ["I don’t have a clock, but it’s always a good time to chat!", "Time flies when we’re talking!"],
        r"\bwhat.*your favorite color\b": ["I like all the colors of the rainbow!", "Maybe blue… or green!"],
        r"\bhow old are you\b": ["I was born the moment you ran this program!", "Age is just a number for bots!"],
        r"\bthank(s| you)\b": ["You’re welcome!", "No problem!", "Anytime!"],
        r"\b(yes|yeah|yep)\b": ["Great!", "Good to know!", "Awesome!"],
        r"\b(no|nah|nope)\b": ["Oh, okay.", "Alright.", "No worries."],
        r"\bhelp\b": ["You can ask me about my name, who I am, how I am, or just say hello!"]
    }

    while True:
        user_input = input("You: ").lower().strip()
        matched = False

        for pattern, responses in rules.items():
            if re.search(pattern, user_input):
                print(f"🤖 Chatbot: {random.choice(responses)}")
                matched = True
                if re.search(r"\b(bye|exit|goodbye)\b", user_input):
                    return
                break

        if not matched:
            print("🤖 Chatbot: Sorry, I didn’t understand that. Could you rephrase?")

# Run it
chatbot()