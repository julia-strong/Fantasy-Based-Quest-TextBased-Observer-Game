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
pygame.display.set_caption("RPG Fantasy Game with Text-Based, Graphic, and Clicker Elements")
surface1 = pygame.Surface((display_width, display_height))


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
      screen.fill(0)
      running = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    