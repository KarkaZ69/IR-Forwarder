from m5stack import *
from m5ui import *
from uiflow import *
import machine
import time

input_pin = machine.Pin(26, machine.Pin.IN)  
ir_out = machine.Pin(19, machine.Pin.OUT)    


lcd.clear()
lcd.font(lcd.FONT_DefaultSmall) 
setScreenColor(0x000000)


lcd.print("IR Forwarder", 5, 5, 0xffffff)
lcd.print("G26->A7", 5, 20, 0x00ff00)
lcd.print("Status:", 5, 35, 0xffff00)


lcd.fillRect(60, 35, 8, 8, 0x333333)  

last_state = 1
signal_count = 0

while True:
    current_state = input_pin.value()

    ir_out.value(current_state)
    

    if current_state != last_state:
        signal_count += 1
        lcd.fillRect(60, 35, 8, 8, 0xff0000 if current_state == 0 else 0x00ff00)
        last_state = current_state
    

    if signal_count % 10 == 0:  
        lcd.fillRect(80, 35, 40, 8, 0x000000)  
        lcd.print(str(signal_count), 80, 35, 0xffffff)
    

    time.sleep_us(30) 
    

    if btnA.wasPressed():
        lcd.print("X", 120, 5, 0xff0000)
        time.sleep_ms(300)
        machine.reset()
