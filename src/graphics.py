import pygame

pygame.init()
display_width = 500
display_height = 500
display_time = 5000
x = 1
y = 1
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pathstart = pygame.image.load("pathstart.png").convert()
startImage = pygame.image.load("startImage.png").convert()
testImage = pygame.image.load("testImage.png").convert()
firstChoice = pygame.image.load("firstChoice.png").convert()
backpackImage = pygame.image.load("backpack.png").convert()
bookImage = pygame.image.load("Book.png").convert()
crystalBallImage = pygame.image.load("crystalball.png").convert()
secondPath = pygame.image.load("secondPath.png").convert()
noFirstEncount = pygame.image.load("noFirstEncount.png").convert()
firstEncount = pygame.image.load("firstEncount.png").convert()
beachPath = pygame.image.load("beachpath.png").convert()
crabEncount = pygame.image.load("CrabEncounter.png").convert()
boatPath = pygame.image.load("boatPath.png").convert()
boat = pygame.image.load("boat.png").convert()
birdEncount = pygame.image.load("birdEncount.png").convert()
findPotion = pygame.image.load("findPotion.png").convert()
healthBoost = pygame.image.load("healthBoost.png").convert()
pygame.display.set_caption("RPsG Fantasy Game with Text-Based, Graphic, and Clicker Elements")
surface1 = pygame.Surface((display_width, display_height))
def draw_image(image, x, y):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_image = pygame.transform.scale(
      image, (startImage.get_width() // 1, startImage.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_image, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= 100000:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
def draw_image1(startImage, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_startImage = pygame.transform.scale(
      startImage, (startImage.get_width() // 1, startImage.get_height() // 1))
  while running:
    screen.blit(scaled_startImage, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
def draw_image2(bookImage, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_bookImage = pygame.transform.scale(
      bookImage, (bookImage.get_width() // 1, bookImage.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_bookImage, (x, y))
    pygame.display.flip()
    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
def draw_image3(firstChoice, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_firstChoice = pygame.transform.scale(
      firstChoice, (firstChoice.get_width() // 1, firstChoice.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_firstChoice, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw_backpack(backpackImage, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_backpack = pygame.transform.scale(
      backpackImage, (backpackImage.get_width() // 1, backpackImage.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_backpack, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False


def draw_Pathstart(pathstart, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_pathstart = pygame.transform.scale(
      pathstart, (pathstart.get_width() // 1, pathstart.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_pathstart, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False


def draw_crystalBall(crystalBallImage, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_crystalBallImage = pygame.transform.scale(
      crystalBallImage, (crystalBallImage.get_width() // 1, crystalBallImage.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_crystalBallImage, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False


def draw_secondPath(secondPath, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_secondPath = pygame.transform.scale(
      secondPath, (secondPath.get_width() // 1, secondPath.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_secondPath, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw_noFirstEncount(noFirstEncount, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_noFirstEncount = pygame.transform.scale(
      noFirstEncount, (noFirstEncount.get_width() // 1, noFirstEncount.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_noFirstEncount, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False


def draw_firstEncount(firstEncount, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_firstEncount = pygame.transform.scale(
      firstEncount, (firstEncount.get_width() // 1, firstEncount.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_firstEncount, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw_beachPath(beachPath, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_beachPath = pygame.transform.scale(
      beachPath, (beachPath.get_width() // 1, beachPath.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_beachPath, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw_CrabEncount(crabEncount, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_CrabEncount = pygame.transform.scale(
      crabEncount, (crabEncount.get_width() // 1, crabEncount.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_CrabEncount, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw_boatPath(boatPath, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_boatPath = pygame.transform.scale(
      boatPath, (boatPath.get_width() // 1, boatPath.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_boatPath, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw_boat(boat, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_boat = pygame.transform.scale(
      boat, (boat.get_width() // 1, boat.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_boat, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw_birdEncount(birdEncount, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_birdEncount = pygame.transform.scale(
      birdEncount, (birdEncount.get_width() // 1, birdEncount.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_birdEncount, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw_findPotion(findPotion, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_findPotion = pygame.transform.scale(
      findPotion, (findPotion.get_width() // 1, findPotion.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_findPotion, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def draw_healthBoost(healthBoost, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_healthBoost = pygame.transform.scale(
      healthBoost, (healthBoost.get_width() // 1, healthBoost.get_height() // 1))
  while running:
    screen.fill(0)
    screen.blit(scaled_healthBoost, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False