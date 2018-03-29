class symbolTable(object):
    symbolTable = []

    def __init__(self):
        self.symbolTable.append(["KW","program",0,0])
        self.symbolTable.append(["KW","if",0,0])
        self.symbolTable.append(["KW","else",0,0])
        self.symbolTable.append(["KW","while",0,0])
        self.symbolTable.append(["KW","write",0,0])
        self.symbolTable.append(["KW","read",0,0])
        self.symbolTable.append(["KW","num",0,0])
        self.symbolTable.append(["KW","char",0,0])
        self.symbolTable.append(["KW","not",0,0])
        self.symbolTable.append(["KW","or",0,0])
        self.symbolTable.append(["KW","and",0,0])
        
    def addSymbolTable(self, word, row, column):
        self.symbolTable.append(["ID", word, row, column])

    def __str__(self):
        string = ""
        for i in range(0,len(self.symbolTable)):
            string += "Token: <"+self.symbolTable[i][0]+", \""+self.symbolTable[i][1]+"\">\tRow: "+str(self.symbolTable[i][2])+"\tColumn: "+str(self.symbolTable[i][3])+"\n"
        return string
