import pyautogui as pg
import time

import random
name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'




pg.hotkey('ctrl', 'winleft', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.3)

pg.hotkey('winleft', 'up')
pg.typewrite('gmail new account\n',.1)


time.sleep(2)
pg.click(420, 290)

time.sleep(2)
pg.hotkey('tab')
pg.hotkey('tab')

#Name
time.sleep(2)

counter=0
while counter < 6:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1

#Last
pg.hotkey('tab')

counter=0
while counter < 6:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1

#Username
pg.hotkey('tab')

counter=0
while counter < 6:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1

#Password
pg.hotkey('tab')
pg.hotkey('tab')
counter=0
while counter < 6:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1

#Confirm Password
time.sleep(2)
pg.hotkey('shift', 'up')

time.sleep(2)
pg.hotkey('ctrl','c')

pg.hotkey('tab')


pg.hotkey('ctrl', 'v')


