
#have split screen on the left and have two tabs open

import pyautogui as pg
import random
name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

pg.moveTo(1104, 34)
pg.click(1104, 34)

pg.typewrite('gmail sign in\n')
pg.moveTo(977, 310, 1)
pg.click(977, 310,)

pg.moveTo(883,497,1)
pg.click(883,497)

pg.moveTo(897, 505,1)
pg.click(897, 505)

pg.moveTo(938, 269,1)
pg.click(938, 269)

counter=0
while counter < 10:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1

    
