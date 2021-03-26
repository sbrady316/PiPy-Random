from sense_hat import SenseHat

purple = (64,0,128)
halfPurple = (32,0,64)
#halfYellow = (128,128,0)

sense = SenseHat()
sense.set_rotation(180)
sense.show_message("Hello, World", text_colour=(128,128,0), back_colour=halfPurple)
#sense.clear(halfPurple)
sense.clear()

