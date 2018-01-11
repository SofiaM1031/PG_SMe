import pyautogui as pg
import time

import random
name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'




pg.hotkey('ctrl', 'winleft', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.3)

pg.hotkey('winleft', 'up')
pg.hotkey('winleft', 'up')
pg.hotkey('winleft', 'up')
pg.typewrite('https://accounts.google.com/SignUp?hl=en\n',.1)


time.sleep(2)
pg.hotkey('tab')
pg.hotkey('tab')

#Name
time.sleep(2)

counter=0
while counter < 15:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1

#Last
time.sleep(2)

pg.hotkey('tab')

counter=0
while counter < 15:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1


#Username
time.sleep(2)

pg.hotkey('tab')

counter=0
while counter < 15:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1

#Password
time.sleep(2)
    
pg.hotkey('tab')
pg.hotkey('tab')
counter=0
pw=''
while counter < 15:
    a = symbols[random.randint(1,len(name)-1)]

    pg.typewrite(a)
    pw=pw+a

    counter += 1

#password saved as A

#Confirm Password
time.sleep(2)
pg.hotkey('tab')

time.sleep(2)
pg.typewrite(pw)


#Month
time.sleep(2)

pg.hotkey('tab')
pg.hotkey('down')
pg.hotkey('enter')
