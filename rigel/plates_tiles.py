from parallel import *
# ~ from perpendicular import *
import sys
printflag = True
# ~ printflag = False
if printflag:
	sprint = print
else:
	sprint = lambda *args: None

import numpy as np
class tplate:
	def __init__(self):
		self.float = False
		self.hole = False
		self.n = 1
		self.V = 0
		
		self.xc = 0
		self.yc = 0
		self.z = 0.0
		self.id = 0
		self.tile_lx = 0
		self.tile_ly = 0
		self.nx = 0
		self.ny = 0
		
	def makexyz(self, x, y, z, lx, ly):
		n = self.nx * self.ny
		i = np.arange(n)
		ix = i%self.nx;	iy = i//self.nx;	
		slx = self.tile_lx
		sly = self.tile_ly
		x[:n] = ix * slx - slx/2*(self.nx-1) + self.xc	
		y[:n] = iy * sly - sly/2*(self.ny-1) + self.yc
		z[:n] = self.z
		lx[:n] = self.tile_lx
		ly[:n] = self.tile_ly
	def makev(self, v):
		v[:self.n] = self.V
		
		

u = tplate(); 	d = tplate(); 	f = tplate(); h = tplate()
gap = 0.02
lc = 0.1
u_lx = lc
u_ly = lc
u.nx = 1
u.ny = 1
u.n = u.nx * u.ny
u.tile_lx = u_lx / u.nx
u.tile_ly = u_ly / u.ny
u.xc = -lc / 2 - gap / 2
u.yc = 0
u.z = 0

d_lx = lc
d_ly = lc
d.nx = 1
d.ny = 1
d.n = d.nx * d.ny
d.tile_lx = d_lx / d.nx
d.tile_ly = d_ly / d.ny
d.xc = lc / 2 + gap / 2
d.yc = 0
d.z = 0

f_lx = 10 * lc
f_ly = 10 * lc
f.nx = 1
f.ny = 1
f.n = f.nx * f.ny
f.tile_lx = f_lx / f.nx
f.tile_ly = f_ly / f.ny
f.xc = 0
f.yc = 0
f.z = 1e-2

h_lx = lc/2
h_ly = lc/2
h.nx = 1
h.ny = 1
h.n = h.nx * h.ny
h.tile_lx = h_lx / h.nx
h.tile_ly = h_ly / h.ny
h.xc = 0
h.yc = 0
h.z = f.z


u.V = .5; 		d.V = -.5; 		f.float = True;	   h.hole = True

u.id = 0;	d.id = 1;	f.id = 2;   h.id = 3
n = u.n + d.n + f.n + h.n
sprint ("number of tiles",n)
x = np.zeros(n); y = np.zeros(n); z = np.zeros(n)
lx = np.zeros(n); ly = np.zeros(n); V = np.zeros(n)
up = 0
dp = up + u.n
fp = dp + d.n
hp = fp + f.n

u.makexyz(x[up:],y[up:],z[up:], lx[up:], ly[up:])
d.makexyz(x[dp:],y[dp:],z[dp:], lx[dp:], ly[dp:])
f.makexyz(x[fp:],y[fp:],z[fp:], lx[fp:], ly[fp:])
h.makexyz(x[hp:],y[hp:],z[hp:], lx[hp:], ly[hp:])

u.makev(V[up:])
d.makev(V[dp:])
f.makev(V[fp:])
h.makev(V[hp:])
# ~ "در این قسمت x-lx/2 برای تمام ماتریس محاسبه می‌شود شاید تنها برای hp: به بعد کفایت کند."
x1 = x - lx/2
x2 = x + lx/2
y1 = y - ly/2
y2 = y + ly/2

area = (lx*ly)
print ('area = ' , area)
area = (lx*ly)[hp:,np.newaxis]*np.ones(n)[np.newaxis, :]
print ('area = ' , area)
malpha = (-(np.abs(x1[hp:,np.newaxis] - x1[np.newaxis, :])+\
			(x1[hp:,np.newaxis] + x1[np.newaxis, :])) \
		+(-np.abs(x2[hp:,np.newaxis] - x2[np.newaxis, :])+\
			(x2[hp:,np.newaxis] + x2[np.newaxis, :]))) /2 
malpha[malpha<0] = 0
malpha *= (-(np.abs(y1[hp:,np.newaxis] - y1[np.newaxis, :])+\
			(y1[hp:,np.newaxis] + y1[np.newaxis, :])) \
		+(-np.abs(y2[hp:,np.newaxis] - y2[np.newaxis, :])+\
			(y2[hp:,np.newaxis] + y2[np.newaxis, :]))) /2 		
malpha[malpha<0] = 0
malpha /= area	
sprint ("malpha", malpha)

# ~ hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

# ~ matrix z, x, y
mz = np.abs( (z[:,np.newaxis]- z[np.newaxis, :] ) )
#sprint (mz)
mx = np.abs( (x[:,np.newaxis]- x[np.newaxis, :] ) )
#sprint (mx)
my = np.abs( (y[:,np.newaxis]- y[np.newaxis, :] ) )
#sprint (my)
pij = np.zeros_like(mx)
icp = mz<1e-10
ipp = np.logical_not(icp)
mlx = lx[:,np.newaxis]*np.ones(n)[np.newaxis, :]
mly = ly[:,np.newaxis]*np.ones(n)[np.newaxis, :]
pij[ipp] = parallel (mlx[ipp],mly[ipp], np.transpose(mlx)[ipp], np.transpose(mly)[ipp],\
					 mx[ipp], my[ipp], mz[ipp])
pij[icp] = parallel_coplanar (mlx[icp],mly[icp], np.transpose(mlx)[icp], np.transpose(mly)[icp],\
					 mx[icp], my[icp])
sprint("-----------------------------------")
sprint (pij)

sys.exit()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

V = np.zeros(n)
V[up:dp] = u.V
V[dp:fp] = d.V
V[fp:] = 0
# ~ naghes
# ~ pij[u.n + d.n: n - 1,:] -= pijd[u.n + d.n +
pij[fp:hp-1] -= pij[hp-1]
pij[hp-1, :fp] = 0
pij[hp-1, fp:] = 1
sprint("-----------------------------------")
sprint (pij)


q = np.linalg.solve(pij, V)
print ('..........')
print (q)
Q = np.sum(q[:dp])
print (Q)
Q = np.sum(q[dp:fp])
print (Q)
print ('&&&&', e0 * plength * plength / f.z)
Q = np.sum(q[fp:])
print (Q)


# ~ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
