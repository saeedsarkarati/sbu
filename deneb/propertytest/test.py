class RV:
    def __init__(self, x):
        self._x = x 
        self._y = x * 2  # Initial relationship

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value * 1.0
        self._y = value * 2.0  # Update y when x changes

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value *1.0
        self._x = value / 2  # Update x when y changes
class oo:
	def __init__(self):
		self.xx = 0;
	@property
	def x(self):
		return self.xx
	@x.setter
	def x(self, v):
		self.xx = v
# Example usage
ss = RV(10)
print(ss.x, ss.y)  # Output: 0 20

ss.x = 20
print(ss.x, ss.y)  # Output: 20 40

ss.y = 50
print(ss.x, ss.y)  # Output: 25 50
q = oo()
q.x = 10
print (q.x)
