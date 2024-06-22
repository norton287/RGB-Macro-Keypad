# Find it ALL here https://github.com/pimoroni/pmk-circuitpython/tree/main
# Keys are here https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py
# This uses CircuitPython which is a custom version of MicroPython, not Pimoroni's Build FYI
# The Pico when connected to your computer will show up as a USB drive, CircuitPython Auto Runs the file code.py first!
import math
import time
from pmk import PMK, number_to_xy, hsv_to_rgb
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

pmk = PMK(Hardware())

# Rotate the keypad 90 degrees
pmk.rotate(90)

# Insta Keys Array, you have keys 0-15.
keys = pmk.keys

# Set up the keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Time modifiers
short_debounce = 0.5
long_debounce = 0.15
debounce = 0.03

# Build the layers
layer1 = True
layer2 = False
layer3 = False

# Hold bool
fired = False

step = 0

while True:
    pmk.update()
    
    # Increment step for color shifting
    step += 1

    # Make a rainbow pattern matrix on the pads
    for i in range(16):
        # Convert the key number to an x/y coordinate to calculate the hue a matrix.
        x, y = number_to_xy(i)

        # Calculate the hue.
        hue = (x + y + (step / 20)) / 8
        hue = hue - int(hue)
        hue = hue - math.floor(hue)

        # Convert the hue to RGB values.
        r, g, b = hsv_to_rgb(hue, 1, 1)

        # Display it on the key!
        keys[i].set_led(r, g, b)    
    
    # Here are the 16 Keys from 0 - 15, they are rotated in the software at the top of this script by 90 degrees
    # If the key hasn't just fired (prevents refiring) then execute the key presses and set the debounce
    # These control the three layers Keys 0-2 0 = 1 1 = 2 2 = 3
    if keys[0].pressed:
        print("Key 0 pressed")
        if not fired:
            keys[0].set_led(255,255,255)
            fired = True
            debounce = short_debounce
            layer1 = True
            layer2 = False
            layer3 = False
            time.sleep(.5)
            keys[0].set_led(0,0,0)
    
    if keys[1].pressed:
        print("Key 1 pressed")
        if not fired:
            keys[1].set_led(255,255,255)
            fired = True
            debounce = short_debounce
            layer1 = False
            layer2 = True
            layer3 = False
            time.sleep(.5)
            keys[1].set_led(0,0,0)
    
    if keys[2].pressed:
        print("Key 2 pressed")
        if not fired:
            keys[2].set_led(255,255,255)
            fired = True
            debounce = short_debounce
            layer1 = False
            layer2 = False
            layer3 = True
            time.sleep(.5)
            keys[2].set_led(0,0,0)
    
    # Layer 1
    if layer1 == True:
        if keys[3].pressed:
            print("Key 3 pressed")
            if not fired:
                keys[3].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.V)
                time.sleep(.5)
                keys[3].set_led(0,0,0)
        
        if keys[4].pressed:
            print("Key 4 pressed")
            if not fired:
                keys[4].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.Z)
                time.sleep(.5)
                keys[4].set_led(0,0,0)
                
        if keys[5].pressed:
            print("Key 5 pressed")
            if not fired:
                keys[5].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.Y)
                time.sleep(.5)
                keys[5].set_led(0,0,0)
                
        if keys[6].pressed:
            print("Key 6 pressed")
            if not fired:
                keys[6].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.N)
                time.sleep(.5)
                keys[6].set_led(0,0,0)
        
        if keys[7].pressed:
            print("Key 7 pressed")
            if not fired:
                keys[7].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.ALT, Keycode.F4)
                time.sleep(.5)
                keys[7].set_led(0,0,0)
        
        if keys[8].pressed:
            print("Key 8 pressed")
            if not fired:
                keys[8].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.D)
                time.sleep(.5)
                keys[8].set_led(0,0,0)
                
        if keys[9].pressed:
            print("Key 9 pressed")
            if not fired:
                keys[9].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.RIGHT_SHIFT, Keycode.DELETE)
                time.sleep(.5)
                keys[9].set_led(0,0,0)
                
        if keys[10].pressed:
            print("Key 10 pressed")
            if not fired:
                keys[10].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.F2)
                time.sleep(.5)
                keys[10].set_led(0,0,0)
                
        if keys[11].pressed:
            print("Key 11 pressed")
            if not fired:
                keys[11].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.ESCAPE)
                time.sleep(.5)
                keys[11].set_led(0,0,0)
                
        if keys[12].pressed:
            print("Key 12 pressed")
            if not fired:
                keys[12].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.ALT, Keycode.TAB)
                time.sleep(.5)
                keys[12].set_led(0,0,0)
                
        if keys[13].pressed:
            print("Key 13 pressed")
            if not fired:
                keys[13].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.PRINT_SCREEN)
                time.sleep(.5)
                keys[13].set_led(0,0,0)
                
        if keys[14].pressed:
            print("Key 14 pressed")
            if not fired:
                keys[14].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.I)
                time.sleep(.5)
                keys[14].set_led(0,0,0)
        
        if keys[15].pressed:
            print("Key 15 pressed")
            if not fired:
                keys[15].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.E)
                time.sleep(.5)
                keys[15].set_led(0,0,0)
    
    if layer2 == True:
        if keys[3].pressed:
            print("Key 3 pressed")
            if not fired:
                keys[3].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.A)
                time.sleep(.5)
                keys[3].set_led(0,0,0)
        
        if keys[4].pressed:
            print("Key 4 pressed")
            if not fired:
                keys[4].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.D)
                time.sleep(.5)
                keys[4].set_led(0,0,0)
                
        if keys[5].pressed:
            print("Key 5 pressed")
            if not fired:
                keys[5].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.L)
                time.sleep(.5)
                keys[5].set_led(0,0,0)
                
        if keys[6].pressed:
            print("Key 6 pressed")
            if not fired:
                keys[6].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.V)
                time.sleep(.5)
                keys[6].set_led(255,255,255)
        
        if keys[7].pressed:
            print("Key 7 pressed")
            if not fired:
                keys[7].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.PERIOD)
                time.sleep(.5)
                keys[7].set_led(0,0,0)
        
        if keys[8].pressed:
            print("Key 8 pressed")
            if not fired:
                keys[8].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.PRINT_SCREEN)
                time.sleep(.5)
                keys[8].set_led(0,0,0)
                
        if keys[9].pressed:
            print("Key 9 pressed")
            if not fired:
                keys[9].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.RIGHT_SHIFT, Keycode.S)
                time.sleep(.5)
                keys[9].set_led(0,0,0)
                
        if keys[10].pressed:
            print("Key 10 pressed")
            if not fired:
                keys[10].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.LEFT_ARROW)
                time.sleep(.5)
                keys[10].set_led(0,0,0)
                
        if keys[11].pressed:
            print("Key 11 pressed")
            if not fired:
                keys[11].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.WINDOWS, Keycode.RIGHT_ARROW)
                time.sleep(.5)
                keys[13].set_led(0,0,0)
                
        if keys[12].pressed:
            print("Key 12 pressed")
            if not fired:
                keys[12].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.N)
                time.sleep(.5)
                keys[12].set_led(0,0,0)
                
        if keys[13].pressed:
            print("Key 13 pressed")
            if not fired:
                keys[13].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.RIGHT_SHIFT, Keycode.N)
                time.sleep(.5)
                keys[13].set_led(0,0,0)
                
        if keys[14].pressed:
            print("Key 14 pressed")
            if not fired:
                keys[14].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.RIGHT_SHIFT, Keycode.T)
                time.sleep(.5)
                keys[14].set_led(0,0,0)
        
        if keys[15].pressed:
            print("Key 15 pressed")
            if not fired:
                keys[15].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.TAB)
                time.sleep(.5)
                keys[13].set_led(0,0,0)
                
    if layer3 == True:
        if keys[3].pressed:
            print("Key 3 pressed")
            if not fired:
                keys[3].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.PAGE_UP)
                time.sleep(.5)
                keys[3].set_led(0,0,0)
        
        if keys[4].pressed:
            print("Key 4 pressed")
            if not fired:
                keys[4].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.ALT, Keycode.F)
                time.sleep(.5)
                keys[4].set_led(0,0,0)
        
        if keys[5].pressed:
            print("Key 5 pressed")
            if not fired:
                keys[5].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.PAGE_UP)
                time.sleep(.5)
                keys[5].set_led(0,0,0)
                
        if keys[6].pressed:
            print("Key 6 pressed")
            if not fired:
                keys[6].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.ONE)
                time.sleep(.5)
                keys[6].set_led(0,0,0)
        
        if keys[7].pressed:
            print("Key 7 pressed")
            if not fired:
                keys[7].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.TWO)
                time.sleep(.5)
                keys[7].set_led(0,0,0)
        
        if keys[8].pressed:
            print("Key 8 pressed")
            if not fired:
                keys[8].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.THREE)
                time.sleep(.5)
                keys[8].set_led(0,0,0)
                
        if keys[9].pressed:
            print("Key 9 pressed")
            if not fired:
                keys[9].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.FOUR)
                time.sleep(.5)
                keys[9].set_led(0,0,0)
                
        if keys[10].pressed:
            print("Key 10 pressed")
            if not fired:
                keys[10].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.FIVE)
                time.sleep(.5)
                keys[10].set_led(0,0,0)
                
        if keys[11].pressed:
            print("Key 11 pressed")
            if not fired:
                keys[11].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.SIX)
                time.sleep(.5)
                keys[11].set_led(0,0,0)
                
        if keys[12].pressed:
            print("Key 12 pressed")
            if not fired:
                keys[12].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.SEVEN)
                time.sleep(.5)
                keys[12].set_led(0,0,0)
                
        if keys[13].pressed:
            print("Key 13 pressed")
            if not fired:
                keys[13].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.EIGHT)
                time.sleep(.5)
                keys[13].set_led(0,0,0)
                
        if keys[14].pressed:
            print("Key 14 pressed")
            if not fired:
                keys[14].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.CONTROL, Keycode.NINE)
                time.sleep(.5)
                keys[14].set_led(0,0,0)
        
        if keys[15].pressed:
            print("Key 15 pressed")
            if not fired:
                keys[15].set_led(255,255,255)
                fired = True
                debounce = short_debounce
                keyboard.send(Keycode.ALT, Keycode.F)
                time.sleep(.5)
                keys[15].set_led(0,0,0)
    
    # Reset keypress watcher
    if fired and time.monotonic() - pmk.time_of_last_press > debounce:
        fired = False
