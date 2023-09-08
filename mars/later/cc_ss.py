#Coupling Coeffitient
from scipy.special import erf
import numpy as np
k0 = 9e9
e0 = 1 / (4 * np.pi * k0)
def Iss(x1, x2, y1, y2, z):
	x = np.abs(x1 - x2)
	y = np.abs(y1 - y2)
	z = np.abs(z)

	# ~ print (x)
	R = np.sqrt(x**2 + y**2 + z**2)

	I0 = 1 / 12 * (- x**2 - y**2 + 2 * z**2) * R ** (1/2)
	I1 = np.zeros_like (x)
	C1 = np.logical_or(x != 0, z!= 0)
	I1[C1] =  1 / 4 * (y[C1] * (x[C1]**2 - z[C1]**2) ) * np.arcsinh(y[C1] / np.hypot(x[C1], z[C1]) )
	I2 = np.zeros_like (x)
	C2 = np.logical_or(y != 0, z!= 0)
	I2[C2] =  1 / 4 * (x[C2] * (y[C2]**2 - z[C2]**2) ) * np.arcsinh(x[C2] / np.hypot(y[C2], z[C2]) )
	I3 = np.zeros_like (x)
	C3 = z != 0
	I3[C3] = -1 / 2 * x[C3] * y[C3] * z[C3] * np.arctan(x[C3] * y[C3] /(z[C3] * R[C3] ) )
	II = np.sqrt(np.pi) * ( I0 + I1 + I2 + I3 )
	return II
	I1 = 1 / 12 * (- x**2 - y**2 + 2 * z**2) * ( x**2 + y**2 + z**2) ** (1/2)
	I2 =  1 / 4 * (y * (x**2 - z**2) ) * np.arcsinh(y / np.hypot(x, z) )
	I3 =  1 / 4 * (x * (y**2 - z**2) ) * np.arcsinh(x / np.hypot(y, z) )
	I4 = -1 / 2 * x * y * z * np.arctan(x * y /(z * np.sqrt(x**2 + y**2 + z**2) ) )
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

def saeed(Lx ,Ly,x0,y0,z):
	x1L = [x0-Lx/2, x0+Lx/2]
	x2L = [-Lx/2, +Lx/2]
	y1L = [y0-Ly/2, y0+Ly/2]
	y2L = [-Ly/2, +Ly/2]
	Limits = [x1L, x2L, y1L, y2L]
	return ISum(Limits, z) * k0 / (Lx*Ly)**2 *2 /np.sqrt(np.pi)

def hitoshi_i(x ,y, d):
	r = np.sqrt(d*d + x*x +y * y)
	I1 = -d * np.arctan(x * y /(d * r))
	I2 = y * np.log(x + r)
	I3 = x * np.log(y + r)
	return I1 + I2 + I3
def hitoshi_coplanar_i(x ,y):
	r = np.hypot(x, y)
	I = x * np.log(r + y) + y * np.log(r + x)
	return I
def hitoshi(Lx ,Ly,x0,y0,z):
	I = hitoshi_i(x0+Lx/2, y0+Ly/2, z) - hitoshi_i(x0+Lx/2, y0-Ly/2, z)
	J = hitoshi_i(x0-Lx/2, y0-Ly/2, z) - hitoshi_i(x0-Lx/2, y0+Ly/2, z)
	return (I+J)/(Lx*Ly) * k0
def hitoshi_coplanar(Lx ,Ly,x0,y0):
	I = hitoshi_coplanar_i(x0+Lx/2, y0+Ly/2) - hitoshi_coplanar_i(x0+Lx/2, y0-Ly/2)
	J = hitoshi_coplanar_i(x0-Lx/2, y0-Ly/2) - hitoshi_coplanar_i(x0-Lx/2, y0+Ly/2)
	return (I+J)/(Lx*Ly)*k0
def orion(Lx, Ly):
	II =  1/Lx * np.arcsinh(Lx / Ly) + 1/Ly * np.arcsinh(Ly / Lx) + \
	(Lx / Ly**2 + Ly / Lx**2 - (1 / Lx**2 + 1 / Ly**2) * np.hypot(Lx,Ly) )/3
	return II * 2 * k0
def zho(Lx ,Ly,x0,y0,z):
	return 1/np.sqrt(x0**2 + y0**2 + z**2)*k0 
def zho_coplanar(Lx ,Ly,x0,y0):
	C = np.logical_and(x0 == 0, y0 == 0)
	Cn = np.logical_not(C)
	I2 = np.zeros_like (x0)
	I2 [C] = orion(Lx, Ly)
	I2[Cn] = 1/np.sqrt(x0[Cn]**2 + y0[Cn]**2)*k0 
	return I2
