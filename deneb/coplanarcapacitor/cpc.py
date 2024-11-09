# ~ این برنامه برای محاسبه ظرفیت خازنی ما بین دو صفحه هم سطح نوشته شده است.
# ~ در این برنامه اختلاف ولتاژ بین دو صفحه ثابت فرض می‌شود.
from parallel import *
import matplotlib.pyplot as plt

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
		self.nx = 0
		self.ny = 0
		self.n = 1
		self.tile_lx = 0
		self.tile_ly = 0
		self.xc = 0
		self.yc = 0
		self.z = 0.0
		
	def makexyz(self, x, y, z, lx, ly):
		n = self.nx * self.ny
		i = np.arange(n)
		ix = i%self.nx;	iy = i//self.nx;	
		slx = self.tile_lx
		sly = self.tile_ly
		x[:n] = ix * slx - slx/2*(self.nx-1) + self.xc	
		y[:n] = iy * sly - sly/2*(self.ny-1) + self.yc
		z[:n] = self.z
		lx[:n] = slx
		ly[:n] = sly
	def makev(self, v, V):
		v[:self.n] = V
		
u = tplate(); 	d = tplate(); 	
lc = 0.1
gap = lc/10

u_lx = lc;	u_ly = lc
u.nx = 10;	u.ny = 10;	u.n = u.nx * u.ny
u.tile_lx = u_lx / u.nx;	u.tile_ly = u_ly / u.ny
u.xc = lc/2+gap/2;	u.yc = 0;	u.z = 0

d_lx = lc;	d_ly = lc
d.nx = 10;	d.ny = 10;	d.n = d.nx * d.ny
d.tile_lx = d_lx / d.nx;	d.tile_ly = d_ly / d.ny
d.xc = -lc/2-gap/2;	d.yc = 0;	d.z = 0


n = u.n + d.n
sprint ("number of tiles",n)
x = np.zeros(n); y = np.zeros(n); z = np.zeros(n)
lx = np.zeros(n); ly = np.zeros(n); V = np.zeros(n)

up = 0
dp = up + u.n

u.makexyz(x[up:],y[up:],z[up:], lx[up:], ly[up:])
d.makexyz(x[dp:],y[dp:],z[dp:], lx[dp:], ly[dp:])

u.makev(V[up:], 0.5)
d.makev(V[dp:], -0.5)

# ~ matrix z, x, y
mz = np.abs( (z[:,np.newaxis]- z[np.newaxis, :] ) )
mx = np.abs( (x[:,np.newaxis]- x[np.newaxis, :] ) )
my = np.abs( (y[:,np.newaxis]- y[np.newaxis, :] ) )
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
sprint (V)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

## changing the pij and V matrix to solve satify the final state equations
# U and D plate equations
pij[:-1] -= pij[-1]
V[:-1] -= V[-1]
pij[-1, :] = 1
V[-1] = 0
sprint (pij)
sprint (V)


q = np.linalg.solve(pij, V)
sprint("q:",q)
Q = q[:int(n/2)].sum()
sprint ("q: uf = ", Q)
sprint ("c = q / v", Q/1)
sprint (e0 * lc * lc / gap)
sys.exit()



