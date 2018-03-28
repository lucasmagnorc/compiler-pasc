from tokens import token

def openFile(nameFile):
	file = open(nameFile, 'r')
	textArq = file.readlines()

openFile("pasC1.txt")

tokenTeste = token("EOF", "EOF", 0, 21)

print(str(tokenTeste))

