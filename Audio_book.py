import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open('sample.pdf', 'rb'))
speaker = pyttsx3.init()
speaker.setProperty('rate', 175)
for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()