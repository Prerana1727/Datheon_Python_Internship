
import re

# Chatbot responses
intents = {
    "greeting": {
        "patterns": [r"\bhello\b", r"\bhi\b", r"\bhey\b"],
        "response": "Hello! Welcome to Python Assistant. How can I help you?"
    },

    "hours": {
        "patterns": [r"\btime\b", r"\bhours\b", r"\bopen\b", r"\bclosing\b"],
        "response": "Our business hours are Monday to Saturday, 9 AM to 6 PM."
    },

    "products": {
        "patterns": [r"\bproduct\b", r"\bproducts\b", r"\bservices\b", r"\bservice\b"],
        "response": "We offer software development, web development and technical support."
    },

    "pricing": {
        "patterns": [r"\bprice\b", r"\bcost\b", r"\bpricing\b", r"\bcharges\b"],
        "response": "Our pricing depends on the service and project requirements."
    },

    "contact": {
        "patterns": [r"\bcontact\b", r"\bemail\b", r"\bphone\b", r"\bsupport\b"],
        "response": "You can contact our support team through hello@example.com."
    },

    "thanks": {
        "patterns": [r"\bthanks\b", r"\bthank you\b"],
        "response": "You're welcome! Happy to help."
    },

    "help": {
        "patterns": [r"\bhelp\b", r"\boptions\b"],
        "response": "You can ask about business hours, products, pricing or contact details."
    }
}


def get_response(user_input):

    # Convert input to lowercase
    user_input = user_input.lower().strip()

    # Check every intent
    for intent, details in intents.items():

        for pattern in details["patterns"]:

            if re.search(pattern, user_input):
                return details["response"]

    # Default response
    return "Sorry, I didn't understand that. Please ask about our products, pricing or business hours."


def chatbot():

    print("\n====================================")
    print("       PYTHON TERMINAL CHATBOT")
    print("====================================")
    print("Bot: Hello! Welcome to Python Assistant.")
    print("Bot: Type 'help' to see what you can ask.")
    print("Bot: Type 'bye' to exit.")
    print("------------------------------------")

    while True:

        user_input = input("\nYou: ").strip()

        # Check empty input
        if not user_input:
            print("Bot: Please enter something.")
            continue

        # Exit commands
        if re.fullmatch(r"(bye|exit|quit)", user_input, re.IGNORECASE):
            print("Bot: Thank you for chatting. Goodbye!")
            break

        # Generate response
        response = get_response(user_input)

        print("Bot:", response)


# Start chatbot
if __name__ == "__main__":
    chatbot()
