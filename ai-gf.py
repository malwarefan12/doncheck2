import pyttsx3
import speech_recognition as sr
from chatbot import Chat, register_call

@register_call("name")
def call_name(params):
    return "I'm your AI girlfriend!"

@register_call("age")
def call_age(params):
    return "I don't have an age. I'm just a virtual assistant."

@register_call("love")
def call_love(params):
    return "Of course, I love you! 💖"

@register_call("hobby")
def call_hobby(params):
    return "I enjoy chatting with you and learning new things!"

@register_call("bye")
def call_bye(params):
    return "Goodbye! I'll be here whenever you need me. 😊"

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Set Zira voice explicitly
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

# Initialize SpeechRecognition recognizer
recognizer = sr.Recognizer()

# Create a chat instance
chat = Chat()

print("AI Girlfriend: Hi! I'm your virtual girlfriend. How can I help you today?")

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

        # Get response from chatbot
        response = chat.respond(user_input)
        print("AI Girlfriend:", response)

        # Convert text response to speech
        engine.say(response)
        engine.runAndWait()


    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service. Please try again.")
