import csv

with open ("tv.csv", "w") as f:
	  w = csv.writer (f,
	                       delimiter=",")
	  w.writerow (["Звездные войны", 
	                    "Терминатор", 
	                    "Искусственный интеллект"])
	  w.writerow (["Дурак", 
	                    "Матильда", 
	                    "Левиафан"])
	  w.writerow (["Люди в черном", 
	                    "Я - робот", 
	                    "Эволюция"])
	          
	     