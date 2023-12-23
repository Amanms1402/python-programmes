import pyttsx3
#import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
                                       # getting details of current speaking rate
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
speak ("") 

    
