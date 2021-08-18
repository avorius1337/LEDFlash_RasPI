#LED_button_press.py
#gpio 2 is led
#gpio 3 is button

from signal import pause
from gpiozero import LED, Button
from time import sleep

button = Button(3)
led = LED(2)
cycleState = False

def fire_cycle():
    
    global cycleState
    
    if cycleState:
        led.on()
        sleep(0.25)
        led.off()
        cycleState = False  
    else:   
        return

def makeCycleTrue():
    
    global cycleState
    cycleState = True
    
try:
    
    button.when_pressed = fire_cycle
    button.when_released = makeCycleTrue
    pause()

finally:
    pass
