import pyttsx3
import PyPDF2

book = open('sample.pdf', 'rb')
reader = PyPDF2.PdfFileReader(book)
totalPages = reader.numPages
print("total pages in book are {} ".format(totalPages))
voice = pyttsx3.init()
for i in range(0, totalPages):
    page = reader.getPage(i)
    text = page.extractText()
    voice.say(text)
    voice.runAndWait()
