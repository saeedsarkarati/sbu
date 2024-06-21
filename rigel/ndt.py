import sys
printflag = True
if printflag:
	sprint = print
else:
	sprint = lambda *args: None

from parallel import *
from perpendicular import *

a = np.arange(10)
print (a)
b = np.arange(10,20)
print (b)
# ~ b=a*2
def m(x,y,n):
	y[:n] = x[:n] * 2
m(a[2:],b[2:],2)
print(b, b.size)
b = np.delete(b, [1])
print (b, b.size)
print (b[1:3])
x = np.arange(1,3)
print (b[x])
sys.exit()
import plates
