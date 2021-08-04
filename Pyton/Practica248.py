class Shape ( ):
  	def __init__(self, w, l):
  		self.width = w
  		self.len = l
  	
  	def what_am_i (self):
  		print ("""Я {} - фигура {}""" .format (self.width, self.len))
  		                           
class Square (Shape):
	pass
	
a_square = Square (40, 40)
a_square.what_am_i()

class Rectangle (Shape):
	pass
	
a_rectangle = Rectangle (50, 80)
a_rectangle.what_am_i ()
  		         
  		         
