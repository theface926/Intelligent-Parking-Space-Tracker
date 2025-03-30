import LCD1602
import time
LCD1602.init(0x27, 1)
#def setup():
    #LCD1602.init(0x27, 1)   # init(slave address, background light)
    #LCD1602.write(0, 0, 'Greetings!!')
    #LCD1602.write(1, 1, 'from SunFounder')
    #time.sleep(2)
def blankMessage():
    LCD1602.write(0,0,'')
    LCD1602.write(0,1,'')
import random
try:
    while True:
        #setup()
        #time.sleep(3)
        #LCD1602.write(2,0, "Have a cow")
        #LCD1602.write(4,1, "Man")
        blankMessage()
        num = 0
        num = random.randint(10,110)
        top = 'Random Number:'
        if (num > 100):
            top += ' >100'
        bot = str(num)
        LCD1602.write(0,0, top)
        LCD1602.write(0,1, bot)
        #s = str(random.randint(10,200))
        
        #LCD1602.write(0,0, 'Random Number:')
        #LCD1602.write(0,1, s)
        #0,1 collumn first then row
        time.sleep(0.25)
except KeyboardInterrupt:
    time.sleep(0.3)
    blankMessage()
    LCD1602.write(0,0, 'keyboard interrupt')
    time.sleep(2)
    blankMessage()
    time.sleep(3)
    print('LCD Good to Go')