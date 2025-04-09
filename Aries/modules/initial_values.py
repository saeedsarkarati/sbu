import numpy as np

Tx =  [-1, -1,  1,  1]
Ty =  [-1,  1, -1,  1]
Tz =  [ 0,  0,  0,  0]
Tlx = [ 2,  2,  2,  2]
Tly = [ 2,  2,  2,  2]

Hx =  [-0.5,  0, 1.75, 1.75]
Hy =  [-0.5,  0,   -1, 1   ]
Hz =  [   0, -1,    0, 0   ]
Hlx = [   1,  0,  0.5, 0.5 ]
Hly = [   1,  0,    2, 2   ]

Tx = np.array(Tx, dtype = float)
Ty = np.array(Ty, dtype = float)
Tz = np.array(Tz, dtype = float)
Tlx = np.array(Tlx, dtype = float)
Tly = np.array(Tly, dtype = float)

Hx = np.array(Hx, dtype = float)
Hy = np.array(Hy, dtype = float)
Hz = np.array(Hz, dtype = float)
Hlx = np.array(Hlx, dtype = float)
Hly = np.array(Hly, dtype = float)
def ss_init():
	return Tx, Ty, Tz, Tlx, Tly, Hx, Hy, Hz, Hlx, Hly
def ss_print():
	np.set_printoptions(formatter={'float': '{:8.3f}'.format})
	print (Tx)
	print (Ty)
	print (Tz)
	print (Tlx)
	print (Tly)
	
	print()
	print (Hx)
	print (Hy)
	print (Hz)
	print (Hlx)
	print (Hly)
	
