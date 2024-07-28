def f(*arg):
	print (arg)
	print (type(arg))
	# ~ print (type(*arg))
	print (*arg)
f('0', 1)
a = [2,1]
print (*a)
print (a)
g = lambda x: x*2
print (g(8))
h = lambda *args : None
h()
