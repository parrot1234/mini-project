
import pyttsx3
import speech_recognition as sr
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
engine.setProperty('rate', 140)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement



speak("Tell me the mobile number to track")
number = takeCommand()
number=number.replace(" ","")
#print(number)
speak("this is what i found")
ch_number = phonenumbers.parse(number, "CH")
speak(geocoder.description_for_number(ch_number, "en"))
print(geocoder.description_for_number(ch_number, "en"))
service_provider = phonenumbers.parse(number, "RO")
speak(carrier.name_for_number(service_provider, "en"))
print(carrier.name_for_number(service_provider, "en"))