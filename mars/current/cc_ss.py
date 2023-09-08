#Coupling Coeffitient
# ~ from scipy.special import erf
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
	return 1/np.sqrt(x0**2 + y0**2)*k0 	
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
	Io = orion(Lx, Ly)
	print ('orion %e' %Io)
	Isc = saeed_sc(Lx, Ly)
	print ('saeed self copling %e' %Isc, 'saeed_sc/orion',Isc / Io)

	Icp = saeed_coplanar(Lx, Ly, d, 0)
	print ('saeed coplanar %e' %Icp, 'saeed/orion',Icp / Io)

	Is = saeed(Lx, Ly, d, 0, z)
	print ('saeed %e' %Is, 'saeed/orion',Is / Io)

	Ih = hitoshi(Lx, Ly, d, 0, z)
	print ('hitoshi',Ih, 'saeed/hitoshi',Is/Ih)
