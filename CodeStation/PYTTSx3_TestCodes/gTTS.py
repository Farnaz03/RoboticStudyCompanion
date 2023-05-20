# # Import the required module for text
# # to speech conversion
# from gtts import gTTS

# # This module is imported so that we can
# # play the converted audio
# import os

# # The text that you want to convert to audio
# mytext = 'Welcome to geeksforgeeks!'

# # Language in which you want to convert
# language = 'en'

# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)

# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("welcome.mp3")

# # Playing the converted file
# os.system("mpg321 welcome.mp3")


from gtts import gTTS
from playsound import playsound
# import pyttsx3
# engine = pyttsx3.init() 

text_to_speech = gTTS('I will say what you write')
text_to_speech.save('TTS.mp3')
print(text_to_speech)

playsound('TTS.mp3')
# engine.say(text_to_speech)
# engine.runAndWait()
