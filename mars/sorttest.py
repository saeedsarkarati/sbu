import numpy as np
a = np.array([1,1,11])
b = np.array([100,10,8])
c = np.array([1,7,80])
x = np.array([a, b, c])
print (x)
print ('----------')
x.sort(axis = 0)
print(x)
print ('----------')
a = x[0]
b = x[1]
c = x[2]
print (a)
print (b)
print (c)
ii = np.array([[0, 2, 0, 2], [2, 0, 2, 0], [0, 2, 0, 2], [2, 0, 2, 0]])
jj = np.array([[0, 0, 2, 2], [0, 0, 2, 2], [2, 2, 0, 0], [2, 2, 0, 0]])
x = np.array([ii,jj])
print (x)
print ('++++++++++----------')
x.sort(axis = 0)
print(x)
print ('+++++++++++++----------')
ii = x[0]
jj = x[1]
print (ii)
print (jj)



