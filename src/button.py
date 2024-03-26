import pygame
from graphics import screen
def __init__(self, x, y, width, height):
      self.self = self
      self.x = 0
      self.y = 0
      self.width = 0
      self.height = 0


def isClicked(X1, X2, Y1, Y2):
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    if mouseX >= X1 and mouseX <= X2 and mouseY >= Y1 and mouseY <= Y2:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if pygame.mouse.get_pressed()[0]:
            print("test1")
            pygame.event.wait()
            return True
        else:
            return False
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return False
# def testPolygon():
#   color = (255,0,0)
#   pygame.draw.polygon(screen,color,[[200,395],[355,395],[315,460],[150,460]],2)
#   pygame.display.flip()
#   mouse_pos = pygame.mouse.get_pos
#   if pygame.mouse.get_pressed()[0] and pygame.draw.polygon(screen, color, [[200, 395], [355, 395], [315, 460], [150, 460]]).collidepoint(mouse_pos):
#     print("test")
#     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)