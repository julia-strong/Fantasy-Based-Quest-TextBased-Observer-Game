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
from graphics import secondPath
from graphics import noFirstEncount
from graphics import draw_noFirstEncount
from graphics import draw_secondPath
from graphics import draw_firstEncount
from graphics import firstEncount
from graphics import draw_beachPath
from graphics import beachPath
import time
import pygame
import random
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
continueContinuing = False
continueAfterFirstEncount = False
windowClicked = False
crystalBallClicked = False
bookClicked = False
secondBook = False
secPath = False
secpathDrawn  = False
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
        print("\n Important Note! \n Try to avoid clicking multiple times on the same thing, unless it is stated otherwise, since it could potentially result in skipping a screen and/or missing important information!")
        print("\n" + " click on the bottom right corner of the book to continue")
      elif gamestart and isClicked(340,450,350,490):
        print("\n" + "Click on the crystal ball to hear from a townsperson for additional information. Click on the backpack to see your inventory. Click on the window to continue on your journey.")
        draw_image3(firstChoice, 2, 2, 0)
        secondBook = True
      elif gamestart and not inventory and isClicked(325,425,200,350):
        draw_backpack(backpackImage,2,2,0)
        time.sleep(4)
        inventory = True
        if inventory:
          print(inventoryContents)
          print("click anywhere in the screen to continue")
      elif gamestart and not continueAdventure and isClicked(100,225,100,225) and not windowClicked:
        print("Click on the path to continue")
        draw_Pathstart(pathstart,2,2,0)
        continueAdventure = True
        pathdrawn = True
        windowClicked = True
      elif inventory and not continueAdventure and isClicked(0,500,0,500):
        print("Click on the path to continue")
        draw_Pathstart(pathstart,2,2,0)
        pathdrawn = True
        continueAdventure = True

      elif gamestart and not continueAdventure and isClicked(200,300,350,450) and not crystalBallClicked and bookClicked and secondBook:
         print("clicked on crystal ball")
         print("[insert townsperson speech]")
         draw_crystalBall(crystalBallImage,2,2,0)
         crystalBallClicked = True
         print("click anywhere in the screen to continue")
      elif gamestart and isClicked(0,500,0,500) and crystalBallClicked:
         print("Click on the path to continue")
         draw_Pathstart(pathstart,2,2,0)
         continueAdventure = True
         pathdrawn = True

      if continueAdventure and isClicked(200,300,250,500) and not secPath and pathdrawn:
        inventory = True
        draw_secondPath(secondPath,2,2,0)
        randEncount = random.randint(1,3)
        print("you continue on your journey along the path when you reach a turn in the path and here growling around the corner \n click anywhere in the screen to continue")
        secPath = True
        secpathDrawn = True
      elif secPath and isClicked(0,500,0,500) and secpathDrawn:
        randEncount = random.randint(1,3)
        print(randEncount)
        draw_secondPath(secondPath,2,2,0)
        if randEncount == 2:
          print("you come across your first encounter! The townsperson that you may have spoken to earlier in the journey mentioned that you will encounter these sorts of creatures.")
          draw_firstEncount(firstEncount,2,2,0)
          input1 = input("correctly name the creature to repel it \n a) chicken b) rat c)shark d)other \n")
          if input1.lower() == "a":
            print("correct \n click  anywhere on the scren to continue")
          else:
            print("try again" + input1)
          clickedOnFirstCreature = False
          firstCreature = True
          if not clickedOnFirstCreature and firstCreature and isClicked(0,500,0,500):
            continueAfterFirstEncount = True
        elif randEncount != 2:
          print("as you turn the corner the growling quiets down and you continue along")
          print("click anywhere in the screen to continue")
          continueAfterFirstEncount = True
        if continueAfterFirstEncount and isClicked(0,500,0,500):
          draw_noFirstEncount(noFirstEncount,2,2,0)
          print("you continue on the journey")
          print("click anywhere in the screen to continue")
          continueContinuing = True
      if continueContinuing and isClicked (0,500,0,500):
          draw_beachPath(beachPath,2,2,0)
          print("click on the crab to continue")
        
      