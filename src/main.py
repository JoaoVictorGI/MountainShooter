import pygame
from pygame.surface import Surface

print("Game started")
pygame.init()

window: Surface = pygame.display.set_mode(size=(640, 480))

print("Start loop")
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close the window
            quit()  # End pygame "process"
