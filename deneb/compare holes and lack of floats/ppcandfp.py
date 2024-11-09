# ~ این برنامه برای محاسبه ظرفیت خازنی مابین دو صفحه خازنی نوشته شده است.
# ~ در این برنامه اختلاف ولتاژ بین دو صفحه ثابت فرض می‌شود.
# ~ در این برنامه دو صفحه فلزی در میان دو صفحه خازن جایگذاری می‌شوند به نحوی که 
# ~ حجم موثر خازن نصف شود و امیدواریم که ظرفیت دو برابر شود.
# ~ دو صفحه float یا شناور دارای ولتاژ یکسانی هستند و جمع بارها در آن‌ها برابر صفر خواهد بود.
from parallel import *
import matplotlib.pyplot as plt

import sys
printflag = True
# ~ printflag = False
if printflag:
	sprint = print
else:
	sprint = lambda *args: None
Fixed, Float, Hole = 0, 1, 2
import numpy as np
class tplate:
	def __init__(self):
		self.nx = 0
		self.ny = 0
		self.n = 1
		self.lx = 0
		self.ly = 0
		self.tile_lx = 0
		self.tile_ly = 0
		self.xc = 0
		self.yc = 0
		self.z = 0.0
		self.type = Fixed
		
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

plates = []
np = 10
lc = 0.1
lh = lc / 2
lx13 = lc;  lx24 = (lc - lh) /2
lx = [lc, lc,  lx13, lx13, lx24, lx24, lx13, lx13, lx24, lx24] 
ly13 = (lc -h)/2;  ly24 = lh
ly = [lc, lc,  ly13, ly13, ly24, ly24, ly13, ly13, ly24, ly24]
x0 = 0; y03 = x0
xc13 = x0; xc2 = x0 + lh / 2 + lx24/2; xc4 = x0 + lh /2 - lx24/2
xc = [x0, x0, xc13, xc13, xc2, xc2, xc13, xc13, x4, x4]
y0 = 0; y24 = y0

gap = lc/10000
nx = 1;	ny = 1
for i in range(np):
	plates.append()
	if i<2:
		plates[i[.type = Fixed
	else:
		plates[i[.type = Float
	plates[i].lx = lx[i]
	plates[i].ly = ly[i]
	plates[i].nx = nx; plates[i].ny = ny
	plates[i].tile_lx = plates[i].lx / plates[i].nx
	plates[i].tile_ly = plates[i].ly / plates[i].ny
	
	
# ~ u = tplate(); 	d = tplate();	fu0 = tplate();	fd0 = tplate();
# ~ fu1 = tplate();	fd1 = tplate();	fu2 = tplate();	fd2 = tplate();
# ~ fu3 = tplate();	fd3 = tplate();

u_lx = lc;	u_ly = lc
u.nx = nx;	u.ny = ny;	u.n = u.nx * u.ny
u.tile_lx = u_lx / u.nx;	u.tile_ly = u_ly / u.ny
u.xc = 0;	u.yc = 0;	u.z = gap/2

d_lx = lc;	d_ly = lc
d.nx = nx;	d.ny = ny;	d.n = d.nx * d.ny
d.tile_lx = d_lx / d.nx;	d.tile_ly = d_ly / d.ny
d.xc = 0;	d.yc = 0;	d.z = -gap/2

fu1_lx = lc;	fu1_ly = lc/2
fu.nx = nx;	fu.ny = ny;	fu.n = fu.nx * fu.ny
fu.tile_lx = fu_lx / fu.nx;	fu.tile_ly = fu_ly / fu.ny
fu.xc = 0;	fu.yc = 0;	fu.z = gap/4

fd_lx = lc*.01;	fd_ly = lc*.01
fd.nx = nx;	fd.ny = ny;	fd.n = fd.nx * fd.ny
fd.tile_lx = fd_lx / fd.nx;	fd.tile_ly = fd_ly / fd.ny
fd.xc = 0;	fd.yc = 0;	fd.z = -gap/4

n = u.n + d.n + fu.n + fd.n
sprint ("number of tiles",n)
x = np.zeros(n); y = np.zeros(n); z = np.zeros(n)
lx = np.zeros(n); ly = np.zeros(n); V = np.zeros(n)

up = 0;	dp = up + u.n;	fup = dp + d.n;	fdp = fup + fu.n

u.makexyz(x[up:],y[up:],z[up:], lx[up:], ly[up:])
d.makexyz(x[dp:],y[dp:],z[dp:], lx[dp:], ly[dp:])
fu.makexyz(x[fup:],y[fup:],z[fup:], lx[fup:], ly[fup:])
fd.makexyz(x[fdp:],y[fdp:],z[fdp:], lx[fdp:], ly[fdp:])

u.makev(V[up:], 0.5)
d.makev(V[dp:], -0.5)
fu.makev(V[fup:], 0)
fd.makev(V[fdp:], 0)
sprint (V)

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
pij[:fup-1] -= pij[fup-1]
V[:fup-1] -= V[fup-1]
pij[fup-1, :fup] = 1
pij[fup-1, fup:] = 0
V[fup-1] = 0

pij[fup:-1] -= pij[-1]
V[fup:-1] -= V[-1]
pij[-1, fup:] = 1
pij[-1, :fup] = 0
V[-1] = 0
sprint ("final****************")
sprint (pij)
sprint (V)
# ~ sys.exit()


q = np.linalg.solve(pij, V)
sprint("q:",q)
Q = q[:dp].sum()
sprint ("q: uf = ", Q)
sprint ("c = q / v", Q/1)
sprint (e0 * lc * lc / gap)
sys.exit()



