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
draw_image1(startImage, 1, 1, 0)
#print("Hello World")
print("Welcome to the RPG Fantasy Game with Text Based, Clicker Game, and Graphics Aspects!")
print("Click on the book to begin the adventure!")
input("testInput")
mouse_x, mouse_y = pygame.mouse.get_pos()
for event in pygame.event.get():
  if event.type == pygame.MOUSEBUTTONDOWN:
      if mouse_x > 200 and mouse_y > 400 and mouse_x < 400 and mouse_y < 495:
        print("test")



  
pygame.quit()