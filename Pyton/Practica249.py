class Horse ():
	def __init__(self,
	                    name, 
	                    owner) :
		self.name = name
		self.owner = owner
		
class Rider ():
	def __init__ (self, name):
		self.name = name
		
mike = Rider ("Майкл Деним")
rich = Horse ("Ричард",
                      mike)
print (rich.owner.name)
                      
