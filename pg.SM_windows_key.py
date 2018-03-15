#NAME - Fred Flintstone
#USERNAME - Flintstones31@gmail.com
#PASS - FredFlintstone7




import pyautogui as pg
import time

import random
name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'




pg.hotkey('ctrl', 'winleft', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n',.5)

pg.hotkey('winleft', 'up')
pg.hotkey('winleft', 'up')
pg.hotkey('winleft', 'up')
pg.typewrite('https://accounts.google.com/SignUp?hl=en\n',.1)


time.sleep(2)
pg.hotkey('tab')
pg.hotkey('tab')

#Name
time.sleep(.2)

counter=0
while counter < 15:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1

#Last
time.sleep(.2)

pg.hotkey('tab')

counter=0
while counter < 15:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1


#Username
time.sleep(.2)

pg.hotkey('tab')

counter=0
while counter < 15:
    pg.typewrite(symbols[random.randint(1,len(name)-1)])
    counter += 1

#Password
time.sleep(.2)
    
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
time.sleep(.2)
pg.hotkey('tab')

time.sleep(.2)
pg.typewrite(pw)

#DOB
year = str(random.randint(2003))
day = str(random.randit(1,31))

#Month
time.sleep(.2)

pg.hotkey('tab')
pg.hotkey('d')

#Day
pg.hotkey('tab')
pg.typewrite(day,.2)

#Year
pg.hotkey('tab')
pg.typewrite(year,.2)

#Gender
pg.hotkey('tab')
pg.hotkey('r')
pg.hotkey('tab')

#mobile Phone
pg.hotkey('tab')
time.sleep(.2)

#Current Email Address
pg.hotkey('tab')
time.sleep(.2)

pg.typewrite('Flintstones31@gmail.com')

#Location
pg.hotkey('tab')
pg.hotkey('tab')
time.sleep(.2)
#next step
pg.hotkey('space')
time.sleep(.2)

#Accept Terms and Conditions

pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)
pg.hotkey('tab')
time.sleep(.2)

pg.hotkey('space')

pg.hotkey('tab')  
time.sleep(.2)


pg.hotkey('space')
    

#Verify Email (NEED PHONE)



