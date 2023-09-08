import numpy as np
f = open ("cuberesults.txt", "r")
d = f.read()
f.close()
print (d)
e = d.split()
f=[]
for i in e:
	f.append(float(i))
f = np.array(f)
print (f)
f = f.reshape((f.size//3, 3 ))
print (f[:,2])

import matplotlib.pyplot as plt
plt.plot(f[:,2])
plt.ylabel('Capacitance of Unit Cube')
plt.xlabel('1d segmentation number')
plt.show()
