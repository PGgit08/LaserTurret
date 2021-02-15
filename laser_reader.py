from serial import Serial
import pygame

pygame.init()

# arduino serializer
arduino = Serial('COM5', baudrate=115200, timeout=.01)
print(arduino.name)

# divisors
XDIV = 7
YDIV = 4

# or 180 * 7
SCREEN_WIDTH = 180 * 7
SCREEN_HEIGHT = 180 * 4

CANVAS_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

WHITE = (255, 255, 255)

# create screen
canvas = pygame.display.set_mode(CANVAS_SIZE)

# create lines on screen
pygame.draw.line(canvas, WHITE, (0, SCREEN_HEIGHT/2), (SCREEN_WIDTH, SCREEN_HEIGHT/2))
pygame.draw.line(canvas, WHITE, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

# angles
angles = [90, 90]

def send_angles(pos):
    # serial angles will be sent here
    yaw = str(pos[0]) + '\n'
    pitch = str(pos[1]) + '\n'

    yaw = yaw.encode()
    pitch = pitch.encode()

    # print('sending')
    if arduino.isOpen() == True:
        # print('port open')
        arduino.write(yaw)
        arduino.write(pitch)

clock = pygame.time.Clock()
while True:    
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            arduino.close()
            exit()
    
    if mouse_pos[0] % XDIV == 0:
        angles[0] = mouse_pos[0] // XDIV
    
    if mouse_pos[1] % YDIV == 0:
        angles[1] = mouse_pos[1] // YDIV

    send_angles(angles)

    clock.tick(60)
    pygame.display.flip()
