from sense_hat import SenseHat
import time

def FadeIn( sense, maxComponent ):
    for i in range (0,maxComponent):
        color = (i,0,i)
        sense.clear(color)
        time.sleep(0.1)

def Fade(sense, fadeRange):
    b = (1, 1, 1)
    g = (0, 180, 0)
    r = (180, 0, 0)
    blue = (0, 0, 180)

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


b = (0,180,0)
halfPurple = (64,0,64)
halfYellow = (64,64,0)

sense = SenseHat()
sense.set_rotation(180) # Allows power supply to be away from viewer
sense.clear()

Fade(sense, range(1,64))
sense.show_message("luuk is 7!!!", text_colour=halfYellow, back_colour=b)
Fade(sense, range(63,0,-1))


# FadeIn (sense, 64)

# #sense.show_message("Hello, World", text_colour=halfYellow, back_colour=halfPurple)
# sense.clear()

# FadeIn2(sense)
