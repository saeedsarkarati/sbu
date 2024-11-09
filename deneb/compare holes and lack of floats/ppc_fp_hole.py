# ~ برنامه محاسبه ظرفیت خازنی برای دو صفحه خازن و یک صفحه شناور و شکافی در میان صفحه شناور
# ~ در این برنامه صفحه شناور به صورت دو صفحه نازک مجاور هم تعریف شده است.
# ~ و شکاف نیز در هر دو صفحه شناور تعریف می‌شود.
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
		
u = tplate(); 	d = tplate();	fu = tplate();	fd = tplate();	hu = tplate();	hd = tplate();
lc = 0.1
gap = lc/10000
nx = 1;	ny = 1

u_lx = lc;	u_ly = lc
u.nx = nx;	u.ny = ny;	u.n = u.nx * u.ny
u.tile_lx = u_lx / u.nx;	u.tile_ly = u_ly / u.ny
u.xc = 0;	u.yc = 0;	u.z = gap/2

d_lx = lc;	d_ly = lc
d.nx = nx;	d.ny = ny;	d.n = d.nx * d.ny
d.tile_lx = d_lx / d.nx;	d.tile_ly = d_ly / d.ny
d.xc = 0;	d.yc = 0;	d.z = -gap/2

fu_lx = lc ;	fu_ly = lc
fu.nx = nx;	fu.ny = ny;	fu.n = fu.nx * fu.ny
fu.tile_lx = fu_lx / fu.nx;	fu.tile_ly = fu_ly / fu.ny
fu.xc = 0;	fu.yc = 0;	fu.z = gap/4

fd_lx = lc;	fd_ly = lc
fd.nx = nx;	fd.ny = ny;	fd.n = fd.nx * fd.ny
fd.tile_lx = fd_lx / fd.nx;	fd.tile_ly = fd_ly / fd.ny
fd.xc = 0;	fd.yc = 0;	fd.z = -gap/4

hu_lx = lc/2;	hu_ly = lc /2
hu.nx = 1;	hu.ny = 1;	hu.n = hu.nx * hu.ny
hu.tile_lx = hu_lx / hu.nx;	hu.tile_ly = hu_ly / hu.ny
hu.xc = 0;	hu.yc = 0;	hu.z = gap/4

hd_lx = lc/2;	hd_ly = lc /2
hd.nx = 1;	hd.ny = 1;	hd.n = hd.nx * hd.ny
hd.tile_lx = hd_lx / hd.nx;	hd.tile_ly = hd_ly / hd.ny
hd.xc = 0;	hd.yc = 0;	hd.z = -gap/4

n = u.n + d.n + fu.n + fd.n + hu.n + hd.n
sprint ("number of tiles",n)
x = np.zeros(n); y = np.zeros(n); z = np.zeros(n)
lx = np.zeros(n); ly = np.zeros(n); V = np.zeros(n)

up = 0;	dp = up + u.n;	fup = dp + d.n;	fdp = fup + fu.n;	\
	hup = fdp + fd.n;	hdp = hup + hu.n

u.makexyz(x[up:],y[up:],z[up:], lx[up:], ly[up:])
d.makexyz(x[dp:],y[dp:],z[dp:], lx[dp:], ly[dp:])
fu.makexyz(x[fup:],y[fup:],z[fup:], lx[fup:], ly[fup:])
fd.makexyz(x[fdp:],y[fdp:],z[fdp:], lx[fdp:], ly[fdp:])
hu.makexyz(x[hup:],y[hup:],z[hup:], lx[hup:], ly[hup:])
hd.makexyz(x[hdp:],y[hdp:],z[hdp:], lx[hdp:], ly[hdp:])

u.makev(V[up:], 0.5)
d.makev(V[dp:], -0.5)
fu.makev(V[fup:], 0)
fd.makev(V[fdp:], 0)
hu.makev(V[hup:], 0)
hd.makev(V[hdp:], 0)
sprint ("V = ", V)
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

sprint("--------before changes---------------------------")
sprint ("pij = ",pij)
sprint ("V = ", V)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
x1 = x - lx/2
x2 = x + lx/2
y1 = y - ly/2
y2 = y + ly/2

area = (lx *ly)#[hp:,np.newaxis]*np.ones(n)[np.newaxis, :])

malpha = (-(np.abs(x1[hup:,np.newaxis] - x1[np.newaxis, :])+\
			(x1[hup:,np.newaxis] + x1[np.newaxis, :])) \
		+(-np.abs(x2[hup:,np.newaxis] - x2[np.newaxis, :])+\
			(x2[hup:,np.newaxis] + x2[np.newaxis, :]))) /2 
malpha[malpha<0] = 0
malpha *= (-(np.abs(y1[hup:,np.newaxis] - y1[np.newaxis, :])+\
			(y1[hup:,np.newaxis] + y1[np.newaxis, :])) \
		+(-np.abs(y2[hup:,np.newaxis] - y2[np.newaxis, :])+\
			(y2[hup:,np.newaxis] + y2[np.newaxis, :]))) /2 		
malpha[malpha<0] = 0
malpha[ipp[hup:]] = 0
malpha /= area	
sprint("malpha = ", malpha)
# ~ sys.exit()



## changing the pij and V matrix to solve satify the final state equations
# U and D plate equations
pij[:fup-1] -= pij[fup-1]
V[:fup-1] -= V[fup-1]
pij[fup-1, :fup] = 1
pij[fup-1, fup:] = 0
V[fup-1] = 0


# float plate equations 
# subsitude last float from all cuz the V of tiles of the float are equal
pij[fup:hup-1] -= pij[hup-1]
# sumation of the Qs of the float and hole must be equal to 0
pij[hup-1, :fup] = 0
pij[hup-1, fup:] = 1
# Qs of the hole = - malpha * Q of the float under that
pij[hup: , :fup] = 0
pij[hup: , fup:hup] = malpha[: , fup:hup ]
pij[hup: , hup:] = np.identity(hu.n+ hd.n)

sprint("^^^^^^^^^^after changes^^^^^^^")
sprint ("pij = ", pij)
sprint ("V = ", V)


# ~ sys.exit()


q = np.linalg.solve(pij, V)
sprint("q:",q)
Q = q[:dp].sum()
sprint ("q: u = ", Q)
sprint ("c = q / v", Q/1)
sprint (e0 * lc * lc / gap)
sys.exit()



