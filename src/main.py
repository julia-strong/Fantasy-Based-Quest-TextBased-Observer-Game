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
from graphics import draw_backpack
from graphics import backpackImage
from graphics import pathstart
from graphics import draw_Pathstart
from graphics import draw_crystalBall
from graphics import crystalBallImage
import time
import pygame
from button import isClicked

inventoryContents = ["your inventory is currently empty"]
pygame.init()
mouseX = pygame.mouse.get_pos()[0]
mouseY = pygame.mouse.get_pos()[1]
display_width = 500
display_height = 500
display_time = 5000
gamestart = False
inventory = False
continueAdventure = False
windowClicked = False
crystalBallClicked = False
bookClicked = False
secondBook = False
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
        bookClicked = True
        gamestart = True
        print("\n"+ "temporary intro paragraph for information")
        print("\n" + " click on the bottom right corner of the book to continue")
      elif gamestart and isClicked(340,450,350,490):
        print("\n" + "Click on the crystal ball to hear from a townsperson for additional information. Click on the backpack to see your inventory. Click on the window to continue on your journey.")
        draw_image3(firstChoice, 2, 2, 0)
        secondBook = True
      if gamestart and not inventory and isClicked(325,425,200,400):
        draw_backpack(backpackImage,2,2,0)
        time.sleep(4)
        inventory = True
        if inventory:
          print(inventoryContents)
          print("click anywhere in the screen to continue")
      elif gamestart and not continueAdventure and isClicked(100,225,100,225) and not windowClicked:
        print("you have begun your adventure")
        draw_Pathstart(pathstart,2,2,0)
        continueAdventure = True
        windowClicked = True
      elif inventory and not continueAdventure and isClicked(0,500,0,500):
        print("you have begun your adventure")
        draw_Pathstart(pathstart,2,2,0)
        continueAdventure = True

      elif gamestart and not continueAdventure and isClicked(300,350,350,450) and not crystalBallClicked and bookClicked and secondBook:
         print("clicked on crystal ball")
         print("[insert townsperson speech]")
         draw_crystalBall(crystalBallImage,2,2,0)
         crystalBallClicked = True
