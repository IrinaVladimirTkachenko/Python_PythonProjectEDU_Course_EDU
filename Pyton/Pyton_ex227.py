import csv

with open ("st.csv", "w") as f:
    w = csv.writer(f,
	           delimiter=",")
    w.writerow (["odin",
	           "dva",
	           "tri"])
    w.writerow (["chetire",
	         "pyat",
	         "shest"])
	                     
