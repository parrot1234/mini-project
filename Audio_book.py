import PyPDF2
import pyttsx3
from pygame import mixer
import speech_recognition as sr
import os
import time




speaker = pyttsx3.init()
voices=speaker.getProperty('voices')
speaker.setProperty('voice','voices[0].id')
speaker.setProperty('rate', 140)

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            print("...")
            return "None"
        return statement
#speaker.setProperty('rate', 180)


pdf_File = open('FBA-UNIT1_final.pdf', 'rb')
#Create PDF Reader Object
pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages # counts number of pages in pdf
textList = []

#Extracting text data from each page of the pdf file
for i in range(count):
   try:
    page = pdf_Reader.getPage(i)    
    textList.append(page.extractText())
   except:
       pass

#Converting multiline text to single line text
textString = " ".join(textList)
speaker.save_to_file(textString,'Audio.wav')
speaker.runAndWait()
pdf_File.close()

mixer.init()

mixer.music.load('Audio.wav')
mixer.music.set_volume(0.7)
mixer.music.play()


while True:
      
   
    query = takeCommand().lower()
      
    if 'pause' in query:
  
        # Pausing the music
        mixer.music.pause()     
    elif 'resume' in query:
  
        # Resuming the music
        mixer.music.unpause()
    elif 'stop' in query:
  
        # Stop the mixer
        mixer.music.stop()
        break
speaker.stop()    