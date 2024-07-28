from parallel import *
gap = 0.02
z = 1e-2
lc = 0.1
u_lx = lc
u_ly = lc

Iuu = parallel_coplanar(lc, lc, lc, lc, 0, 0)
print ('parallel coplanar normal %e' %Iuu)

Iuu = parallel_coplanar(lc*10, lc*10, lc*10, lc*10, 0, 0)
print ('parallel coplanar normal %e' %Iuu)

Iuu = parallel_coplanar(lc/2, lc/2, lc/2, lc/2, 0, 0)
print ('parallel coplanar normal %e' %Iuu)

Iuu = parallel_coplanar(10*lc, 10*lc, lc/2, lc/2, 0, 0)
print ('parallel coplanar normal %e' %Iuu)



Iu = parallel(lc, lc, 10*lc, 10*lc, lc/2+gap/2, 0, z)
print ('paralel %e' %Iu)

Iu = parallel(lc, lc, lc/2, lc/2, lc/2+gap/2, 0, z)
print ('paralel %e' %Iu)

Iu = parallel(lc, lc, 10*lc, 10*lc, lc*10, 0, z)
print ('paralel %e' %Iu)
