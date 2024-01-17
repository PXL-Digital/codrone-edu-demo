from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

drone.takeoff()

drone.set_throttle(30)

drone.set_drone_LED(0,255,0,255)
drone.move(1)
drone.set_drone_LED(255,255,0,255)
drone.move(1)
drone.set_drone_LED(255,100,0,255)
drone.move(1)
drone.set_drone_LED(255,0,0,255)
drone.move(1)
drone.hover(3)

drone.land()
drone.close()