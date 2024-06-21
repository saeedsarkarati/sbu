import sys


from parallel import *
from perpendicular import *

# ~ All the tiles are squred.
nupx = 1; nupy = 1;
nlpx = 3; nlpy = 3;
nup = nupx * nupy
nlp = nlpx * nlpy
n = nup + nlp
# ~ cap_upper_plate_tiles_length = 1; cap_lower_plate_tile_length = 1
cuptl = 1; clptl = 1
tile_up_length = .1
tile_lp_length = 1
up_x0 = 0;   up_y0 = 0;    up_z = 1;
lp_x0 = 0;   lp_y0 = 0;    lp_z = 0;

# ~ tile_plates = np.zeros(n)
tp = np.zeros(n, dtype = int)
tx = np.zeros(n); ty = np.zeros(n); tz = np.zeros(n);
tl = np.zeros(n)
# ~ tiles_ommited = np.zeros(n)
to = np.zeros(n, dtype = int)
# ~ to[4+nup] = 1
# ~ tile_indecies = np.arange(n)
ti = np.arange(n)
print (ti)
tp[ti<nup] = 0
tp[ti>=nup] = 1
print (tp)
tl[ti<nup] = tile_up_length
tl[ti>=nup] = tile_lp_length
print (tp)
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
print (tx)
print (ty)
print (tz)
print (to)
# ~ matrix z
mz = np.abs( (tz[:,np.newaxis]- tz[np.newaxis, :] ) )
print (mz)
mx = np.abs( (tx[:,np.newaxis]- tx[np.newaxis, :] ) )
print (mx)
my = np.abs( (ty[:,np.newaxis]- ty[np.newaxis, :] ) )
print (my)
# ~ matrix plates
mp = np.abs( (tp[:,np.newaxis]- tp[np.newaxis, :] ) )
print (mp)
pij = np.zeros_like(mx)
print ("%%%%%%%%%%%%")
ml1 = (tl[:,np.newaxis] -0*tl[np.newaxis, :])
ml2  = (tl[np.newaxis, :] -0*tl[:, np.newaxis])
pij[mp != 0] = parallel (ml1[mp != 0], 1, 1, 1, mx[mp != 0], my[mp != 0], mz[mp != 0])
print('----------------')
pij[mp != 0] = parallel (ml1[mp != 0], ml1[mp != 0], ml2[mp != 0], ml2[mp != 0], \
			   mx[mp != 0], my[mp != 0], mz[mp != 0])
pij[mp == 0] = parallel_coplanar (ml1[mp == 0], ml1[mp == 0], ml2[mp == 0], ml2[mp == 0],\
			   mx[mp == 0], my[mp == 0])
print (pij)
for i in range(n):
	for j in range (n):
		print (i, j, end = '----:  ')
		
		if tp[i] == tp [j]:
			print ("%E"%parallel_coplanar(tl[i], tl[i], tl[j], tl[j],\
				np.abs(tx[i] - tx[j]), np.abs(ty[i] - ty[j]) ) )
		else:
			print ("%E"%parallel(tl[i], tl[i], tl[j], tl[j],\
				np.abs(tx[i] - tx[j]), np.abs(ty[i] - ty[j]), np.abs(tz[i] - tz[j]) ) )
			
