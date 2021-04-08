import sys

import Movement

def DoPattern(sense, opName, opValue):
#    print(f'{opName} -> {opValue.__name__}')

    sense.clear()
    opValue(sense)

#
# Main
#
print(sys.argv)
if len(sys.argv) > 1:
    pattern = sys.argv[1]
else:
    pattern = 'Move'

if len(sys.argv) > 2:
    senseOption = sys.argv[2]
else:
    senseOption = 'UnSet'
# senseOption = os.environ.get("SenseHat", "Unset")
#print(f'SenseOption = {senseOption}')
if senseOption == "EMU":
    print("Using emulator per SenseHat setting...")
    from sense_emu import SenseHat
else:
    print("Using the real Sense Hat...")
    from sense_hat import SenseHat
# print(f'{sys.argv[0]} {pattern} {senseOption}')

sense = SenseHat()
sense.set_rotation(180) # Allows power supply to be away from viewer

if pattern == 'All':
    for opName, opValue in Movement.Operations.items():
        DoPattern(sense, opName, opValue)
else:
    opValue = Movement.Operations.get(pattern, Movement.MoveQuick)
    DoPattern(sense, pattern, opValue)
