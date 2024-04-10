#Julia Strong
#To Do
#write intro paragraph for line 43
#implement player/user, npc, and monster stats
# implement observation where there's location and user has to find something specific such as traps - likely would take intelligence and/or wisdom into consideration
# final goal
# win/lose scenarios
#locations
#quests
from graphics import draw_image2
from graphics import draw_image3
from graphics import startImage
from graphics import draw_image1
from graphics import bookImage
from graphics import firstChoice
import time
import pygame
from button import isClicked


pygame.init()
mouseX = pygame.mouse.get_pos()[0]
mouseY = pygame.mouse.get_pos()[1]
display_width = 500
display_height = 500
display_time = 5000
gamestart = False
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(
    "RPG Fantasy Game with Text-Based, Graphic, and Clicker Elements")

draw_image1(startImage, 1, 1, display_time)
pygame.display.flip()
print(
    "Welcome to the RPG Fantasy Based Game with Text Based, Clicker Game, and Graphics Aspects!"
)
print("\n" + "Click on the book to begin!")
print("")


running = True
start_time = pygame.time.get_ticks()
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type != pygame.QUIT:
      if not gamestart and isClicked(150, 350, 395, 460):
        draw_image2(bookImage, 2,2, 0)
        gamestart = True
        print("\n"+ "temporary intro paragraph for information")
        print("\n" + " click on the bottom right corner of the book to continue (still working on making that work as of now)")
        # time.sleep(2)
        # pygame.event.clear()
        # if gamestart and isClicked(340, 450, 350, 490):
      # elif gamestart and pygame.mouse.get_pressed()[0] and 340 <= mouseX <= 450 and 350 <= mouseY <= 490:
      elif gamestart and isClicked(340,450,350,490):
          # pygame.event.get()
          # if event.type == pygame.MOUSEBUTTONUP:
        print("\n" + "clicked on corner")
        print("\n" + "Click on the crystal ball to hear from a townsperson for additional information. Click on the backpack to see your inventory. Click on the window to continue on your journey.")
        draw_image3(firstChoice, 2, 2, 0)
        # else:
        #   pygame.event.wait()

