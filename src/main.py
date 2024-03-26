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
from graphics import testPolygon
from Player import name
import time
import pygame
from button import isClicked


display_width = 500
display_height = 500
display_time = 5000
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(
    "RPG Fantasy Game with Text-Based, Graphic, and Clicker Elements")

draw_image1(startImage, 1, 1, display_time)
pygame.display.flip()
print(
    "Welcome to the RPG Fantasy Based Game with Text Based, Clicker Game, and Graphics Aspects!"
)
# name = input("What is your character's name?" + "\n")
# print(name)
# print("Welcome," + "\n" + name + "!" )
print("\n" + "Click on the book to begin!")
print("")
testPolygon()

running = True
start_time = pygame.time.get_ticks()
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif isClicked(200, 350, 375, 450):
        draw_image2(bookImage, 2,2, 0)
        print("\n"+ "temporary intro paragraph for information")
        print("\n" + "click on the bottom right corner of the book to continue")
        if isClicked(340, 450, 350, 490):
          print("\n" + "clicked on corner")
          draw_image3(firstChoice, 2, 2, 0)
          print("\n" + 
              "Click on the crystal ball to hear from a townsperson for additional information. Click on the backpack to see your inventory. Click on the window to continue on your journey."
          )

