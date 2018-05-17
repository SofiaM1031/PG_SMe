import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()

with sr.Microphone () as source:
    speak.Speak("What do you want to look for")
    print("Listening....")
    audio = r.listen(source)
    print("Thinking.....")

try:
    words = r.recognize_google(audio)

    speak.Speak("Ok then, searching for " + r.recognize_google(audio) + " on Google")
    wb.open("https://www.google.com/search?q=" + words)
    

except sr.UnknownValueError:
        print ("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
        print ("Could not get results on Google")


 

    
    
    
