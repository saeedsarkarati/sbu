import pygame
from pygame.locals import *
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
Lx = 300
Ly = 300
ss = pygame.Surface((Lx, Ly)) 
n = 6
n1 = n + 1
lx = Lx // n1
ly = Ly // n1
ss.fill(white)
setA = [0, 5, 30, 35]
setB = [1, 4, 6, 11, 24, 29, 31, 34]
setC = [2, 3, 12, 17, 18, 23, 32, 33]
setD = [7, 10, 25, 28]
setE = [8, 9, 13, 16, 19, 22, 26, 27]
setF = [14, 15, 20, 21]
setss = [setA, setB, setC, setD, setE, setF]
letss = ['A', 'B', 'C' , 'D', 'E', 'F']
def ktomw(k):
	for i in range (len(setss)):
		if k in setss[i]:
			return letss[i]
	return '#'
def ktoc(k):
	for i in range (len(setss)):
		if k in setss[i]:
			return 255 - i * 200 // 6
	return 0
for i in range(n1):
	pygame.draw.line(ss, black, (i * lx + lx // 2 , ly //2 ) , (i * lx + lx // 2 , ly //2  + ly * n))
for j in range(n1):
	pygame.draw.line(ss, black, (lx // 2 , j * ly + ly //2 ) , (n * lx + lx // 2 , j * ly + ly //2 ))
# ~ font = pygame.font.SysFont('IRTabassom', 25, bold=True)
font = pygame.font.SysFont('IRTabassom', 25)
for k in range(n * n):
	i = k % n
	j = k// n
	mw = ktomw(k)
	c = ktoc(k)
	# ~ c = 100
	pygame.draw.rect(ss, (c, c, c), ( i * lx + lx // 2 + 1, j * ly + ly // 2 + 1, lx - 1, ly - 1))
	ff = font.render(mw, True, black, (c, c, c))
	xf = ff.get_width(); yf = ff.get_height()
	ss.blit(ff, (i * lx + lx - xf // 2, j * ly + ly - yf // 2 )) 

	pass
	# ~ pygame.draw.
pygame.image.save(ss, 'maxwell3.png')



