import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import speech_recognition as sr
import pyttsx3

# Load pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("Koriyy/DialoGPT-medium-gf")  # Replace with your fine-tuned model directory

# Initialize SpeechRecognition recognizer
recognizer = sr.Recognizer()

# Initialize pyttsx3 engine
engine = pyttsx3.init()

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

        # Tokenize input
        input_ids = tokenizer.encode(user_input, return_tensors="pt")

        # Generate response
        with torch.no_grad():
            output = model.generate(input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id, num_return_sequences=1)

        # Decode response
        bot_response = tokenizer.decode(output[0], skip_special_tokens=True)
        print("AI Girlfriend:", bot_response)

        # Speak the response
        engine.say(bot_response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service. Please try again.")
