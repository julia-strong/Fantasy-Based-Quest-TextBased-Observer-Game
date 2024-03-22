import pygame
import pygame

pygame.init()
display_width = 500
display_height = 500
display_time = 5000
x = 1
y = 1
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
startImage = pygame.image.load("startImage.png").convert()
testImage = pygame.image.load("testImage.png").convert()
firstChoice = pygame.image.load("firstChoice.png").convert()
pygame.display.set_caption("RPG Fantasy Game with Text-Based, Graphic, and Clicker Elements")
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

bookImage =pygame.image.load("Book.png").convert()
def draw_image2(bookImage, x, y, display_time):
  running = True
  display_width = 500
  display_height = 500
  screen = pygame.display.set_mode((display_width, display_height))
  start_time = pygame.time.get_ticks()
  scaled_bookImage = pygame.transform.scale(
      bookImage, (bookImage.get_width() // 1, bookImage.get_height() // 1))
  while running:
    screen.blit(scaled_bookImage, (x, y))
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= display_time:
      #screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def something_was_clicked(x1, y1, x2, y2, image):
  running = True
  clicked = False
  while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          elif event.type == pygame.MOUSEBUTTONDOWN:
              mouse_x, mouse_y = pygame.mouse.get_pos()
              #print("Mouse position:", mouse_x, mouse_y)  
              if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:
                  screen.fill(0)
                  draw_image(image, 1, 1)
                  clicked = True
                  print("Clicked within the specified area")  
                  break  
      if clicked:
          break 
  return clicked