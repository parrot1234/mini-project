import instaloader
import pyttsx3
import speech_recognition as sr

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





ig = instaloader.Instaloader()
# dp = input("Enter Insta username : ")
speak("tell me Insta username")
dp=takeCommand().lower()
dp=dp.replace(" ","")
dp=dp.replace("underscore","_")
dp=dp.replace("dot",".")
print(dp)
ig.download_profile(dp , profile_pic_only=True)
