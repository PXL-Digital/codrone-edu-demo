from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

drone.takeoff()

# INSERT CODE HERE

drone.land()
drone.close()