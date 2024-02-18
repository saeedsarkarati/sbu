from plates import *
import time
printflag = True
if printflag:
	sprint = print
else:
	sprint = lambda *args: None
t0 = time.time()
for nn in range (1, 2):
	tt = time.time()
	print (int( (tt - t0)*100) /100  )
	l = 1
	l2 = l / 2
	plate=[]
	zzc = [l2, -l2]
	xxc = [0, 0]
	yyc = [0, 0]
	ddr = [0, 3]

	plate.append(tplate())
	plate[0].n = nn; 
	plate[0].l = l * 2; 
	plate[0].xc, plate[0].yc, plate[0].zc =   0, 0, l2/10
	plate[0].dir = 0
	plate[0].index = 0
	plate[0].ax = 0
	plate[0].upordown = 0
	
	plate.append(tplate())
	plate[1].n = nn; 
	plate[1].l = l*2; 
	plate[1].xc, plate[1].yc, plate[1].zc =   0, 0, -l2/10
	plate[1].dir = 3
	plate[1].index = 1
	plate[1].ax = 0
	plate[1].upordown = 1
		
	for i in plate:
		i.make_tiles()
		sprint(i.i)
		sprint(i.j)
		sprint(i.k)
		sprint('--------------')
	V = np.ones(nn * nn * 2) * .5
	V[nn * nn:] = -0.5
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
		sprint (i)
		sprint (P)
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
	Q = np.sum(q[:nn*nn])
	c1 = Q 
	# ~ print (q[0:nn*nn])
	print ("ctop",nn, c1 )
	
