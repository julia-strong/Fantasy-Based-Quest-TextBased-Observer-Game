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
from graphics import openDoor
from graphics import draw_openDoor
from graphics import roomWithMouse
from graphics import draw_roomWithMouse
from graphics import bat
from graphics import draw_bat
from graphics import holeInWall
from graphics import draw_holeInWall
from graphics import seeDragon
from graphics import draw_seeDragon
from graphics import dragonFace
from graphics import draw_dragonFace
from graphics import noMouse
from graphics import draw_noMouse
from graphics import openBox
from graphics import draw_openBox
from graphics import caveExit
from graphics import draw_caveExit
from graphics import secondCrab
from graphics import draw_secondCrab
from Player import hitPoints
from Player import level
from Monster import loot
from Monster import crabLoot
from Monster import Monster
from Monster import Player
from Monster import birdLoot
from Monster import batLoot
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
openedDoor = False
sawMouse = False
discoveredBat = False
batEncounterEnded = False
batLeft = False
drankPotion = False
sawDragon = False
vulnerable = False
immune = False
resistant = False
fendOffDragon = False
mouseGone = False
openedBox = False
leavingCave = False
secCrab = False
returnBoat = False
returnPath = False
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
          print("click in the top left corner of the screen to continue")
      elif gamestart and not continueAdventure and isClicked(100,225,100,225) and not windowClicked and not continueFromCrab:
        print("Click on the path to continue")
        draw_Pathstart(pathstart,2,2,0)
        continueAdventure = True
        pathdrawn = True
        windowClicked = True
      elif inventory and not continueAdventure and isClicked(0,100,0,100) and not continueFromCrab and not secCrab:
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
      elif secPath and isClicked(0,230,125,235) and secpathDrawn and not continueOntoBoat and not foundCave and not enteredCave and not returnPath:
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
            clickedOnFirstCreature = False
            firstCreature = True
            randEncount = 4
          else:
            print("wrong! :( \n you answered: \n" + input1 + "\n the correct answer was a) chicken \n")
            Player.hitPoints -= 5
            print("the chicken bit you \n -5 health \n your current health is now: \n" , Player.hitPoints)
            print("click on the chicken's eyes to continue")
          clickedOnFirstCreature = False
          firstCreature = True
          randEncount = 4
          if not clickedOnFirstCreature and firstCreature and isClicked(0,200,0,240) and not secCrab:
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
      if continueAfterFirstEncount and isClicked(375,500,0,225) and randEncount == 4 and not continueOntoBoat and not sawDragon:
        draw_noFirstEncount(noFirstEncount,2,2,0)
        print("you continue on the journey")
        print("click on the sun in the upper right corner to continue")
        continueContinuing = True
      if continueContinuing and isClicked (375,500,0,225) and not continueOntoBoat and not arrivedOnIsland and not sawDragon:
          draw_beachPath(beachPath,2,2,0)
          print("click on the crab to continue")
          beachDrawn = True
    if continueContinuing and beachDrawn and not crabClicked and isClicked(0,100,370,460) and not continueOntoBoat:
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
    if sawBird and isClicked(10,150,10,150) and not enteredCave and pathdrawn:
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
    if birdFlewAway and isClicked(260,400,100,300) and not arrivedOnIsland and not batLeft and not drankPotion and not returnBoat:
      draw_findPotion(findPotion,2,2,0)
      input5 = input("you find a mysterious vile with a green liquid do you want to consume it? (y/n) \n")
      if input5.lower() == "n":
        draw_healthBoost(healthBoost,2,2,0)
        input6 = input("a wave crashes against the boat and the bottle topples over the edge of the boat falling into the sea \n you see a small label on the bottle reading 'health increasing potion' would you like to try to grab the bottle? (y/n) \n")
        if input6.lower() == "n":
          print("you watch as the bottle sinks slowly into the water")
          print("click on the bottom right corner of the screen to continue")
          potionSeen = True
        elif input6.lower() == "y":
          Player.hitPoints -= 1
          print("you manage to grab the bottle just before it gets fully submurged by the water \n although a piranha bites your finger \n your health decreases \n your current health is now: \n", Player.hitPoints)
          input5 = "y" 
          piranha = True
      elif input5.lower() == "y" or piranha:
        allergicToPotion = random.randint(1,100)
        input5 = "y"
        # print(allergicToPotion)
        if allergicToPotion != 50:
          potionSeen = True
          print("you drink the bottle and notice its effects working, as you flip the bottle over you see a lable stating 'health increasing potion' ")
          drankPotion = True
          Player.hitPoints += 5
          print("your current health is now", Player.hitPoints)
          print("click on the bottom right corner of the screen to continue")
          time.sleep(1)
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
    elif arrivedOnIsland and isClicked(375,500,100,250) and not enteredCave and not batLeft:
      draw_caveEntrance(caveEntrance,2,2,0)
      print("you continue along your journey when you come across a cave you remember hearing that this cave may contain a monster that no other adventurer has been able to defeat, click on the stone closest to the cave to proceed")
      foundCave = True
    if foundCave and isClicked(220,360,290,350) and not enteredCave and not mouseGone:
      draw_startTunnel(startTunnel,2,2,0)
      print("you make your way into the cave and down a set of stairs \n click on the creature at the end of the tunnel to continue")
      enteredCave = True
    elif enteredCave and isClicked(290,350,100,150) and not batLeft and not mouseGone:
      draw_door(door,2,2,0)
      print("you continue along the path, moving deeper and deeper into the cave until you come across a door, click on the doorknob to open the door")
      sawDoor = True
    if sawDoor and isClicked(285,340,260,340) and not openedDoor and not batLeft:
      draw_openDoor(openDoor,2,2,0)
      print("you open the door and see a box, click on it to investigate further")
      openedDoor = True
    if openedDoor and isClicked(200,325,300,420) and not mouseGone:
      draw_roomWithMouse(roomWithMouse,2,2,0)
      print("you enter the room and see a mouse scurrying along the floor, click on the mouse to continue")
      sawMouse = True
    if sawMouse and isClicked(100,200,375,450) and not mouseGone:
      draw_bat(bat,2,2,0)
      discoveredBat = True
      print("you examine the mouse closer only to realize that it's actually a bat")
      print("the bat is angered that it was assumed to be a mouse, it tries to engage in battle with you")
      Monster.attack(Player)
      fendOffBat = random.randint(1,3)
      if fendOffBat == 2:
        print("you manage to fend off the bat sucessfully \n the bat left behind something: \n", batLoot)
        inventoryContents.append(loot)
        print("your inventory now contains: \n" , inventoryContents)
        batEncounterEnded = True
        print("click in the bottom right corner of the screen to continue")
        time.sleep(1)
      elif fendOffBat != 2:
        print("you try to fend off the bat but it manages to attack you")
        Monster.attack(Player)
        fendOffBatAgain = random.randint(1,10)
        time.sleep(1)
        if fendOffBatAgain == 7:
          print("you try to fend off the bat once again but it still manages to attack you")
          Monster.attack(Player)
          batEncounterEnded = True
          print("click in the bottom right corner of the screen to continue")
          time.sleep(1)
        elif fendOffBatAgain != 7:
          print("you manage to fend off the bat sucessfully \n the bat left behind something: \n", batLoot)
          inventoryContents.append(loot)
          print("your inventory now contains: \n" , inventoryContents)
          batEncounterEnded = True
          print("click in the bottom right corner of the screen to continue")
          time.sleep(1)
    if batEncounterEnded and isClicked(400,500,400,500) and not fendOffDragon:
      draw_holeInWall(holeInWall,2,2,0)
      batLeft = True
      print("the bat flies away and you notice a small and mysterious hole in the wall, click on the hole in the wall to continue")    
    if batLeft and isClicked(250,310,90,200):
      draw_seeDragon(seeDragon,2,2,0)
      print("you look into the hole in the wall and find a small dragon, click on the upper right corner of the screen to investiate")
      sawDragon = True
    if sawDragon and isClicked(400,500,0,100):
      draw_dragonFace(dragonFace,2,2,0)
      print("the dragon approaches you, and it attacks you with fire-breath")
      dragonResult = random.randint(1,100)
      if dragonResult == 30:
        print("the dragon attacked you, but the damage is twice than what you expected, and you remember that you are vulnerable to dragon attacks and take twice the damage")
        Monster.attack(Player)
        Monster.attack(Player)
        vulnerable = True
        print("this lowers your health, your current health is now: \n", Player.hitPoints)
      elif dragonResult == 10:
        print("the dragon attacked you, but you don't feel any damage, and realize that you're immune to this dragon's attack")
        immune = True
      elif 40 < dragonResult > 50:
        print("the dragon attacks you, but it doesn't do quite as much damage as you expected, and you realize that you're slightly resistant to the dragon's attack")
        resistant = True
        Player.hitPoints += 1 
        Monster.attack(Player)
      else:
        Monster.attack(Player)
      print("you realize that you can offer a sacrifice from your inventory to the dragon if you don't want to engage in battle with it")
      input7 = input("type 's' to sacrifice an item from your inventory, or type 'b' to engage in battle with the dragon instead \n")
      if input7.lower() == "s":
        sacrifice = random.randint(1,len(inventoryContents))
        del inventoryContents[sacrifice-1]
        print("you sacrificed an item from your inventory, your inventory now contains: \n", inventoryContents)
        fendOffDragon = True
        print("click on the bottom left corner of the screen to continue")
      elif input7.lower() == "b":
        print("you engage in battle with the dragon")
        if vulnerable:
          Monster.attack(Player)
          Monster.attack(Player)
        elif immune:
          print("the dragon tries to attack you but doesn't do any damage again")
        elif resistant:
          print("the dragon tries to attack you but doesn't do quite as much damage again")
          Player.hitPoints += 1
          Monster.attack(Player)
        else:
          Monster.attack(Player)
        fendOffDragonFirst = random.randint(1,7)
        if fendOffDragonFirst == 6:
          print("you manage to sucessfully fend off the dragon, however you find that it didn't leave behind any treasure, although the cave is rumored to be filled with the dragon's treasure")
          fendOffDragon = True
          print("click on the bottom left corner of the screen to continue")
        else:
          Monster.attack(Player)
          fendOffDragonSecond = random.randint(1,3)
          if fendOffDragonSecond == 2:
            print("you sucessfully manage to fend off the dragon after being attacked again, but it didn't seem to leave behind any loot, which you find odd considering the cave is rumored to be filled with the dragon's treasure")
            fendOffDragon = True
            print("click on the bottom left corner of the screen to continue")
          elif fendOffDragonSecond != 2:
            Player.hitPoints += 2
            print("you have enough time to somewhat recover before the dragon attacks you again")
            Monster.attack(Player)
            print("you are able to not lose as much health this time, and since you were more prepared for the attack, you manage to finally fend off the dragon")
            fendOffDragon = True
            print("click on the bottom left corner of the screen to continue")
    if fendOffDragon and isClicked(0,100,400,500) and not leavingCave:
      draw_noMouse(noMouse,2,2,0)
      print("you return back to the room where you saw the mouse, where you discover that it has left, click on the treasure chest to continue")
      mouseGone = True
    elif mouseGone and isClicked(200,450,300,450) and not openedBox and not leavingCave:
      draw_openBox(openBox,2,2,0)
      input8 = input("you open the box and find it to be filled with a wide variety of objects, which of the following objects is not in the box? \n a) feather and quill \n b) 4 gold pieces/coins \n c) a bat tooth \n d) an apple core \n e) a snail \n f) a diamond \n g) a pocketwatch \n")
      if input8.lower() != "c":
        print("wrong! you answered", input8, "the correct answer was c) a bat tooth ")
        openedBox = True
        print("click on the snail to continue")
      if input8.lower() == "c":
        print("correct! \n you grab the four gold pieces and add them to your inventory")
        inventoryContents.append("4 gold pieces")
        print("your inventory now contains: \n", inventoryContents)
        openedBox = True
        print("click on the snail to continue")
    if openedBox and isClicked(350,475,275,400) and not secCrab:
      draw_caveExit(caveExit,2,2,0)
      print("you make your way to the exit of the cave, click on the tree on the left side to continue")
      leavingCave = True
    if leavingCave and isClicked(0,150,240,390):
      draw_secondCrab(secondCrab,2,2,0)
      print("you continue along your journey when you come across another crab, you can either click on it and see what happens, or click on the sun to continue your journey")
      secCrab = True
    if secCrab and isClicked(425,500,300,400):
      draw_image1(startImage,2,2,0)
      print("you realize that the crab somehow teleported you back home, \n you won the game!")
      print("your current health is \n", hitPoints)
      print("you have ended the game with these items in your inventory \n", inventoryContents)
      print("the end!")
      time.sleep(5)
      exit()
    elif secCrab and isClicked(0,150,0,150):
      draw_boat(boat, 2,2,0)
      print("you get on the boat that you took to get to the island, and continue sailing smoothly, without running into any issues, and you do end up seeing the bird again, however it does not approach")
      print("click on the flag of the boat to continue")
      returnBoat = True
    if returnBoat and isClicked(260,400,100,300) and not returnPath:
      returnPath = True
      draw_secondPath(secondPath,2,2,0)
      print("you continue along your return trip when you come across the path where you heard the growling noise earlier, click on where the path turns the corner to continue returning home")
    if returnPath and isClicked(0,230,125,235):
      draw_image1(startImage,2,2,0)
      print("you have made it home!")
      print("your current health is \n", hitPoints)
      print("you have ended the game with these items in your inventory \n", inventoryContents)
      print("the end!")
      time.sleep(5)
      exit()
    if Player.hitPoints <= 0:
      print("You have run out of hit points! :( \n Game over!!!")
      time.sleep(1)
      exit()
          
      
