from codrone_edu.drone import *
import time

def blink(n):
    white = [255,255,255]
    blinkcolor = [255, 140,0]

    for x in range(0, n*2): #  herhaal 'n x 2' keer (x loopt van 0 tot 'n')
        # als x even is -> wit, anders groen
        # daarna korte 'pauze' (sleep)
        if x%2 == 0: # modulo operator ==> rest na deling
            drone.set_drone_LED(white[0], white[1], white[2],255)
        else:
            drone.set_drone_LED(blinkcolor[0], blinkcolor[1], blinkcolor[2], 255)
        time.sleep(1)

drone = Drone()
drone.pair()

blink(5)

drone.set_drone_LED(255,0,0,255)
drone.drone_buzzer(Note.C4, 200)
drone.set_drone_LED(255,0,255,255)
drone.drone_buzzer(Note.E4, 200)
drone.set_drone_LED(255,255,0,255)
drone.drone_buzzer(Note.G4, 200)
drone.set_drone_LED(0,255,0,255)
drone.drone_buzzer(Note.C5, 200)
drone.set_drone_LED(0,255,255,255)

drone.takeoff()
drone.hover(3)

drone.set_throttle(10)
drone.move(1)

drone.land()

drone.drone_buzzer(Note.C5, 200)
drone.drone_buzzer(Note.G4, 200)
drone.drone_buzzer(Note.E4, 200)
drone.drone_buzzer(Note.C4, 200)

drone.close()