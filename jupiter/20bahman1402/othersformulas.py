#Coupling Coeffitients in old formulas
import numpy as np
k0 = 9e9
e0 = 1 / (4 * np.pi * k0)
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

	Ih = hitoshi(Lx, Ly, d, 0, z)
	print ('hitoshi %e' %Ih)
