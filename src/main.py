#Julia Strong
#To Do
#implement player/user, npc, and monster stats
# implement observation where there's location and user has to find something specific such as traps - likely would take intelligence and/or wisdom into consideration
# final goal
# win/lose scenarios
#locations
#quests
from graphics import startImage
from graphics import draw_image1
import time
import pygame

pygame.init()

display_width = 500
display_height = 500
display_time = 5000

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(
    "RPG Fantasy Game with Text-Based, Graphic, and Clicker Elements")

draw_image1(startImage, 1, 1, display_time)

print(
    "Welcome to the RPG Fantasy Game with Text Based, Clicker Game, and Graphics Aspects!"
)
print("Click on the book to begin the adventure!")
time.sleep(4)
running = True
start_time = pygame.time.get_ticks()

while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 200 < mouse_x < 400 and 400 < mouse_y < 495:
                print("Clicked inside the specified area.")

    pygame.display.flip()

#pygame.quit()