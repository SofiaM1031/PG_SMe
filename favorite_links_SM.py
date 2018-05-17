import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=LYN6DRDQcjI","https://www.youtube.com/watch?v=8YGlzSl6cxU"]

hockey = ["https://www.google.com/search?q=rangers+game&rlz=1C1GCEA_enUS752US752&oq=rangers+game&aqs=chrome..69i57j0l5.2377j0j7&sourceid=chrome&ie=UTF-8"]

answer = pg.prompt (
"""
Which would you rather do
a) listen to bad music
b) find the scores to the Rangers game

"""
    )


if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in hockey:
        webbrowser.open(i)
        
