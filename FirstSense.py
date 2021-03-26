from sense_hat import SenseHat
import time

def FadeIn(sense, max)
    for i in range (0,max)
        color = (i,0,2*i)
        sense.clear(color)
        time.sleep(0.05)


purple = (64,0,128)
halfPurple = (32,0,64)
halfYellow = (64,64,0)



sense = SenseHat()
sense.set_rotation(180) # Allows power supply to be away from viewer
FadeIn (sense, 32)

sense.show_message("Hello, World", text_colour=halfYellow, back_colour=halfPurple)
sense.clear()

