import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb


speak = wincl.Dispatch ("SAPI.SpVoice")

#speak.Speak ("What's ur naME")

#pg.prompt

#name = pg.prompt("Enter name")

#speak.Speak ("Hello " + name + " what's your favorite food")

#food = pg.prompt("Enter favorite food")

#elif food == "Water":
    #speak.Speak("Be careful with thay")

#else:
   # speak.Speak ("You like to eat " + food + " I'm still learning what that is.")


speak.Speak("What video would you like to watch?")

video = pg.prompt("Enter your video below.")

speak.Speak("Ok, looking for " + video + "on Youtube")

wb.open("https://www.youtube.com/results?search_query=" + video)
