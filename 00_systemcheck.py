from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()
#drone.get_trim()
#drone.set_trim(-3,0) # Compensates imbalance in flying drone

drone.set_drone_LED(0,0,255,255)

drone.drone_buzzer(Note.C4, 200)
drone.drone_buzzer(Note.E4, 200)
drone.drone_buzzer(Note.G4, 200)
drone.drone_buzzer(Note.C5, 200)

drone.takeoff()
drone.hover(3)

# Movement: set properties and call move for given duration
# Set-methods require power value between [-100, 100]
#drone.set_roll(-5)     # negative is left, positive is right
#drone.set_pitch(20)    # positive is forward, negative is backward
#drone.set_yaw(40)      # turn. Positive = topview counterclockwise
#drone.set_throttle(40) # positive is ascend
#drone.move(1)          # execute move with programmed paramters. duration in seconds.

# Move forward
drone.set_pitch(40) # rustig vooruit bewegen bij volgende move
drone.move(2)       # in seconden
drone.set_pitch(0)  # terug uitschakelen (power = 0), anders zal dit volgende move ook nog actief zijn

# Turn around
drone.set_yaw(50) # draai in tegenwijzerzin
drone.move(3) # in seconden

drone.land()

drone.drone_buzzer(Note.C5, 200)
drone.drone_buzzer(Note.G4, 200)
drone.drone_buzzer(Note.E4, 200)
drone.drone_buzzer(Note.C4, 200)

drone.close()