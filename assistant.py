import speech_recognition as sr # this module supports speech recognition
import openai # this module allows us to communicate with OpenAI APIs
import os # this module allows us to interact with environment variables
from dotenv import load_dotenv
import subprocess

load_dotenv() # This loads the environment variables from the .env file
name = os.getenv('NAME')
api_key = os.getenv('OPEN_AI_KEY')
assistant_name = os.getenv('ASSISTANT_NAME')
conversation_size = os.getenv('CONVERSATION_SIZE')


r = sr.Recognizer() # Initialize the speech recognizer


conversation_history = [
    {"role": "system", "content": f"Your name is {assistant_name}. You're a helpful friend of {name}'s."}
]


def SpeakText(command): # Converts Speech to Text

    subprocess.run(['espeak', '-v', 'en+m1', '-s', '140', '-p', '60', '-g', '2', command])





def generate_response(text): # Function to interact with the OpenAI API (generates the text that the assistant speaks)

    openai.api_key = api_key
    
    conversation_history.append({"role": "user", "content": text})
    
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history
    )
    assistant_message = response.choices[0].message.content
    
    conversation_history.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message




while True: # The loop allows the program to constantly listen
    try:

        with sr.Microphone() as source2: # Use the microphone as source for input
            
            r.adjust_for_ambient_noise(source2, duration=0.5) # Continuous adjustment for ambient noise
            print("Adjusting for ambient noise. Please wait...")

            audio2 = r.listen(source2, timeout=None, phrase_time_limit=5) # Listen for the first phrase and extract it into audio data

            myText = r.recognize_google(audio2).lower() # Recognize speech using Google Speech Recognition
            
            if f"{assistant_name}" in myText: # Check if the recognized text contains the keyword
                
                print(f"Activated! You said: {myText}")
                generated_text = generate_response(myText)  # Send the text to the OpenAI API (GPT-4o-mini)
                SpeakText(f"{generated_text}") # Speak the answer that OpenAI generated
                
                
            #if (len(conversation_history) > conversation_size): # Keeps the conversation a certain size
               # conversation_history = conversation_history[:1]

            #else: # The user failed to specify the keyword that activates the assistant
              #  print(f"Listening... You said: {myText}")

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.UnknownValueError:
        print("No speech detected or speech was unintelligible.")