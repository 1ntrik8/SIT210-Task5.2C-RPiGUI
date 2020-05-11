# Leigh Rowell
# ID: 219309149
# SIT210 - 5.2C

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## Hardware
ledRed = LED(14)
ledGreen = LED(15)
ledBlue = LED(16)

## Gui Definitions
win=Tk()
win.title("SIT210 - 5.2C")
win.geometry("200x90")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')

## Event functions
def ledAllOff():
    ledRed.off()
    ledGreen.off()
    ledBlue.off()

def ledToggle():
    ledOption = str(value.get())
    label.config(text = ledOption)
    ledAllOff()

    if ledOption == 'red':
        ledRed.on()
    if ledOption == 'green':
        ledGreen.on()
    if ledOption == 'blue':
        ledBlue.on()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

## widgets
value  =  StringVar ()
redButton  =  Radiobutton ( win,  text = "Red" ,  variable = value ,  value = 'red' ,
    command = ledToggle)
greenButton  =  Radiobutton ( win ,  text = "Green" ,  variable = value ,  value = 'green' ,
    command = ledToggle)
blueButton  =  Radiobutton ( win ,  text = "Blue",  variable = value ,  value = 'blue' ,
    command = ledToggle)
redButton.pack(anchor = W)
greenButton.pack(anchor = W)
blueButton.pack(anchor = W)

label = Label(win)
label.pack()

win.protocol("WM_DELETE_WINDOW", close) # Close cleanly when clicking window X..

win.mainloop() # Loop forever and keep GUI running.