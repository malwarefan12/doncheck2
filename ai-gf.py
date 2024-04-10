import pyttsx3
import speech_recognition as sr
from chatbotAI import ChatbotAI

# Create a ChatbotAI instance
chatbot = ChatbotAI()

print("AI Girlfriend: Hi! I'm your virtual girlfriend. How can I help you today?")

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Set Zira voice explicitly
voices = engine.getProperty('voices')
for voice in voices:
    if "Zira" in voice.name:
        engine.setProperty('voice', voice.id)

# Initialize SpeechRecognition recognizer
recognizer = sr.Recognizer()

# Chat loop
while True:
    # Listen for speech input
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech input
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)

        # Get response from ChatbotAI
        response = chatbot.get_response(user_input)
        print("AI Girlfriend:", response)

        # Convert text response to speech
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service. Please try again.")
