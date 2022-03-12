import pygame
import pyfirmata # Firmata is a standard Arduino Serial communication protocol

# arduino firmata setup
arduino = pyfirmata.Arduino('COM5')

# set up yaw and pitch servo pins
Yaw = arduino.get_pin('d:3:s')
Pitch = arduino.get_pin('d:4:s')

# angles
yaw = 0
pitch = 0

# angles for updating
angles = [yaw, pitch]
oldAngles = angles

# divisors
XDIV = 7
YDIV = 4

# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CANVAS_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

WHITE = (255, 255, 255)

# create screen
canvas = pygame.display.set_mode(CANVAS_SIZE)

# screen caption
pygame.display.set_caption("Laser Turret")

# create lines on screen
pygame.draw.line(canvas, WHITE, (0, SCREEN_HEIGHT / 2), (SCREEN_WIDTH, SCREEN_HEIGHT / 2))
pygame.draw.line(canvas, WHITE, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

# Pygame Loop
clock = pygame.time.Clock()
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # get mouse positions
    (mouseX, mouseY) = pygame.mouse.get_pos()

    # possible tuning
    # mouseX -= 20

    # servo angles (coords -> angles)
    yaw = int(mouseX * (182 / SCREEN_WIDTH))
    pitch = int(mouseY * (182 / SCREEN_HEIGHT))

    # update angles
    angles = [yaw, pitch]

    # serial send if updated angles
    if angles != oldAngles: 
        oldAngles = angles

        # serial send (angles -> PWM thingy)
        Yaw.write(yaw * (255 / 182))
        Pitch.write(pitch * (255 / 182))

        print(yaw, pitch)


    # pygame update
    clock.tick(60)
    pygame.display.flip()
