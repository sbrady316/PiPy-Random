import os
import sys
import time

if len(sys.argv) > 1:
    senseOption = sys.argv[1]
else:
    senseOption = 'UnSet'
# senseOption = os.environ.get("SenseHat", "Unset")
print(f'SenseOption = {senseOption}')
if senseOption == "EMU":
    print("Using emulator per SenseHat setting...")
    from sense_emu import SenseHat
else:
    print("Using the real Sense Hat...")
    from sense_hat import SenseHat

def FadeIn( sense, maxComponent ):
    for i in range (0,maxComponent):
        color = (i,0,i)
        sense.clear(color)
        time.sleep(0.1)

def Fade(sense, fadeRange):
    b = (1, 1, 1)
    g = (0, 180, 0)
    r = (180, 0, 0)

    canvas = [
        b, b, b, b, b, b, b, b,
        b, g, b, g, b, g, b, g,
        b, r, b, r, b, r, b, r,
        b, blue, b, blue, b, blue, b, blue,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b
    ]

    for i in fadeRange:
        canvas[i] = g
        sense.set_pixels(canvas)
        time.sleep(0.05)

def Move(sense):
    for y in range(0,8):
        for x in range(0,8):
            sense.set_pixel(x,y,fore)
            time.sleep(0.1)
            if x == 7:
                sense.set_pixel(x,y,(0,255,0))
            else:
                sense.set_pixel(x,y,back)


halfPurple = (64,0,64)
halfYellow = (64,64,0)
black = (0,0,0)
blue = (0, 0, 255)

fore = blue
back = black

sense = SenseHat()
sense.set_rotation(180) # Allows power supply to be away from viewer
sense.clear()

Move(sense)

# Fade(sense, range(1,64))

# sense.show_message("luuk is 7!!!", text_colour=halfYellow, back_colour=b)
# Fade(sense, range(63,0,-1))


# FadeIn (sense, 64)

# #sense.show_message("Hello, World", text_colour=halfYellow, back_colour=halfPurple)
# sense.clear()

# FadeIn2(sense)
