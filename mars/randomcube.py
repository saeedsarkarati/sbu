import pygame
from pygame.locals import *
pygame.init()
sc = pygame.display.set_mode((800, 600))

import numpy as np
k0 = 9e9
n = 200
l = 1
l2 = l / 2
x = l2-np.random.rand(n)*l2/10
y = l2-np.random.rand(n)*l2/10
z = np.ones(n) * l2
def energy(i):
	X = np.copy(x)
	Y = np.copy(y)
	Z = np.copy(z)
	X, Y, Z = np.concatenate((X, Y)), np.concatenate((Y, X)) ,np.concatenate((Z, Z))
	X, Y, Z = np.concatenate((X,  -Y, -X, Y)), np.concatenate((Y, X, -Y, -X)) ,np.concatenate((Z, Z, Z, Z))
	X, Y, Z = np.concatenate((X,  X,  Z, -Z,  Y,  Y)), np.concatenate((Y,  Y,  X,  X,  Z, -Z)),\
			  np.concatenate((Z, -Z,  Y,  Y,  X,  X))
	R = np.sqrt((X-x[i])**2+ (Y-y[i])**2+(Z-z[i])**2)**.5
	e = np.zeros_like(R)
	e[R>0] = 1/R[R>0]
	E= np.sum(e)
	return E
def totalenergy():
	X = np.copy(x)
	Y = np.copy(y)
	Z = np.copy(z)
	X, Y, Z = np.concatenate((X, Y)), np.concatenate((Y, X)) ,np.concatenate((Z, Z))
	X, Y, Z = np.concatenate((X,  -Y, -X, Y)), np.concatenate((Y, X, -Y, -X)) ,np.concatenate((Z, Z, Z, Z))
	X, Y, Z = np.concatenate((X,  X,  Z, -Z,  Y,  Y)), np.concatenate((Y,  Y,  X,  X,  Z, -Z)),\
			  np.concatenate((Z, -Z,  Y,  Y,  X,  X))

	xx = (X[:,np.newaxis]- x[np.newaxis, :] )
	yy = (Y[:,np.newaxis]- y[np.newaxis, :] )
	zz = (Z[:,np.newaxis]- z[np.newaxis, :] )
	R = np.sqrt(xx**2+ yy**2+zz**2)**.5
	e = np.zeros_like(R)
	e[R>0] = 1/R[R>0]
	E= np.sum(e)
	return E * 48
# ~ for i in range(n):
	# ~ print (energy(i))
# ~ print (totalenergy())
# ~ print ('---------')
cont = True
t = 0
m = 1
while cont:
	if t > 100000:
		cont = False
		
	for e in pygame.event.get():
		if e.type == QUIT:
			cont = False

	if t%10 == 0:
		sc.fill((0,0,0))
		for i in range(n):
			xx = int (x[i] * 500)
			yy = int (y[i] * 500)
			pygame.draw.circle (sc, (255, 255, 0), (xx, yy), 2)
		pygame.display.update()
		E = totalenergy()
		nq = n * 48
		Eq = E * k0
		c = nq * nq / (2 * Eq)
		print (t, E, c)
	m += .01
	mm = int (m)
	if mm > n:
		mm = n
	i = np.random.randint(n)
	xx = x[i]
	yy = y[i]
	E1 = energy(i)
	x[i] = np.random.rand()*l2
	y[i] = np.random.rand()*l2
	if E1 < energy(i):
		x[i] = xx
		y[i] = yy
	else : 
		a = 0.9
		x[i] = (1-a) * xx + a * x[i]
		y[i] = (1-a) * yy + a * y[i]
	t += 1	
# ~ pygame.quit()
cont = True
while cont:
	for e in pygame.event.get():
		if e.type == QUIT:
			cont = False
pygame.quit()
#2528.6853272232265
#52.680979167387235
#2.4009172553075473e-09
#n= 100  4.879250839253576e-11
#n= 10 4.916465594605384e-11
# n = 1000 4.837236660091801e-11

