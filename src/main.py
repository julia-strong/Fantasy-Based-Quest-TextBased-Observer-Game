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
from graphics import draw_boatPath
from graphics import boatPath
from graphics import boat
from graphics import draw_boat
from graphics import birdEncount
from graphics import draw_birdEncount
from graphics import findPotion
from graphics import draw_findPotion
from graphics import healthBoost
from graphics import draw_healthBoost
from graphics import arriveOnShore
from graphics import draw_arriveOnShore
from graphics import caveEntrance
from graphics import draw_caveEntrance
from graphics import startTunnel
from graphics import draw_startTunnel
from graphics import door
from graphics import draw_door
from Player import hitPoints
from Player import level
from Monster import loot
from Monster import crabLoot
from Monster import Monster
from Monster import Player
from Monster import birdLoot
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
continueOntoBoat = False
sawBird = False
birdFlewAway = False
defeatBird = False
potionSeen = False
arrivedOnIsland = False
piranha = False
foundCave = False
enteredCave = False
sawDoor = False
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
      elif gamestart and isClicked(340,450,350,450) and not continueFromCrab and not potionSeen:
        print("\n" + "Click on the crystal ball to hear from a townsperson for additional information. Click on the backpack to see your inventory. Click on the window to continue on your journey.")
        draw_image3(firstChoice, 2, 2, 0)
        secondBook = True
      elif gamestart and not inventory and isClicked(325,425,200,350) and not arrivedOnIsland:
        draw_backpack(backpackImage,2,2,0)
        time.sleep(2)
        inventory = True
        if inventory:
          print(inventoryContents)
          print("click anywhere in the screen to continue")
      elif gamestart and not continueAdventure and isClicked(100,225,100,225) and not windowClicked and not continueFromCrab:
        print("Click on the path to continue")
        draw_Pathstart(pathstart,2,2,0)
        continueAdventure = True
        pathdrawn = True
        windowClicked = True
      elif inventory and not continueAdventure and isClicked(0,500,0,500) and not continueFromCrab:
        print("Click on the path to continue")
        draw_Pathstart(pathstart,2,2,0)
        pathdrawn = True
        continueAdventure = True

      elif gamestart and not continueAdventure and isClicked(200,300,350,450) and not crystalBallClicked and bookClicked and secondBook and not foundCave:
         print("clicked on crystal ball")
         print("[insert townsperson speech]")
         draw_crystalBall(crystalBallImage,2,2,0)
         crystalBallClicked = True
         print("click in the upper left portion of the screen above the crystal ball to continue")
      elif gamestart and isClicked(225,400,225,350) and crystalBallClicked and not continueFromCrab:
         print("Click on the path to continue")
         draw_Pathstart(pathstart,2,2,0)
         continueAdventure = True
         pathdrawn = True

      if continueAdventure and isClicked(200,300,250,500) and not secPath and pathdrawn and not foundCave and not enteredCave:
        inventory = True
        draw_secondPath(secondPath,2,2,0)
        randEncount = random.randint(1,3)
        print("you continue on your journey along the path when you reach a turn in the path and here growling around the corner \n click where the path turns the corner to continue")
        secPath = True
        secpathDrawn = True
      elif secPath and isClicked(0,230,125,235) and secpathDrawn and not continueOntoBoat and not foundCave and not enteredCave:
        randEncount = random.randint(1,3)
        # print(randEncount)
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
          else:
            print("wrong! :( \n you answered: \n" + input1 + "\n the correct answer was a) chicken \n")
            Player.hitPoints -= 5
            print("the chicken bit you \n -5 health \n your current health is now: \n" , Player.hitPoints)
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
      if continueAfterFirstEncount and isClicked(375,500,0,225) and randEncount == 4 and not continueOntoBoat:
        draw_noFirstEncount(noFirstEncount,2,2,0)
        print("you continue on the journey")
        print("click on the sun in the upper right corner to continue")
        continueContinuing = True
      if continueContinuing and isClicked (375,500,0,225) and not continueOntoBoat and not arrivedOnIsland:
          draw_beachPath(beachPath,2,2,0)
          print("click on the crab to continue")
          beachDrawn = True
    if continueContinuing and beachDrawn and not crabClicked and isClicked(0,100,370,460) and not continueOntoBoat:
      #  print("test")
      draw_CrabEncount(crabEncount,2,2,0)
      input2 = input("You have come across a crab! This encounter is optional, you have a chance of being attacked by the crab, but might be able to get loot from the crab if you take the risk. Will you take the risk? (y/n) \n")
      if input2.lower() =="n":
        print("okay!")
      if input2.lower() == "y":
        Player.hitPoints -= 5
        if Player.hitPoints <= 0:
          print("You have run out of hit points! :( \n Game over!!!")      
        print("The crab pinches you! \n -5 health \n your current health is now: \n" , Player.hitPoints )
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
    if continueFromCrab and isClicked(400,500,400,500) and not continueOntoBoat:
      draw_boatPath(boatPath,2,2,0)
      print("click on the boat to continue")
      continueOntoBoat = True
    elif continueOntoBoat and isClicked(300,475,175,350) and not birdFlewAway:
      draw_boat(boat,2,2,0)  
      print("you see a bird in the sky \n click on the bird to investigate")   
      sawBird = True
    if sawBird and isClicked(10,150,10,150) and not enteredCave:
      draw_birdEncount(birdEncount,2,2,0)
      print("the bird flies over and lands on your boat")
      input3 = input("there is a risk the bird might attack, would you like to continue (y/n) \n")
      if input3.lower() == "y":
        print("the bird got upset")
        Monster.attack(Player)
        input4 = input("would you like to engage in battle with this creature? (y/n) \n")
        if input4.lower() == "y":
          print("you have engaged in battle with the creature")
          sucessfulMosterAttack = random.randint(1,3)
          # print(sucessfulMosterAttack)
          if sucessfulMosterAttack == 1:
            Monster.attack(Player)
            secondMonsterAttack = random.randint(1,2)
            # print(secondMonsterAttack)
            if secondMonsterAttack == 2:
              Monster.attack(Player)
              secondMonsterAttack = 1
            elif secondMonsterAttack != 2:
              print("you manage to fend off the creature and collect loot")
              defeatBird = True
          elif sucessfulMosterAttack != 1:
            print("you manage to fend off the creature and collect loot")
            defeatBird = True
          if defeatBird:
            if not clearedInvent:
              inventoryContents.clear()
            inventoryContents.append(birdLoot)
            print("Your inventory now contains: \n")
            input3 = "n"
            print(inventoryContents)
        elif input4.lower() == "n":
          input3 = "n"
      if input3.lower() == "n":
        draw_boat(boat,2,2,0)
        print("the bird flies away \n click on the flag of the boat to continue")
        birdFlewAway = True
    if birdFlewAway and isClicked(260,400,100,300) and not arrivedOnIsland:
      draw_findPotion(findPotion,2,2,0)
      input5 = input("you find a mysterious vile with a green liquid do you want to consume it? (y/n) \n")
      if input5.lower() == "n":
        draw_healthBoost(healthBoost,2,2,0)
        input6 = input("a wave crashes against the boat and the bottle topples over the edge of the boat falling into the sea \n you see a small label on the bottle reading 'health increasing potion' would you like to try to grab the bottle? (y/n) \n")
        if input6.lower() == "n":
          print("you watch as the bottle sinks slowly into the water")
          print("click on the bottom right corner of the screen to continue")
          potionSeen = True
        if input6.lower() == "y":
          Player.hitPoints -= 1
          print("you manage to grab the bottle just before it gets fully submurged by the water \n although a piranha bites your finger \n your health decreases \n your current health is now: \n", Player.hitPoints)
          input5 = "y" 
          piranha = True
      if input5.lower() == "y" or piranha:
        allergicToPotion = random.randint(1,100)
        # print(allergicToPotion)
        if allergicToPotion != 50:
          potionSeen = True
          print("you drink the bottle and notice its effects working, as you flip the bottle over you see a lable stating 'health increasing potion' ")
          Player.hitPoints += 5
          print("your current health is now", Player.hitPoints)
          print("click on the bottom right corner of the screen to continue")
        elif allergicToPotion == 50:
          potionSeen = True
          print("as you drink the bottle you flip the bottle over you see a lable stating 'health increasing potion' ")
          print("you start to feel sick after drinking the bottle and realize that you are allergic to this potion")
          Player.hitPoints -= 5
          print("your health declines \n your current health is now: \n", Player.hitPoints)
          print("click on the bottom right corner of the screen to continue")
    if potionSeen and isClicked(400,500,400,500):
      draw_arriveOnShore(arriveOnShore,2,2,0)
      print("you arrive on the shore of a mysterious island, click on the tree on the right to continue on your journey")
      arrivedOnIsland = True
    elif arrivedOnIsland and isClicked(375,500,100,250) and not enteredCave:
      draw_caveEntrance(caveEntrance,2,2,0)
      print("you continue along your journey when you come across a cave you remember hearing that this cave may contain a monster that no other adventurer has been able to defeat, click on the stone closest to the cave to proceed")
      foundCave = True
    if foundCave and isClicked(220,360,290,350) and not enteredCave:
      draw_startTunnel(startTunnel,2,2,0)
      print("you make your way into the cave and down a set of stairs \n click on the creature at the end of the tunnel to continue")
      enteredCave = True
    elif enteredCave and isClicked(290,350,100,150):
      draw_door(door,2,2,0)
      print("you continue along the path, moving deeper and deeper into the cave until you come across a door, click on the doorknob to open the door")
      sawDoor = True
    if sawDoor and isClicked(285,340,260,340):
      print("test")
if Player.hitPoints <= 0:
  time.sleep(4)
  print("You have run out of hit points! :( \n Game over!!!")      
      
