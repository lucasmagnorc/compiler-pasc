from tokens import token
from symbolTable import symbolTable

def openFile(nameFile):
	file = open(nameFile, 'r')
	textArq = file.readlines()

openFile("pasC1.txt")

ts = symbolTable()

print(str(ts))

