import pygame
from pygame.locals import *
pygame.init()
sc = pygame.display.set_mode((800, 600))

red = (255, 0, 0)
blue = (0, 0, 255)
pygame.draw.circle(sc, red, (400,300), 100)
                                
pygame.draw.rect(sc, blue, (400,300, 500,600))
# -----------------




# ---------------
pygame.display.update()

cont = True
while cont:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == K_q:
				cont = False
		if event.type == QUIT:
			cont = False
pygame.quit()
