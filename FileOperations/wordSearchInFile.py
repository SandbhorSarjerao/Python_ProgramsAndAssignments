f = open("MyData.txt")

list_line = f.readlines()

for myline in list_line:
	if "SARJERAO" in myline.lower():      # if "error" in myline.lower():
		print(myline)

f.close()