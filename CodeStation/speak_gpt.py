import openai
import pyttsx3
import speech_recognition as sr
from openai_key import API_KEY

import move_servo

import time
import light_neopixel
print("Ready to go ... ")
# #NeoPixel = GREEN = Ready to listen
light_neopixel.pixels.fill((0, 255, 0))
light_neopixel.pixels.show()
time.sleep(5)

openai.api_key = API_KEY

engine = pyttsx3.init()
engine.setProperty('volume', 0.5)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1) 
# write script to find device index
#mic = sr.Microphone()

conversation = ""
user_name = "Farnaz"
bot_name = "Robot Study Companion"

# engine.say("Hello, I am your RSC, Robot Study Companion. How may I help you?")

#Wave Hi
move_servo.wave_hi()
print("waving Hi!")
time.sleep(2)

while True:
    with mic as source:
        print("\nlistening...")
        engine.say("I am listening")
        r.adjust_for_ambient_noise(source, duration=0.1) #background noise
        try:
            audio = r.listen(source, timeout=5) #set timeout to 5 seconds
        except sr.WaitTimeoutError:
            print("Microphone is not picking up any sound. Please check your microphone and try again.")
            continue
    print("no longer listening.\n")

    try:
        user_input = r.recognize_google(audio)
    except Exception as e:
        print(f"\nException occurred!:\n{e}\n")
        continue

    prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "

    conversation += prompt  # allows for context

    # fetch response from open AI api
    response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, max_tokens=300)
    response_str = response["choices"][0]["text"].replace("\n", "")
    # response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

    # conversation += response_str + "\n"
    # print(response_str)

    response_lines = response_str.split("\n")
    response_str = ""
    for line in response_lines:
        if user_name + ":" not in line and bot_name + ":" not in line:
            response_str += line.strip()

    conversation += bot_name + ": " + response_str + "\n"
    print(bot_name + ": " + response_str)
    
    engine.say(response_str)
    engine.runAndWait()

        # Turn off all LEDs
    light_neopixel.pixels.fill((0, 0, 0))
    light_neopixel.pixels.show()
    print("okay, bye ...")