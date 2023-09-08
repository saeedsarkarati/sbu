from ss import *
printflag = False
if printflag:
	sprint = print
else:
	sprint = lambda *args: None
for nn in range (1, 2):
	a, b, c = 1, 1, .1
	x0, y0, z0 = 0, 0, c / 2
	plate=[]
	for i in range(2):
		plate.append(tplate())
		plate[i].na = nn; plate[i].nb = nn;
		plate[i].la = a; plate[i].lb = b
	plate[0].xc, plate[0].yc, plate[0].zc = x0, y0, z0
	plate[1].xc, plate[1].yc, plate[1].zc = x0, y0, -z0

	for i in plate:
		i.make_tiles()
		sprint(i.x)
		sprint(i.y)
		sprint(i.z)
		sprint('--------------')
	V = np.ones(nn * nn ) * 0.5
	V = np.append(V , -V)
	n_plate = len(plate)
	for i in range(n_plate):
		for j in range(n_plate):
			if j == 0: 
				Pj = make_Pij(plate[i], plate[j]) 
			else:
				Pj = np.append(Pj, make_Pij(plate[i], plate[j]) ,axis = 1) 
		if i == 0: 
			P = Pj 
		else:
			P = np.append(P , Pj ,axis = 0) 

	q = np.linalg.solve(P, V)
	Q = np.sum(q[:nn*nn])
	c1 = Q 
	print (nn, c1 )
	
