#In this version only xy plates are included
#In this version only squtre tiles are accepted
from parallel import *
# ~ from perpendicular import *
import sys
# ~ printflag = True
printflag = False
if printflag:
	sprint = print
else:
	sprint = lambda *args: None

import numpy as np
class tplate:
	def __init__(self):
		self.float = False
		self.n = 1
		self.V = 10
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
		self.n = n
		i = np.arange(n)
		ix = i%self.nx;	iy = i//self.nx;	
		slx = self.tile_lx
		sly = self.tile_ly
		x[:n] = ix * slx - slx/2*(nx-1) + self.xc	
		y[:n] = iy * sly - sly/2*(ny-1) + self.yc
		z[:n] = self.z
		lx[:n] = self.tile_lx
		ly[:n] = self.tile_ly
	def makev(self, v):
		v[:self.n] = self.v
		

u = tplate(); 	d = tplate(); 	f = tplate()
u_lx = 0.1
u_ly = 0.1
u.nx = 3
u.ny = 2
u.tile_lx = u_lx / u.nx
u.tile_ly = u_ly / u.ny
u.
u.tile_x 
nx = r * 3;			ny = r * 3;			
u.n = nx * ny
d.n = nx * ny
f.n = nx * ny 
u.V = .5; 		d.V = -.5; 		f.float = True
plength = 1
u.tile_length = plength / nx;	d.tile_length = plength / nx;	
f.tile_length = plength / nx;	
u.id = 0;	d.id = 1;	f.id = 2
n = u.n + d.n + f.n
sprint ("number of tiles",n)
x = np.zeros(n); y = np.zeros(n); z = np.zeros(n);
up = 0
dp = u.n
fp = u.n + d.n

ud_distance = plength /10
u.xc = -plength/2 - ud_distance/2 ; 	
d.xc = +plength/2 + ud_distance/2; 		
f.xc = 0e-1
u.yc = 0;  			d.yc = 0; 				f.yc = 0
u.z = 0;  			d.z = 0; 				f.z = 1e-2

u.makexyz(x[up:],y[up:],z[up:],nx)
d.makexyz(x[dp:],y[dp:],z[dp:],nx)
f.makexyz(x[fp:],y[fp:],z[fp:],nx)
# ~ print (x)
# ~ print (y)
# ~ print (z)
for i in range (n):
	sprint ("%d %f, %f, %f"%(i, x[i], y[i], z[i]))
	
# ~ hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

if True:
	holes = f.makehole(nx) + fp
	sprint (holes)
	sprint (x.size)
	x = np.delete( x, holes)
	y = np.delete( y, holes)
	z = np.delete( z, holes)
	n = x.size
	f.n = f.n - holes.size
for i in range (n):
	sprint ("%d %f, %f, %f"%(i, x[i], y[i], z[i]))
sprint (x.size, u.n, d.n, f.n, f.tile_length)
# ~ matrix z, x, y
mz = np.abs( (z[:,np.newaxis]- z[np.newaxis, :] ) )
sprint (mz)
mx = np.abs( (x[:,np.newaxis]- x[np.newaxis, :] ) )
sprint (mx)
my = np.abs( (y[:,np.newaxis]- y[np.newaxis, :] ) )
sprint (my)
pij = np.zeros_like(mx)
icp = mz<1e-10
ipp = np.logical_not(icp)
l = u.tile_length
pij[ipp] = parallel (l, l, l, l, mx[ipp], my[ipp], mz[ipp])
pij[icp] = parallel_coplanar (l, l, l, l, mx[icp], my[icp])
sprint("-----------------------------------")
sprint (pij)
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
