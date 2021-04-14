import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# Set the pin standard
GPIO.setmode(GPIO.BOARD)

red = 8
green = 10
blue = 12

# Set up all the led pins with an initial value of low
GPIO.setup(red, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(green, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(blue, GPIO.OUT, initial=GPIO.LOW)

from tkinter import *
from tkinter import ttk

# Set up the root window for tkinter
root = Tk()
root.title("ledcontrol.py")

# Create a main frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Define functions for handling button events
def redOn():
	GPIO.output(red, GPIO.HIGH)
	GPIO.output(green, GPIO.LOW)
	GPIO.output(blue, GPIO.LOW)
	print('Red led On!!')

def greenOn():
	GPIO.output(red, GPIO.LOW)
	GPIO.output(green, GPIO.HIGH)
	GPIO.output(blue, GPIO.LOW)
	print('Green led On!!')

def blueOn():
	GPIO.output(red, GPIO.LOW)
	GPIO.output(green, GPIO.LOW)
	GPIO.output(blue, GPIO.HIGH)
	print('BLUE led On!!')

def exit():
	root.destroy()
	GPIO.cleanup()

# Create a label
ttk.Label(mainframe, text="Click  the buttons to control the LEDs.").grid(column=1, row=1, pady=12)

# Add radio buttons
v = IntVar()
ttk.Radiobutton(mainframe, text="Red", variable=v, value=1, command=redOn).grid(column=1, row=2, pady=12)
ttk.Radiobutton(mainframe, text="Green", variable=v, value=2, command=greenOn).grid(column=2, row=2, pady=12)
ttk.Radiobutton(mainframe, text="Blue", variable=v, value=3, command=blueOn).grid(column=3, row=2, pady=12)

# Add exit button
ttk.Button(mainframe, text="Exit", command=exit).grid(column=3, row=3, pady=12)

# Start the tk mainloop
root.mainloop()
