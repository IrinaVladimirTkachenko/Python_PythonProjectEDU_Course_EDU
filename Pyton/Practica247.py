import math

class Circle ( ) :
	def __init__ (self, r) :
		self.radius = r
		
	def area (self) :
			return math.pi * self.radius ** 2
			
	def change_size (self, r) :
			self.radius = r
			
circle = Circle (10)
print (circle.area ( ) )
circle.change_size (20)
print (circle.area ( ) )

a = input ("введите число:")
a = int (a)
circle.change_size (a)
print (circle.area ( ) )
