#Coupling Coeffitient driven by our team
# ~ parallel plates
from scipy.special import erf
import numpy as np
k0 = 9e9
e0 = 1 / (4 * np.pi * k0)
def Iss(x1, x2, y1, y2, z):
	x = np.abs(x1 - x2)
	y = np.abs(y1 - y2)
	z = np.abs(z)
	I1 = 1 / 12 * (- x**2 - y**2 + 2 * z**2) * ( x**2 + y**2 + z**2) ** (1/2)
	I2 =  1 / 4 * (y * (x**2 - z**2) ) * np.arcsinh(y / np.hypot(x, z) )
	I3 =  1 / 4 * (x * (y**2 - z**2) ) * np.arcsinh(x / np.hypot(y, z) )
	I4 = -1 / 2 * x * y * z * np.arctan(x * y /(z * np.sqrt(x**2 + y**2 + z**2) ) )
	II = np.sqrt(np.pi) * ( I1 + I2 + I3 + I4 )
	return II
def Iss_coplanar(x1, x2, y1, y2):
	x = np.abs(x1 - x2)
	y = np.abs(y1 - y2)
	I1 = 1 / 12 * (- x**2 - y**2) * ( x**2 + y**2) ** (1/2)
	x0 = (x == 0)
	y0 = (y == 0)
	xn = np.logical_not(x0)
	yn = np.logical_not(y0)
	I2 = np.zeros_like (x)
	I3 = np.zeros_like (x)
	I2[x0] = 0
	I2[xn] =  1 / 4 * ( y[xn] * x[xn]**2 ) * np.arcsinh( y[xn] / x[xn] )
	I3[y0] = 0
	I3[yn] =  1 / 4 * ( x[yn] * y[yn]**2 ) * np.arcsinh( x[yn] / y[yn] )
	II = np.sqrt(np.pi) * ( I1 + I2 + I3 )
	return II
def ISum(Limits, z):
	s = 0
	for i in [0, 1]:
		for j in [0, 1]:
			for k in [0, 1]:
				for l in [0, 1]:
					if (i + j + k + l) % 2 == 0:
						A = 1
					else:
						A = -1
					s += A * Iss(Limits[0][i], Limits[1][j], Limits[2][k], Limits[3][l], z)
	return s

def ISum_coplanar(Limits):
	s = 0
	for i in [0, 1]:
		for j in [0, 1]:
			for k in [0, 1]:
				for l in [0, 1]:
					if (i + j + k + l) % 2 == 0:
						A = 1
					else:
						A = -1
					s += A * Iss_coplanar(Limits[0][i], Limits[1][j], Limits[2][k], Limits[3][l])
	return s

def saeed(Lx ,Ly,x0,y0,z):
	x1L = [x0-Lx/2, x0+Lx/2]
	x2L = [-Lx/2, +Lx/2]
	y1L = [y0-Ly/2, y0+Ly/2]
	y2L = [-Ly/2, +Ly/2]
	Limits = [x1L, x2L, y1L, y2L]
	return ISum(Limits, z) * k0 / (Lx*Ly)**2 *2 /np.sqrt(np.pi)
def saeed_coplanar(Lx ,Ly,x0,y0):
	x1L = [x0-Lx/2, x0+Lx/2]
	x2L = [-Lx/2, +Lx/2]
	y1L = [y0-Ly/2, y0+Ly/2]
	y2L = [-Ly/2, +Ly/2]
	Limits = [x1L, x2L, y1L, y2L]
	return ISum_coplanar(Limits) * k0 / (Lx*Ly)**2 *2 /np.sqrt(np.pi)
def saeed_sc(x ,y):
	II = 1 / 3 * (x**3 + y**3) + 1 / 3 * (-x**2 - y**2)*np.hypot(x, y) + \
	     y * x**2 * np.arcsinh (y / x) + x * y**2 * np.arcsinh (x / y)
	return II * k0 / (x*y)**2 *2 
if __name__ == "__main__":
	d = 0
	Lx = 1
	Ly = 1
	x1L = [d-Lx/2, d+Lx/2]
	x2L = [-Lx/2, +Lx/2]
	y1L = [-Ly/2, +Ly/2]
	y2L = [-Ly/2, +Ly/2]
	Limits = [x1L, x2L, y1L, y2L]
	z = 1e-9
	Isc = saeed_sc(Lx, Ly)
	print ('saeed self copling %e' %Isc)

	Icp = saeed_coplanar(Lx, Ly, d, 0)
	print ('saeed coplanar %e' %Icp)

	Is = saeed(Lx, Ly, d, 0, z)
	print ('saeed %e' %Is)
