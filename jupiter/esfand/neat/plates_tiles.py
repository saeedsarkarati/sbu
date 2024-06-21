import sys
from parallel import *
from perpendicular import *
printflag = True
if printflag:
	sprint = print
else:
	sprint = lambda *args: None

class tplate:
	def __init__(self):
		self.float = False
		self.length = 0.1
		self.n = 1
		self.tile_length = 0.1
		self.V = 10
		self.xc = 0
		self.yc = 0
		self.z = 0
		self.index = 0

u = tplate(); 	d = tplate(); 	f = tplate()
r = 1
unx = r;		uny = r;		u.n = unx * uny
dnx = r;		dny = r;		d.n = dnx * dny
fnx = r*3;		fny = r*3;		fn = fnx * fny
u.V = .5; 		d.V = -.5; 		f.float = True
u.length = .1;	d.length = 0.1;	f.length = .3
u.tile_length = u.length / unx;	
d.tile_length = d.length / dnx;	
f.tile_length = f.length / fnx;	
u.index = 0;	d.index = 1;	f.index = 2
# o m m i t e d
ommited = []
udn = d.n + u.n
sprint (udn)
sys.exit()
if fnx == 3:
	ommited= [4]
if fnx == 6:
	ommited = [14, 15, 20, 21]
if fnx == 9:
	ommited = [30, 31, 32, 39, 40, 41, 48, 49, 50]
for i in range(len(ommited)):
	ommited[i] += udn
sprint (ommited)
sprint (np.shape(pij))
for i in ommited:
	qij = np.delete(qij, i, 0)
	qij = np.delete(qij, i, 1)
	V =  np.delete(V, i)
n = n - len(ommited)

n = u.n + d.n + f.n
print (n)
ti = np.arange(n)
tu = ti < u.n;	
td = np.logical_and(ti >= u.n, ti < u.n + d.n );	
tf = ti >= u.n + d.n
tp = np.zeros(n, dtype = int)
tp[tu] = u.index;	tp[td] = d.index;	tp[tf] = f.index
print (tp)
tx = np.zeros(n); ty = np.zeros(n); tz = np.zeros(n);
tl = np.zeros(n)
V = np.zeros(n)
u.xc = 0.06; 	d.xc = -0.06; 		f.xc = 0
u.yc = 0;  		d.yc = 0; 			f.yc = 0
u.z = 0;  		d.z = 0; 			f.z = 1e-2
tl[tu] = u.tile_length;	tl[td] = d.tile_length;	tl[tf] = f.tile_length
# ~ tl[tu] = u.tile_length;	tl[td] = d.tile_length;	tl[tf] = f.tile_length
sprint (tl)
tui = ti;		tdi = ti - u.n;		tfi = ti - u.n - d.n
tuix = tui%u.nx;	tuiy = tui//u.nx;	
tdix = tdi%d.nx;	tdiy = tdi//d.nx;	
tfix = tfi%f.nx;	tfiy = tfi//f.nx;
# ~ tfix = np.zeros(n);	tfiy = np.zeros(n)
tx[tu] = tuix[tu] * tl[tu] - tl[tu]/2*(u.nx-1) + u.xc	
ty[tu] = tuiy[tu] * tl[tu] - tl[tu]/2*(u.ny-1) + u.yc	

tx[td] = tdix[td] * tl[td] - tl[td]/2*(d.nx-1) + d.xc	
ty[td] = tdiy[td] * tl[td] - tl[td]/2*(d.ny-1) + d.yc	

tx[tf] = tfix[tf] * tl[tf] - tl[tf]/2*(f.nx-1) + f.xc	
ty[tf] = tfiy[tf] * tl[tf] - tl[tf]/2*(f.ny-1) + f.yc	

tz[tu] = u.z;	tz[td] = d.z;	tz[tf] = f.z

sprint ('tx')
sprint (tx)
sprint ('ty')
sprint (ty)
# ~ sprint (tz)
# ~ sys.exit()



# ~ matrix z
mz = np.abs( (tz[:,np.newaxis]- tz[np.newaxis, :] ) )
sprint (mz)
mx = np.abs( (tx[:,np.newaxis]- tx[np.newaxis, :] ) )
sprint (mx)
my = np.abs( (ty[:,np.newaxis]- ty[np.newaxis, :] ) )
sprint (my)
# ~ matrix plates
mp = np.abs( (tp[:,np.newaxis]- tp[np.newaxis, :] ) )
sprint (mp)
pij = np.zeros_like(mx)
sprint ("%%%%%%%%%%%%")
ml1 = (tl[:,np.newaxis] -0*tl[np.newaxis, :])
ml2  = (tl[np.newaxis, :] -0*tl[:, np.newaxis])
sprint('----------------')
# ~ pij[mp != 0] = parallel (ml1[mp != 0], ml1[mp != 0], ml2[mp != 0], ml2[mp != 0], \
			   # ~ mx[mp != 0], my[mp != 0], mz[mp != 0])
# ~ pij[mp == 0] = parallel_coplanar (ml1[mp == 0], ml1[mp == 0], ml2[mp == 0], ml2[mp == 0],\
			   # ~ mx[mp == 0], my[mp == 0])
#is co planar
icp = mz<1e-10
ipp = np.logical_not(icp)
pij[ipp] = parallel (ml1[ipp], ml1[ipp], ml2[ipp], ml2[ipp], \
			   mx[ipp], my[ipp], mz[ipp])
pij[icp] = parallel_coplanar (ml1[icp], ml1[icp], ml2[icp], ml2[icp],\
			   mx[icp], my[icp])
sprint (pij)
V[tu] = u.V;		V[td] = d.V
print (np.shape(pij))
print (n)
qij=np.copy(pij)
pijd = pij[1:]
# ~ pij[u.n + d.n: n - 1,:] -= pijd[u.n + d.n +
sprint(pijd)
pij[u.n+d.n:n-1] -= pijd[u.n + d.n:]
pij[n-1, :u.n + d.n] = 0
pij[n-1, u.n + d.n:] = 1
V[u.n+d.n:] = 0
sprint('pij')
sprint (pij)
# ~ sys.exit()



q = np.linalg.solve(pij, V)
sprint ('..........')
sprint (q)
Q = np.sum(q[tu])
print (Q)
Q = np.sum(q[td])
sprint (Q)
sprint ('&&&&', e0 * u.length * d.length / f.z)
# ~ -----------------------------------

# ~ for i in ommited:
	# ~ pij[i]=0
	# ~ pij[i,i] = 1
	# ~ V[i] = 0
sprint (np.shape(qij))
sprint('qij')
sprint(qij)
qijd = qij[1:]
sprint('qijd')
sprint(qijd)
qij[u.n+d.n:n-1] -= qijd[u.n + d.n:]
qij[n-1, :u.n + d.n] = 0
qij[n-1, u.n + d.n:] = 1

q = np.linalg.solve(qij, V)
sprint ('..........')
sprint (q)
Q = 0
for i in range(u.n):
	Q += q[i]
print (Q)
Q = 0
for i in range(u.n, u.n + d.n):
	Q += q[i]
sprint (Q)
