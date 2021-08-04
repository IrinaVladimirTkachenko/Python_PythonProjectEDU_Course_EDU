class Rectangle ():
	def __init__ (self, a, b) :
		self.width = a
		self.len = b
		
	def calculate_perimeter (self) :
		return 2 * (self.width + self.len)
		
rectangle = Rectangle (5, 10)
print (rectangle.calculate_perimeter ())

class Square ():
	def __init__ (self, a) :
		self.storona = a
		
    		return 4 * self.storona
		
	def change_size (self, a):
		self.storona = a
		
square = Square (2)
print (square.calculate_perimeter ())
square.change_size (-8)
print (square.calculate_perimeter ())
	
