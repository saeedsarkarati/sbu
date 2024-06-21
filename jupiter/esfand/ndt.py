import sys
printflag = False
if printflag:
	sprint = print
else:
	sprint = lambda *args: None

from parallel import *
from perpendicular import *

# ~ All the tiles are squred.
cap_up_length = 0.1
cap_lp_length = .1
nupx = 10; nupy = 10;
nlpx = 30; nlpy = 30;
nup = nupx * nupy
nlp = nlpx * nlpy
n = nup + nlp
# ~ cap_upper_plate_tiles_length = 1; cap_lower_plate_tile_length = 1
cuptl = 1; clptl = 1
tile_up_length = cap_up_length / nupx
tile_lp_length = cap_lp_length / nlpx
up_x0 = 0;   up_y0 = 0;    up_z = 1e-2;
lp_x0 = 0;   lp_y0 = 0;    lp_z = 0;

# ~ tile_plates = np.zeros(n)
tp = np.zeros(n, dtype = int)
tx = np.zeros(n); ty = np.zeros(n); tz = np.zeros(n);
tl = np.zeros(n)
V = np.zeros(n)
# ~ tiles_ommited = np.zeros(n)
to = np.zeros(n, dtype = int)
# ~ to[4+nup] = 1
# ~ tile_indecies = np.arange(n)
ti = np.arange(n)
sprint (ti)
tp[ti<nup] = 0
tp[ti>=nup] = 1
sprint (tp)
tl[ti<nup] = tile_up_length
tl[ti>=nup] = tile_lp_length
sprint (tp)
index = 0
for i in range (nupx):
	for j in range (nupy):
		tx[index] = i * tile_up_length - tile_up_length /2 * (nupx-1) + up_x0
		ty[index] = j * tile_up_length - tile_up_length /2 * (nupy-1) + up_y0
		tz[index] = up_z
		index += 1
for i in range (nlpx):
	for j in range (nlpy):
		tx[index] = i * tile_lp_length - tile_lp_length /2 * (nlpx-1) + lp_x0
		ty[index] = j * tile_lp_length - tile_lp_length /2 * (nlpy-1) + lp_y0
		tz[index] = lp_z
		index += 1
sprint (tx)
sprint (ty)
sprint (tz)
sprint (to)
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
pij[mp != 0] = parallel (ml1[mp != 0], 1, 1, 1, mx[mp != 0], my[mp != 0], mz[mp != 0])
sprint('----------------')
pij[mp != 0] = parallel (ml1[mp != 0], ml1[mp != 0], ml2[mp != 0], ml2[mp != 0], \
			   mx[mp != 0], my[mp != 0], mz[mp != 0])
pij[mp == 0] = parallel_coplanar (ml1[mp == 0], ml1[mp == 0], ml2[mp == 0], ml2[mp == 0],\
			   mx[mp == 0], my[mp == 0])
sprint (pij)
V[ti<nup] = 0.5
V[ti>=nup] = -0.5
q = np.linalg.solve(pij, V)
sprint ('..........')
sprint (q)
Q = np.sum(q[ti<nup])
print (Q)
Q = np.sum(q[ti>=nup])
sprint (Q)
sprint (e0 * cap_up_length * cap_lp_length / up_z)
