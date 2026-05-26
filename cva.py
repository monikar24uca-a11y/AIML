import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        speak("Sorry, I did not understand.")
        return ""

# Welcome message
speak("Hello! I am your AI voice assistant.")

# Main loop
while True:
    command = listen()

    # Open YouTube
    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Open Google
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Tell time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")

    # Wikipedia search
    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, sentences=2)
        speak(info)

    # Exit assistant
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break

    else:
        speak("Please say the command again.")