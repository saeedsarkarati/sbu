from cc_ss import *

class tplate:
	def __init__(self):
		self.xc = 0
		self.yc = 0
		self.zc = 0
		self.na = 1
		self.nb = 1
		self.la = 1
		self.lb = 1
		self.x = None
		self.y = None
		self.z = None
		self.voltage = 1
		self.e_out = 1
		self.e_in = 1
	def make_tiles(self):
		a = (np.arange(-self.na + 1, self.na ,2) )/(2 * self.na) * self.la
		b = (np.arange(-self.nb + 1, self.nb ,2) )/(2 * self.nb) * self.lb
		a , b = np.meshgrid(a, b)
		a, b = a.flatten(), b.flatten()
		self.x = a + self.xc 
		self.y = b + self.yc
		self.z = np.zeros_like(a) + self.zc
	
def make_Pij(pi, pj):
	pix,piy,piz = pi.x-pj.xc, pi.y-pj.yc, pi.z-pj.zc
	pjx,pjy,pjz = pj.x-pj.xc, pj.y-pj.yc, pj.z-pj.zc
	dx = pix[:,np.newaxis]- pjx[np.newaxis, :] 
	dy = piy[:,np.newaxis]- pjy[np.newaxis, :] 
	dz = piz[:,np.newaxis]- pjz[np.newaxis, :] 
	d = np.sqrt (dx*dx + dy*dy + dz*dz)
	Pij = np.zeros_like (d)
	cond1 = dz * dz < 1e-15
	cond2 = np.logical_not(cond1)
	zcond1 = dx * dx + dy * dy + dz * dz < 1e-15
	zcond2 = np.logical_not(zcond1)
	
	# ~ Pij[zcond1] = orion(pj.la / pj.na, pj.lb / pj.nb) 
	# ~ Pij[zcond2] = zho(pj.la/ pj.na, pj.lb / pj.nb, dx[zcond2], dy[zcond2], dz[zcond2]) 
	# ~ Pij[cond1] = hitoshi_coplanar(pj.la / pj.na, pj.lb / pj.nb, dx[cond1], dy[cond1]) 
	# ~ Pij[cond2] = hitoshi(pj.la/ pj.na, pj.lb / pj.nb, dx[cond2], dy[cond2], dz[cond2]) 
	Pij[cond1] = saeed_coplanar(pj.la / pj.na, pj.lb / pj.nb, dx[cond1], dy[cond1]) 
	Pij[cond2] = saeed(pj.la/ pj.na, pj.lb / pj.nb, dx[cond2], dy[cond2], dz[cond2]) 
	return Pij



