import time
from ss import *
printflag = False
if printflag:
	sprint = print
else:
	sprint = lambda *args: None
t0 =  (time.time())

for nn in range (50, 150):
	l = 1
	l2 = l / 2
	plate=[]
	zzc = [l2, -l2, 0, 0, 0, 0]
	xxc = [0, 0, l2, -l2, 0, 0]
	yyc = [0, 0, 0, 0, l2, -l2]
	ddr = [0, 3, 2, 5, 1, 4]
	for i in range(6):
		plate.append(tplate())
		plate[i].n = nn; 
		plate[i].l = l; 
		plate[i].xc, plate[i].yc, plate[i].zc =   xxc[i], yyc[i], zzc[i]
		plate[i].dir = ddr[i]
		plate[i].index = i
		plate[i].ax = plate[i].dir % 3
		plate[i].upordown = plate[i].dir // 3
	
	for i in plate:
		i.make_tiles()
		sprint(i.i)
		sprint(i.j)
		sprint(i.k)
		sprint('--------------')
	V = np.ones(nn * nn * 6) 
	n_plate = len(plate)
	for i in range(n_plate):


		for j in range(n_plate):
			# ~ print (i,j)
			if j == 0: 
				Pj = make_Pij(plate[i], plate[j]) 
			else:
				Pj = np.append(Pj, make_Pij(plate[i], plate[j]) ,axis = 1) 
		if i == 0: 
			P = Pj 
		else:
			P = np.append(P , Pj ,axis = 0) 
	# ~ print('pr--------')
	# ~ print (pr)
	# ~ print('cp--------')
	# ~ print (cp)
	# ~ print('cc--------')
	# ~ print (cc)
	cc.clear()
	cp.clear()
	pr.clear()
	# ~ print (P[0])
	q = np.linalg.solve(P, V)
	Q = np.sum(q)
	c1 = Q 
	# ~ print (q[0:nn*nn])
	t = (time.time())
	
	print (nn, c1, c1 * k0, c1*9e9,'    ' , int((t - t0)*100) /100 )
	
