import subprocess
import requests
import json

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
    # Use Termux speech-to-text
    user_input = subprocess.getoutput("termux-speech-to-text")
    print("You:", user_input)

    try:
        # Get response from chatbot
        r = requests.get("""https://freeaiapi.vercel.app/api/ChitChat?query=""" + str(user_input))
        data = json.loads(r.text)

        # Access the content
        response = data['content']
        print("AI Girlfriend:", response)

        # Convert text response to speech using eSpeak
        text_to_speech(response)


    except Exception as e:
        print("An error occurred:", str(e))
