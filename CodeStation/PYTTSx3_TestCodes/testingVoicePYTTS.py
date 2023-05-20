
### Loop for checking various voice
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id[3])
# #    print(voice.id[3])
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

##################################################################################################################
import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print("Rate: ", rate)                        #printing current voice rate
engine.setProperty('rate', 150)


# engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0)
voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[17].id)
# engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
engine.say('Sunset ... oh no ... another day has gone by')
engine.runAndWait() 

################################################################################################################
import speech_recognition as sr

r = sr.Recognizer()

print(sr.Microphone.list_microphone_names())

    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', 135)
    
    # voices = engine.getProperty('voices')
    # #print(voices[11])
    # engine.setProperty('voice', voices[1].id)
    # #engine.setProperty('voice', 'english+f3') #female voice
    
#################################################################################################################
### Loop for checking voices
# https://stackoverflow.com/questions/44858120/how-to-change-the-voice-in-pyttsx3

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
    if voice.languages[0] == u'en_US':
        engine.setProperty('voice', voice.id)
        break

engine.say('Hello World')

<Voice id=afrikaans
          name=afrikaans
          languages=[b'\x05af']
          gender=male
          age=None>
<Voice id=aragonese
          name=aragonese
          languages=[b'\x05an']
          gender=male
          age=None>
<Voice id=bulgarian
          name=bulgarian
          languages=[b'\x05bg']
          gender=None
          age=None>
<Voice id=bosnian
          name=bosnian
          languages=[b'\x05bs']
          gender=male
          age=None>
<Voice id=catalan
          name=catalan
          languages=[b'\x05ca']
          gender=male
          age=None>
<Voice id=czech
          name=czech
          languages=[b'\x05cs']
          gender=male
          age=None>
<Voice id=welsh
          name=welsh
          languages=[b'\x05cy']
          gender=male
          age=None>
<Voice id=danish
          name=danish
          languages=[b'\x05da']
          gender=male
          age=None>
<Voice id=german
          name=german
          languages=[b'\x05de']
          gender=male
          age=None>
<Voice id=greek
          name=greek
          languages=[b'\x05el']
          gender=male
          age=None>
<Voice id=default
          name=default
          languages=[b'\x05en']
          gender=male
          age=None>
<Voice id=english
          name=english
          languages=[b'\x02en-gb']
          gender=male
          age=None>
<Voice id=en-scottish
          name=en-scottish
          languages=[b'\x05en-sc']
          gender=male
          age=None>
<Voice id=english-north
          name=english-north
          languages=[b'\x05en-uk-north']
          gender=male
          age=None>
<Voice id=english_rp
          name=english_rp
          languages=[b'\x05en-uk-rp']
          gender=male
          age=None>
<Voice id=english_wmids
          name=english_wmids
          languages=[b'\x05en-uk-wmids']
          gender=male
          age=None>
<Voice id=english-us
          name=english-us
          languages=[b'\x02en-us']
          gender=male
          age=None>
<Voice id=en-westindies
          name=en-westindies
          languages=[b'\x05en-wi']
          gender=male
          age=None>
<Voice id=esperanto
          name=esperanto
          languages=[b'\x05eo']
          gender=male
          age=None>
<Voice id=spanish
          name=spanish
          languages=[b'\x05es']
          gender=male
          age=None>
<Voice id=spanish-latin-am
          name=spanish-latin-am
          languages=[b'\x05es-la']
          gender=male
          age=None>
<Voice id=estonian
          name=estonian
          languages=[b'\x05et']
          gender=None
          age=None>
<Voice id=persian
          name=persian
          languages=[b'\x05fa']
          gender=None
          age=None>
<Voice id=persian-pinglish
          name=persian-pinglish
          languages=[b'\x05fa-pin']
          gender=None
          age=None>
<Voice id=finnish
          name=finnish
          languages=[b'\x05fi']
          gender=male
          age=None>
<Voice id=french-Belgium
          name=french-Belgium
          languages=[b'\x05fr-be']
          gender=male
          age=None>
<Voice id=french
          name=french
          languages=[b'\x05fr-fr']
          gender=male
          age=None>
<Voice id=irish-gaeilge
          name=irish-gaeilge
          languages=[b'\x05ga']
          gender=None
          age=None>
<Voice id=greek-ancient
          name=greek-ancient
          languages=[b'\x05grc']
          gender=male
          age=None>
<Voice id=hindi
          name=hindi
          languages=[b'\x05hi']
          gender=male
          age=None>
<Voice id=croatian
          name=croatian
          languages=[b'\x05hr']
          gender=male
          age=None>
<Voice id=hungarian
          name=hungarian
          languages=[b'\x05hu']
          gender=male
          age=None>
<Voice id=armenian
          name=armenian
          languages=[b'\x05hy']
          gender=male
          age=None>
<Voice id=armenian-west
          name=armenian-west
          languages=[b'\x05hy-west']
          gender=male
          age=None>
<Voice id=indonesian
          name=indonesian
          languages=[b'\x05id']
          gender=male
          age=None>
<Voice id=icelandic
          name=icelandic
          languages=[b'\x05is']
          gender=male
          age=None>
<Voice id=italian
          name=italian
          languages=[b'\x05it']
          gender=male
          age=None>
<Voice id=lojban
          name=lojban
          languages=[b'\x05jbo']
          gender=None
          age=None>
<Voice id=georgian
          name=georgian
          languages=[b'\x05ka']
          gender=None
          age=None>
<Voice id=kannada
          name=kannada
          languages=[b'\x05kn']
          gender=None
          age=None>
<Voice id=kurdish
          name=kurdish
          languages=[b'\x05ku']
          gender=male
          age=None>
<Voice id=latin
          name=latin
          languages=[b'\x05la']
          gender=male
          age=None>
<Voice id=lingua_franca_nova
          name=lingua_franca_nova
          languages=[b'\x05lfn']
          gender=male
          age=None>
<Voice id=lithuanian
          name=lithuanian
          languages=[b'\x05lt']
          gender=male
          age=None>
<Voice id=latvian
          name=latvian
          languages=[b'\x05lv']
          gender=male
          age=None>
<Voice id=macedonian
          name=macedonian
          languages=[b'\x05mk']
          gender=male
          age=None>
<Voice id=malayalam
          name=malayalam
          languages=[b'\x05ml']
          gender=male
          age=None>
<Voice id=malay
          name=malay
          languages=[b'\x05ms']
          gender=male
          age=None>
<Voice id=nepali
          name=nepali
          languages=[b'\x05ne']
          gender=male
          age=None>
<Voice id=dutch
          name=dutch
          languages=[b'\x05nl']
          gender=male
          age=None>
<Voice id=norwegian
          name=norwegian
          languages=[b'\x05no']
          gender=male
          age=None>
<Voice id=punjabi
          name=punjabi
          languages=[b'\x05pa']
          gender=None
          age=None>
<Voice id=polish
          name=polish
          languages=[b'\x05pl']
          gender=male
          age=None>
<Voice id=brazil
          name=brazil
          languages=[b'\x05pt-br']
          gender=male
          age=None>
<Voice id=portugal
          name=portugal
          languages=[b'\x05pt-pt']
          gender=male
          age=None>
<Voice id=romanian
          name=romanian
          languages=[b'\x05ro']
          gender=male
          age=None>
<Voice id=russian
          name=russian
          languages=[b'\x05ru']
          gender=male
          age=None>
<Voice id=slovak
          name=slovak
          languages=[b'\x05sk']
          gender=male
          age=None>
<Voice id=albanian
          name=albanian
          languages=[b'\x05sq']
          gender=male
          age=None>
<Voice id=serbian
          name=serbian
          languages=[b'\x05sr']
          gender=male
          age=None>
<Voice id=swedish
          name=swedish
          languages=[b'\x05sv']
          gender=male
          age=None>
<Voice id=swahili-test
          name=swahili-test
          languages=[b'\x05sw']
          gender=male
          age=None>
<Voice id=tamil
          name=tamil
          languages=[b'\x05ta']
          gender=male
          age=None>
<Voice id=turkish
          name=turkish
          languages=[b'\x05tr']
          gender=male
          age=None>
<Voice id=vietnam
          name=vietnam
          languages=[b'\x05vi']
          gender=male
          age=None>
<Voice id=vietnam_hue
          name=vietnam_hue
          languages=[b'\x05vi-hue']
          gender=male
          age=None>
<Voice id=vietnam_sgn
          name=vietnam_sgn
          languages=[b'\x05vi-sgn']
          gender=male
          age=None>
<Voice id=Mandarin
          name=Mandarin
          languages=[b'\x05zh']
          gender=male
          age=None>
<Voice id=cantonese
          name=cantonese
          languages=[b'\x05zh-yue']
          gender=male
          age=None>