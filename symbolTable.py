from tokens import token


class symbolTable(object):
    symbolTable = []

    # Método construtor
    def __init__(self):
        self.symbolTable.append(token("KW","program",0,0))
        self.symbolTable.append(token("KW","if",0,0))
        self.symbolTable.append(token("KW","else",0,0))
        self.symbolTable.append(token("KW","while",0,0))
        self.symbolTable.append(token("KW","write",0,0))
        self.symbolTable.append(token("KW","read",0,0))
        self.symbolTable.append(token("KW","num",0,0))
        self.symbolTable.append(token("KW","char",0,0))
        self.symbolTable.append(token("KW","not",0,0))
        self.symbolTable.append(token("KW","or",0,0))
        self.symbolTable.append(token("KW","and",0,0))

    # Método para adicionar um símbolo na tabela
    def addSymbolTable(self, newToken):
        self.symbolTable.append(newToken)

    # Método para retornar se um token existe
    def getToken(self, tokenAux):
        for tsToken in self.symbolTable:
            if tokenAux.getValue() == tsToken.getValue():
                return tsToken
        return tokenAux

    # Método para retornar a tabela de símbolos
    def __str__(self):
        string = ""
        for tsToken in self.symbolTable:
            string += "Token: <" + tsToken.getTag(
            ) + ", \"" + tsToken.getValue() + "\">\tRow: " + tsToken.getRow(
            ) + "\tColumn: " + tsToken.getColumn() + "\n"
        return string
