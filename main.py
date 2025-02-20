import os
import pyttsx3
import platform

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Ayan")
    engine = pyttsx3.init()  # Initialize pyttsx3 engine

    # Set speech rate (default is usually around 200)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Decrease speed by 50 (Adjust as needed)

    while True:
        x = input("Enter what you want to speak (or 'q' to quit): ")
        if x.lower() == "q":
            engine.say("Goodbye Ayan have a nice day")
            engine.runAndWait()
            break

        # Check OS type
        if platform.system() == "Darwin":  # macOS
            os.system(f'say "{x}"')
        else:  # Windows/Linux
            engine.say(x)
            engine.runAndWait()
