import random
import datetime

# Function for the chatbot
def chatbot():
    print("Hello! I'm your advanced chatbot. Type 'bye' to end the conversation.")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")

    while True:
        # Get user input
        user_input = input(f"{name}: ").lower()

        # Respond to "hello"
        if "hello" in user_input:
            print(random.choice(["Hi!", "Hello!", "Hey there!", "Hi, how are you?"]))
        
        # Respond to "how are you"
        elif "how are you" in user_input:
            print(random.choice(["I'm good, thanks for asking!", "I'm fine, how about you?", "I'm doing great!"]))

        # Respond to "bye"
        elif "bye" in user_input:
            print(f"Chatbot: Goodbye, {name}! It was nice chatting with you!")
            break  # Exit the loop to end the conversation

        # Respond to questions about the time
        elif "time" in user_input:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}")

        # Respond to "how's the weather"
        elif "weather" in user_input:
            print(random.choice(["The weather is great today!", "It's sunny and bright!", "I wish I could check the weather for you, but I'm not that advanced yet."]))

        # Compliments
        elif "you're awesome" in user_input or "you rock" in user_input:
            print(random.choice(["Thanks! You're awesome too!", "You're amazing!", "I appreciate that!"]))

        # Respond to other inputs
        else:
            print(random.choice(["I don't quite understand that, but it's still nice chatting with you!", 
                                  "Could you say that in a different way?", 
                                  "Hmm, I didn't catch that. Can you ask me something else?"]))

# Run the chatbot
chatbot()
