# import openai
# import pyttsx3
# import speech_recognition as sr
# from api_key import API_KEY


# openai.api_key = API_KEY

# engine = pyttsx3.init()

# rec = sr.Recognizer()
# # mic = sr.Microphone(device_index=1)

# def speak(word):
#     engine.setProperty('rate', 135)
#     engine.setProperty('volume', 0.8)

#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)

#     engine.say(str(word))
#     engine.runAndWait()
#     engine.stop()


# conversation = ""
# user_name = "Farnaz"
# bot_name = "TinyHelper"

# while True:
#     with sr.Microphone() as source:
#         print("\nlistening...")
#         rec.adjust_for_ambient_noise(source, duration=0.1) #background noise
#         speak('hello, I am listening for your command')
#         try:
#             audio = rec.listen(source, timeout=5) #set timeout to 5 seconds
#         except sr.WaitTimeoutError:
#             print("Microphone is not picking up any sound. Please check your microphone and try again.")
#             continue
#     print("no longer listening.\n")

#     try:
#         user_input = rec.recognize_google(audio)
#     except Exception as e:
#         print(f"\nException occurred!:\n{e}\n")
#         continue

#     prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "

#     conversation += prompt  # allows for context

#     # fetch response from open AI api
#     response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, max_tokens=300)
#     #gpt-3.5-turbo   or    gpt-3.5-turbo-0301
    
    
#     response_str = response["choices"][0]["text"].replace("\n", "")
#     # response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

#     # conversation += response_str + "\n"
#     # print(response_str)

#     response_lines = response_str.split("\n")
#     response_str = ""
#     for line in response_lines:
#         if user_name + ":" not in line and bot_name + ":" not in line:
#             response_str += line.strip()

#     conversation += bot_name + ": " + response_str + "\n"
#     print(bot_name + ": " + response_str)

#     engine.say(response_str)
#     engine.runAndWait()
###################################################################

import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init(driverName='espeak')

# Set the voice properties
engine.setProperty('rate', 135)
engine.setProperty('volume', 0.6)
voices = engine.getProperty('voices')
# engine.setProperty('voice', 'english-us')
# engine.setProperty('voice', voices[11].id)

# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Use the speak() function to say something
speak("Hello, world!")


# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

for v in voices:
    print(v.name, v.gender, v.languages)

# default male [b'\x05en']
# english male [b'\x02en-gb']
# en-scottish male [b'\x05en-sc']
# english-north male [b'\x05en-uk-north']
# english_rp male [b'\x05en-uk-rp']
# english_wmids male [b'\x05en-uk-wmids']
# english-us male [b'\x02en-us']