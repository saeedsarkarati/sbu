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
def entofa(en):
	fa = ''
	diff = ord ('۰') - ord('0')
	for i in range (len(en)):
		fa += chr (ord(en[i]) + diff)
	return fa
for i in range(n1):
	pygame.draw.line(ss, black, (i * lx + lx // 2 , ly //2 ) , (i * lx + lx // 2 , ly //2  + ly * n))
for j in range(n1):
	pygame.draw.line(ss, black, (lx // 2 , j * ly + ly //2 ) , (n * lx + lx // 2 , j * ly + ly //2 ))
# ~ font = pygame.font.SysFont('IRTabassom', 25, bold=True)
font = pygame.font.SysFont('IRTabassom', 25)
for k in range(n * n):
	i = k % n
	j = k// n
	en = str (k+1)
	fa = entofa(en)
	ff = font.render(fa, True, black, white)
	xf = ff.get_width(); yf = ff.get_height()
	ss.blit(ff, (i * lx + lx - xf // 2, j * ly + ly - yf // 2 )) 

	pass
	# ~ pygame.draw.
pygame.image.save(ss, 'maxwell1.png')



