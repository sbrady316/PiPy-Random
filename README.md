# PiPy-Random
Collection of python scripts I create while exploring my Raspberry Pi

# How-To
## Deploying to Pi
This does the following
* Uses scp to copy the "release" directory to the Pi
* Uses SSH to launch a python script
```Powershell
scp -i C:\Users\sbrady\.ssh\sbrady-s2.pi.pem C:\C\PiPy-Random\* shane@192.168.0.30:/home/shane/C/PiPy-Random/; ssh shane@192.168.0.30 -i C:/Users/sbrady/.ssh/sbrady-s2.pi.pem  python3 ~/C/PiPy-Random/Harness.py Hump
```

# Next Steps
Keeping track of next things to try
## Harness
* Use better command line parsing
* Add encapsulation to movement logic

## Movement
* Add a tail to the dot moving around
* Non-circular pattern

## Graphics
* Can I do this with a different matrix from the sense hat and friends
* Run directly on dev workstation
* Get access to Markku's Pi :-)

## Deployments
* sudo errors out (understandably) in the ssh command.  Need to understand how to access the Sense HAT over ssh automation