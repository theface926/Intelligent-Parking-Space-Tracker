import LCD1602
import time
LCD1602.init(0x27, 1)
#displays message on lcd screen until ctrl+c is pressed, then clears screen and prints lcd good to go to program terminal
try:
    while True:
        LCD1602.write(0,0, 'Hello World')
        LCD1602.write(0,1, 'begin Demo')
        #0,1 collumn first then row
except KeyboardInterrupt:
    time.sleep(0.3)
    LCD1602.clear()
    print('LCD Good to Go')