'''
this program allows you to control the tello drone using the computer keyboard

'''



import keyboard as key     
from djitellopy import tello
from time import sleep


key.init()
drone = tello.Tello()
drone.connect()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    
    if key.getkey('LEFT'): lr =  -speed
    elif key.getkey('RIGHT'): lr = speed
    
    if key.getkey('UP'): fb = -speed
    elif key.getkey('DOWN'): ud = speed
    
    if key.getkey('w'): fb = speed
    elif key.getkey('s'): fb = -speed
    
    if key.getkey('a'): yv = speed
    elif key.getkey('d'): yv = -speed
    
    if key.getkey('f'): drone.flip_forward()
    if key.getkey('t'): drone.takeoff()
    
    
        
    if key.getkey('q'): drone.land()
        
    return [lr, fb, ud, yv]
    

drone.takeoff()

while True:
    vals = getKeyboardInput()
    drone.send_rc_constrol(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
    