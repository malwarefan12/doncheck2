import pyttsx3
import speech_recognition as sr
import requests
import json

engine = pyttsx3.init()

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

recognizer = sr.Recognizer()


print("AI Girlfriend: Hi! I'm your virtual girlfriend. How can I help you today?")

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
        r = requests.get("""https://freeaiapi.vercel.app/api/ChitChat?query=""" + str(user_input))
        data = json.loads(r.text)

        # Access the content
        response = data['content']
        print("AI Girlfriend:", response)

        # Convert text response to speech
        engine.say(response)
        engine.runAndWait()


    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service. Please try again.")
