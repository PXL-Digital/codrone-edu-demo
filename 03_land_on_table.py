from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()
drone.takeoff()


def set_led(s):
    if s:
        drone.set_drone_LED(0, 255, 0, 255)
    else:
        drone.set_drone_LED(255, 0, 0, 255)

safe = False
set_led(safe)
while not safe:
    drone.set_pitch(30)
    drone.move(0.5)
    drone.hover(1)
    range_bottom = drone.get_bottom_range("cm")
    safe = (0 < range_bottom < 70)
    set_led(safe)

drone.land()
drone.close()
