from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

stop = False
while not stop:
    time.sleep(0.1)
    if drone.p_pressed():
        print("P button has been pressed!")
        drone.set_drone_LED(255,0,0,255)
        time.sleep(3)
        drone.takeoff()
    if drone.s_pressed():
        print("S button has been pressed!")
        drone.land()
        stop = True

drone.close()