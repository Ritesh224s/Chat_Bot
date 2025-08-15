import random
import datetime

def chatbot():
    print("🤖 Hello! I’m ChatBot. Type 'exit' to quit.\n")
    name = None
    greetings = ["Hello!", "Hi there!", "Hey!", "Hi! How’s it going?"]
    jokes = [
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "Why do Java developers wear glasses? Because they can't C#.",
        "I told my computer I needed a break, and it said: 'No problem — I'll go to sleep!'"
    ]
    facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren’t.",
        "Sharks existed before trees."
    ]

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("🤖 Goodbye! Have a great day!")
            break

        elif user_input in ["hi", "hello", "hey"]:
            print("🤖", random.choice(greetings) if not name else f"{random.choice(greetings)} {name}!")

        elif "your name" in user_input:
            print("🤖 I’m ChatBot, your friendly assistant.")

        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip().title()
            print(f"🤖 Nice to meet you, {name}!")

        elif "time" in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"⏰ The current time is {current_time}.")

        elif "date" in user_input:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            print(f"📅 Today's date is {current_date}.")

        elif "joke" in user_input:
            print("😂", random.choice(jokes))

        elif "fact" in user_input:
            print("📢", random.choice(facts))

        elif user_input.startswith("calc "):
            try:
                expression = user_input[5:]
                result = eval(expression)
                print(f"🧮 Result: {result}")
            except:
                print("⚠️ Sorry, I couldn’t calculate that.")

        else:
            print("🤖 I’m not sure how to respond to that. Try 'joke', 'fact', 'time', or 'calc 2+2'.")

chatbot()
