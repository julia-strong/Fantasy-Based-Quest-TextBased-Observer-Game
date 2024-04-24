import pygame
def __init__(self, x, y, width, height):
      self.self = self
      self.x = 0
      self.y = 0
      self.width = 0
      self.height = 0


def isClicked(X1, X2, Y1, Y2):
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    if mouseX >= X1 and mouseX <= X2 and mouseY >= Y1 and mouseY <= Y2 and pygame.mouse.get_pressed()[0]:
            # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            return True
        # else:
        #     return False
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return False
