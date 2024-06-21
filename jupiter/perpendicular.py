#Coupling Coeffitient
from cc_ss import *
from scipy.special import erf
import numpy as np
k0 = 8.9875517923e9
e0 = 1 / (4 * np.pi * k0)
def Kss(x1, y1, z1):
	x = np.float64(x1)
	y = np.float64(y1)
	z = np.float64(z1)
	# ~ if type(x) == type(1.5):
		# ~ x = np.array([x])
		# ~ y = np.array([y])
		# ~ z = np.array([z])
	R = np.sqrt(x**2 + y**2 + z**2)
	K0 = -(y * z* R)/6
#  Condition of 1
	K1 = np.zeros_like (x)
	C1 = np.logical_or (x !=0 , z !=0)
	K1[C1] = -(z[C1]*(-3*x[C1]**2 + z[C1]**2)*np.arcsinh(y[C1]/np.hypot(x[C1], z[C1])))/12.

	K2 = np.zeros_like (x)
	C2 = np.logical_or (x !=0 , y !=0)
	K2[C2] = -(y[C2]*(-3*x[C2]**2 + y[C2]**2)*np.arcsinh(z[C2]/np.hypot(x[C2], y[C2])))/12.
	K3 = np.zeros_like (x)
	C3 = np.logical_or (y !=0 , z !=0)
	K3[C3] = (x[C3]*y[C3]*z[C3]*np.arcsinh(x[C3]/np.hypot(y[C3], z[C3])))/2.
	K4 = np.zeros_like (x)
	C4 = z !=0 
	K4[C4] = -(x[C4]*z[C4]**2*np.arctan(x[C4] * y[C4] / (z[C4] * R[C4] )))/4.
	K5 = np.zeros_like (x)
	C5 = y !=0 
	K5[C5] = -x[C5]*y[C5]**2*np.arctan( x[C5] * z[C5] / (y[C5] * R[C5] ) )/4.
	K6 = np.zeros_like (x)
	C6 = x !=0 
	K6[C6] = -x[C6]**3*np.arctan( y[C6] * z[C6] / (x[C6] * R[C6] ) ) /12.
	# ~ ---------------------
	II =  np.sqrt(np.pi) * (K0 + K1 + K2 + K3 + K4 + K5 + K6 )
	return II
def KSum(Limits):
	y, z = Limits[4]
	s = 0
	for i in [0, 1]:
		for j in [0, 1]:
			for k in [0, 1]:
				for l in [0, 1]:
					if (i + j + k + l) % 2 == 0:
						A = 1
					else:
						A = -1
					s += A * Kss(Limits[0][i] - Limits[1][j], Limits[2][k] - y, \
								 Limits[3][l] - z)
	return s
	
def perpendicular(Lx ,Ly,x0,y0,z0):

	L = Lx
	x1 = [x0-L/2, x0+L/2]
	x2 = [-L/2, L/2]
	y1 = [y0-L/2, y0+L/2]
	z1 = [z0-L/2, z0+L/2]
	z = 0
	y = 0
	Limits = [x1, x2, y1, z1,[y, z]]
	return -KSum(Limits) * k0 / (L*L)**2  *2 /np.sqrt(np.pi)
if __name__ == "__main__":
	print ("%e" %saeed (2, 2, 0, 0 , 1))
	print ("%e" %perpendicular())
