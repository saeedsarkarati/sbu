
from cc_ss import *
from perpendicular import *
cc = {} #self 
cp = {} #coplanar
pr = {} #perpendicular
class tplate:
	def __init__(self):
		self.xc = 0
		self.yc = 0
		self.zc = 0
		self.n = 1
		self.l = 1
		self.x = None
		self.y = None
		self.z = None
		self.i = None
		self.j = None
		self.k = None
		self.voltage = 1
		self.e_out = 1
		self.e_in = 1
		self.dir = 0
		self.ax = 0
		self.index = 0
		self.upordown = 0
	def make_tiles(self):
		a = (np.arange(-self.n + 1, self.n ,2) )/(2 * self.n) * self.l
		b = (np.arange(-self.n + 1, self.n ,2) )/(2 * self.n) * self.l
		a , b = np.meshgrid(a, b)
		a, b = a.flatten(), b.flatten()
		
		if self.ax == 0: 
			self.x = a + self.xc 
			self.y = b + self.yc
			self.z = np.zeros_like(a) + self.zc
		if self.ax == 2: 
			self.y = a + self.yc 
			self.z = b + self.zc
			self.x = np.zeros_like(a) + self.xc
		if self.ax == 1: 
			self.x = a + self.xc 
			self.z = b + self.zc
			self.y = np.zeros_like(a) + self.yc

		i = np.arange(1, self.n * 2, 2)
		j = np.arange(1, self.n * 2, 2)
		i , j = np.meshgrid(i, j)
		i, j = i.flatten(), j.flatten()

		if self.upordown == 0:
			k = np.zeros_like(i)
		else:
			k = np.ones_like(i) * self.n * 2
			
			
		if self.ax == 0: 
			self.i = i 
			self.j = j
			self.k = k
		if self.ax == 2: 
			self.j = i 
			self.k = j
			self.i = k
		if self.ax == 1: 
			self.k = i 
			self.i = j
			self.j = k
			
			
	
def make_Pij(pi, pj):

	a = np.abs( (pi.i[:,np.newaxis]- pj.i[np.newaxis, :] ) )
	b = np.abs( (pi.j[:,np.newaxis]- pj.j[np.newaxis, :] ) )
	c = np.abs( (pi.k[:,np.newaxis]- pj.k[np.newaxis, :] ) )
	dl = pi.l / (2 * pi.n)
	dx = a * dl
	dy = b * dl
	dz = c * dl
	# ~ print (dx)
	# ~ print (dy)
	# ~ print (dz)
	d = np.sqrt (dx*dx + dy*dy + dz*dz)
	Pij = np.zeros_like (d)
	cond1 = pi.index == pj.index
	cond2 = np.logical_and(pi.index != pj.index, pi.ax == pj.ax)
	cond3 = pi.ax != pj.ax
	# ~ x = np.array([i, j, k])
	# ~ x.sort(axis = 0)
	# ~ print (pi.i, pi.j, pi.k)
	# ~ print('------')
	# ~ if pi.ax == pj.ax == 0:
		# ~ print (0, pi.i, pi.j, pi.k, pj.i, pj.j, pj.k)
	# ~ if pi.ax == pj.ax == 1:
		# ~ print (1, pi.i, pi.j, pi.k, pj.i, pj.j, pj.k)
	# ~ if pi.ax == pj.ax == 2:
		# ~ print (2, pi.i, pi.j, pi.k, pj.i, pj.j, pj.k)
	# ~ if pi.index == 0:
		
	if pi.ax == pj.ax:
		if pi.ax == pj.ax ==0:
			ddx = dx
			ddy = dy
			ddz = dz
			ii = a
			jj = b
			kk = c
		if pi.ax == pj.ax ==1:
			ddx = dz
			ddy = dx
			ddz = dy
			ii = c
			jj = a
			kk = b
		elif pi.ax == pj.ax == 2:
			ddx = dy
			ddy = dz
			ddz = dx
			ii = b
			jj = c
			kk = a
		# ~ print (ii)
		# ~ print(jj)
		t = np.array([ii,jj])
		t.sort(axis = 0)
		u = t[0] * 100 + t[1]
	else:
		if (pj.ax == 0 and pi.ax == 1) or (pj.ax == 1 and pi.ax == 0):
			ddx = dx
			ddy = dy
			ddz = dz
			ii = a
			jj = b
			kk = c
		if (pj.ax == 0 and pi.ax == 2) or (pj.ax == 2 and pi.ax == 0):
			ddx = dy
			ddy = dz
			ddz = dx
			ii = b
			jj = c
			kk = a
		if (pj.ax == 1 and pi.ax == 2) or (pj.ax == 2 and pi.ax == 1):
			ddx = dz
			ddy = dx
			ddz = dy
			ii = c
			jj = a
			kk = b
			
		t = np.array([jj,kk])
		t.sort(axis = 0)
		# ~ print ('iiiiiiiii', ii)
		# ~ print(a)
		# ~ print ('jjjjjjjjj', jj)
		# ~ print (b)
		# ~ print ('kkkkkkkkk', kk)
		# ~ print(c)
		u = t[0] * 100 + t[1] + ii * 10000
	
	# ~ print (u)

	# ~ print ('----------')
	# ~ Pij[cond2] = saeed(pj.l/ pj.n, pj.l / pj.n, ddx[cond2], ddy[cond2], ddz[cond2]) 
	# ~ Pij[cond3] = perpendicular(pj.l/ pj.n, pj.l / pj.n, ddx[cond3], ddy[cond3], ddz[cond3]) 
	for i in range(len(pi.x)):
		for j in range(len(pi.x)):
			if pi.index == pj.index:
				if not(u[i][j] in cc):
					Pij[i][j] = saeed_coplanar(pj.l / pj.n, pj.l / pj.n, ddx[i][j], ddy[i][j]) 
					cc[u[i][j]] = Pij[i][j]
				else:
					Pij[i][j] = cc[u[i][j]]
					# ~ Pij[i][j] = saeed_coplanar(pj.l / pj.n, pj.l / pj.n, ddx[i][j], ddy[i][j]) 
			elif pi.ax == pj.ax:
				if not(u[i][j] in cp):
					Pij[i][j] = saeed(pj.l / pj.n, pj.l / pj.n, ddx[i][j], ddy[i][j], ddz[i][j]) 
					cp[u[i][j]] = Pij[i][j]
				else:
					Pij[i][j] = cp[u[i][j]]
					# ~ Pij[i][j] = saeed(pj.l / pj.n, pj.l / pj.n, ddx[i][j], ddy[i][j], ddz[i][j]) 
			if pi.ax != pj.ax:
				if not(u[i][j] in pr):
					Pij[i][j] = perpendicular(pj.l / pj.n, pj.l / pj.n, ddx[i][j], ddy[i][j], ddz[i][j]) 
					pr[u[i][j]] = Pij[i][j]
				else:
					Pij[i][j] = pr[u[i][j]]
					# ~ Pij[i][j] = perpendicular(pj.l / pj.n, pj.l / pj.n, ddx[i][j], ddy[i][j], ddz[i][j]) 
				

				
	# ~ Pij[cond1] = saeed_coplanar(pj.l / pj.n, pj.l / pj.n, ddx[cond1], ddy[cond1]) 
	# ~ print (pr)
	return Pij



