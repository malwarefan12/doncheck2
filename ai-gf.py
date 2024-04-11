import subprocess
import speech_recognition as sr
import requests
import json

recognizer = sr.Recognizer()

print("AI Girlfriend: Hi! I'm your virtual girlfriend. How can I help you today?")

def text_to_speech(text, voice='default', speed=160, amplitude=100):
    """
    Convert text to speech using eSpeak.
    
    Parameters:
        text (str): The text to be spoken.
        voice (str): The voice to use for speech synthesis. Default is 'default'.
        speed (int): The speed of speech in words per minute (default is 160).
        amplitude (int): The amplitude of speech (default is 100).
    
    Returns:
        None
    """
    # Build the eSpeak command
    command = [
        'espeak',
        '-v', voice,
        '-s', str(speed),
        '-a', str(amplitude),
        text
    ]
    
    # Execute the command
    subprocess.run(command)


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

        # Convert text response to speech using eSpeak
        text_to_speech(response)


    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service. Please try again.")
