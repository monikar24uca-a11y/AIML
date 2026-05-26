# Import library
import speech_recognition as sr

# Create recognizer object
recognizer = sr.Recognizer()

# Use microphone as input source
with sr.Microphone() as source:
    print("Speak something...")

    # Adjust for background noise
    recognizer.adjust_for_ambient_noise(source)

    # Listen to audio
    audio = recognizer.listen(source)

try:
    # Convert speech to text
    text = recognizer.recognize_google(audio)

    print("You said:")
    print(text)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError:
    print("Internet connection error")