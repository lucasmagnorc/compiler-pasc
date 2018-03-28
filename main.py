
with open("pasC1.txt") as file:
	program = "program"
	while True:
		c = file.read(1)
		for item in c:
			if c.isalpha():
				print (c)
		if not c:
			print("End of file")
			break
		
