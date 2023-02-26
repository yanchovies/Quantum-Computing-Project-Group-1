class MatrixElement:
	def __init__(self, i, j, value):
		self.i = int(i)
		self.j = int(j)
		self.value = value

	def __str__(self):
		return self.value
	
	def __float__(self):
		try:
			return float(self.value)
		except ValueError:
			raise ValueError("Invalid matrix element: " + str(self.value))
