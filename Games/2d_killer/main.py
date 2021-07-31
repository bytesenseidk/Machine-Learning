import os
import sys
import pygame
from pygame.locals import *

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# def main():
#     BACKGROUND = pygame.image.load("background.jpg")
#     BACKGROUND_RECT = BACKGROUND.get_rect()
#     FPS = 60
#     BLACK = (0,0,0)

#     PLAYER = pygame.draw.rect(screen, BLACK(200,200,100,50))


#     while True:
#         pygame.init()
#         pygame.display.set_caption("2D Killer")
#         clock = pygame.time.Clock()
#         screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#         clock.tick(FPS)
#         screen.blit(BACKGROUND, BACKGROUND_RECT)
#         pygame.display.flip()
#         screen.fill(BLACK)

#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             pygame.display.update()

# main()

def main():
    pygame.init()
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 800

    DISPLAY=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()