import time

def Move(sense):
    for y in range(0,8):
        for x in range(0,8):
            sense.set_pixel(x,y,fore)
            time.sleep(0.1)
            if x == 3 or x == 4:
                sense.set_pixel(x,y,yellow)
            else:
                sense.set_pixel(x,y,back)

def Move2(sense):
    for y in range(0,8):
        blueLevel = 32*y + 31
        for x in range(0,8):
            intensity = (4 - abs(x - 4)) * 64 - 1
            # if y == 0:
                # print(f'x = {x}, intensity = {intensity}')
            # intensity = min(255,intensity*2)
            # Guard
            intensity = max(0, min(255, intensity))
            sense.set_pixel(x,y,(intensity, 0, blueLevel))
            time.sleep(0.1)

# Move a box around the permiter
def MovePerimiter(sense):
    x = 0
    y = 0
    xOffset = 1
    yOffset = 0
    for i in range(0,65):
        sense.set_pixel(x,y,fore)
        time.sleep(0.05)
        sense.set_pixel(x,y,yellow)

        if x == 0:
            if y == 0:
                xOffset = 1
                yOffset = 0
            elif y == 7:
                xOffset = 0
                yOffset = -1
        elif x == 7:
            if y == 0:
                xOffset = 0
                yOffset = 1
            elif y == 7:
                xOffset = -1
                yOffset = 0

        x += xOffset
        y += yOffset

# Move with a tail
def MoveTail(sense):
    x = 0
    y = 0
    xOffset = 1
    yOffset = 0
    for i in range(0,65):
        sense.set_pixel(x,y,fore)
        time.sleep(0.05)
        sense.set_pixel(x,y,back)

        if x == 0:
            if y == 0:
                xOffset = 1
                yOffset = 0
            elif y == 7:
                xOffset = 0
                yOffset = -1
        elif x == 7:
            if y == 0:
                xOffset = 0
                yOffset = 1
            elif y == 7:
                xOffset = -1
                yOffset = 0

        x += xOffset
        y += yOffset

def MoveQuick(sense):
    x = 0
    y = 0
    xOffset = 1
    yOffset = 0
    for i in range(0,32):
        sense.set_pixel(x,y,fore)
        time.sleep(0.03)
        sense.set_pixel(x,y,back)

        if x == 0:
            if y == 0:
                xOffset = 1
                yOffset = 0
            elif y == 4:
                xOffset = 0
                yOffset = -1
        elif x == 4:
            if y == 0:
                xOffset = 0
                yOffset = 1
            elif y == 4:
                xOffset = -1
                yOffset = 0

        x += xOffset
        y += yOffset



halfPurple = (64,0,64)
halfYellow = (64,64,0)
yellow = (255,255,0)
black = (0,0,0)
blue = (0, 0, 255)

fore = blue
back = black

Operations = {
    'Tail': MoveTail,
    'Perimeter': MovePerimiter,
    'Bar': Move,
    'Hump': Move2,
    'Quick': MoveQuick,
}

