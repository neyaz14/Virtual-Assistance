import speech_recognition as sr
import pyttsx3
import datetime

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

alexa.say("hi")
alexa.runAndWait()


try:
    with sr.Microphone() as source:
        print('listening.....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)



        print(command)

except:
    pass



