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
from graphics import draw_CrabEncount
from graphics import crabEncount
from graphics import scaled_boatPath
from graphics impoq boatPath
from Player import hitPoints
from Player import level
from Monster import loot
from Monster import crabLoot
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
crabClicked = False
beachDrawn = False
clearedInvent = False
continueFromCrab = False

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
      elif gamestart and isClicked(340,450,350,450) and not continueFromCrab:
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
         print("click in the upper left portion of the screen above the crystal ball to continue")
      elif gamestart and isClicked(225,400,225,350) and crystalBallClicked:
         print("Click on the path to continue")
         draw_Pathstart(pathstart,2,2,0)
         continueAdventure = True
         pathdrawn = True

      if continueAdventure and isClicked(200,300,250,500) and not secPath and pathdrawn:
        inventory = True
        draw_secondPath(secondPath,2,2,0)
        randEncount = random.randint(1,3)
        print("you continue on your journey along the path when you reach a turn in the path and here growling around the corner \n click where the path turns the corner to continue")
        secPath = True
        secpathDrawn = True
      elif secPath and isClicked(0,240,125,245) and secpathDrawn:
        randEncount = random.randint(1,3)
        print(randEncount)
        draw_secondPath(secondPath,2,2,0)
        if randEncount == 2:
          print("you come across your first encounter! The townsperson that you may have spoken to earlier in the journey mentioned that you will encounter these sorts of creatures.")
          draw_firstEncount(firstEncount,2,2,0)
          input1 = input("correctly name the creature to repel it \n a) chicken b) rat c)shark d)other \n")
          if input1.lower() == "a":
            print("correct!")
            level += 1
            print("level up! \n your new level is \n" , level)
            inventoryContents.clear()
            clearedInvent = True
            inventoryContents.append(loot)
            print("you collected things from the chicken \n your inventory now contains:\n")
            print(loot)
            #print("correct \n click on the chicken's eyes to continue")
          else:
            print("wrong! :( \n you answered: \n" + input1 + "\n the correct answer was a) chicken \n")
            hitPoints -= 5
            print("the chicken bit you \n -5 health \n your current health is now \n" , hitPoints)
            print("click on the chicken's eyes to continue")
          clickedOnFirstCreature = False
          firstCreature = True
          randEncount = 4
          if not clickedOnFirstCreature and firstCreature and isClicked(0,200,0,240):
            continueAfterFirstEncount = True
            draw_noFirstEncount(noFirstEncount,2,2,0)
            print("click the sun in the top right portion of the screen to continue")
            randEncount = 4
        elif randEncount == 1 or randEncount == 3:
          print("as you turn the corner the growling quiets down and you continue along")
          draw_noFirstEncount(noFirstEncount,2,2,0)
          print("click on the sun in the upper right corner to continue")
          continueAfterFirstEncount = True
          randEncount = 4
      if continueAfterFirstEncount and isClicked(375,500,0,225) and randEncount == 4:
        draw_noFirstEncount(noFirstEncount,2,2,0)
        print("you continue on the journey")
        print("click on the sun in the upper right corner to continue")
        continueContinuing = True
      if continueContinuing and isClicked (375,500,0,225):
          draw_beachPath(beachPath,2,2,0)
          print("click on the crab to continue")
          beachDrawn = True
    if continueContinuing and beachDrawn and not crabClicked and isClicked(0,100,370,460):
      #  print("test")
      draw_CrabEncount(crabEncount,2,2,0)
      input2 = input("You have come across a crab! This encounter is optional, you have a chance of being attacked by the crab, but might be able to get loot from the crab if you take the risk. Will you take the risk? (y/n) \n")
      if input2.lower() =="n":
        print("okay!")
      if input2.lower() == "y":
        hitPoints -= 5
        if hitPoints <= 0:
          print("You have run out of hit points! :( \n Game over!!!")      
        print("The crab pinches you! \n -5 health \n your current health is now: \n" , hitPoints )
        print("However you still get loot! Your inventory now contains: \n")
        if not clearedInvent:
          inventoryContents.clear()
          clearedInvent = True
        else:
          pass
        inventoryContents.append(crabLoot)
        print (inventoryContents)
      if input2.lower() != "n" and input2.lower() != "y":
        input2 = input("Invalid input! \n Try again. (y/n) \n")
        print(input2)
      continueFromCrab = True
      print("click in the bottom right corner of the screen to continue")
    if continueFromCrab and isClicked(400,500,400,500):
      draw_boatPath(boatPath,2,2,0)
if hitPoints <= 0:
  print("You have run out of hit points! :( \n Game over!!!")      
      