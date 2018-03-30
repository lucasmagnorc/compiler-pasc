from tokens import token
from symbolTable import symbolTable

Ts = symbolTable()
row = 0
column = 0
state = 1

# Função para ler o arquivo texto, e retornar um erro caso não abra
def openFile(nameFile):
    try:
        file = open(nameFile, 'r')
        textArq = file.readlines()
        return textArq
    except IOError:
        print("Erro ao abrir o arquivo")

def nextToken(textArq):
    for line in textArq:
        for word in line:
            print(word)

def switch_demo(current, row, column):
    global state
    global lexem
    while 1:
        if state == 1:
            if current == ' ' or current == '\t' or current == '\n' or current == '\r':
                break
            elif current.isdigit():
                lexem += current
                state = 
                break
            elif current.isalpha():
                lexem += current
                state = 
                break
            elif current == '=':
                state = 2
                break
            elif current == '!':
                state = 5
                break
            elif current == '>':
                state = 7
                break
            elif current == '<':
                state = 10
                break
            elif current == '+':
                state = 13
                break
            elif current == '-':
                state = 14
                break
            elif current == "*":
                state = 15
                break
            elif current == ';':
                state = 16
                break
            elif current == ',':
                state = 17
                break
            elif current == '(':
                state = 18
                break
            elif current == ')':
                state = 19
                break
            elif current == '{':
                state = 20
                break
            elif current == '}':
                state = 21
                break
            elif current == "'":
                lexem += current
                state = 22
                break
            elif current == '"':
                state = 24
                break
            elif current == '/':
                state = 26
                break
            
            else:
                return str("Unknown character: [" + current + "]", row, column)
                break
                
        if state == 2:
            if current == '=':
                state = 3
                break
            else:
                state = 4
                break
        
        # Estado final '=='
        if state == 3:
            return token("OP_EQ", "==", row, column)
        
        # Estado final '='
        if state == 4:
            return token("OP_ASS", "=", row, column)
        
        if state == 5:
            if current == '='
                state = 6
                break
            else:
                return str("Unknown character: [" + current + "]", row, column)
            
        # Estado final '!='
        if state == 6:
            return token("OP_NE", "!=", row, column)
            
        if state == 7:
            if current == '=':
                state = 8
                break
            else:
                state = 9
                break
        
        # Estado final '>='
        if state == 8:
            return token("OP_GE", ">=", row, column)
            
        # Estado final '>'
        if state == 9:
            return token("OP_GT", ">", row, column)            
        
        if state == 10:
            if current == '=':
                state = 11
                break
            else:
                state = 12
                break
                
        # Estado final '<='
        if state == 11:
            return token("OP_LE", "<=", row, column)
        
        # Estado final '<'
        if state == 12:
            return token("OP_LT", "<", row, column)            
        
        # Estado final '+'
        if state == 13:
            return token("OP_AD", "+", row, column)
            
        # Estado final '-'
        if state == 14:
            return token("OP_MIN", "-", row, column)
            
        # Estado final '*'
        if state == 15:
            return token("OP_MUL", "*", row, column)

        # Estado final ';'
        if state == 16:
            return token("SMB_SEM", ";", row, column)

        # Estado final ','
        if state == 17:
            return token("SMB_COM", ",", row, column)
            
        # Estado final '('
        if state == 18:
            return token("SMB_OPA", "(", row, column)
            
        # Estado final ')'
        if state == 19:
            return token("SMB_OPA", ")", row, column)
        
        # Estado final '{'
        if state == 20:
            return token("SMB_CBC", "{", row, column)
            
        # Estado final '}'
        if state == 21:
            return token("SMB_CBC", "}", row, column)

        if state == 22:
            if current.isalpha:
                lexem += current
                state = 23
                break
            else:
                return str("Unknown character: [" + current + "]", row, column)
        
        # Estado final char
        if state == 23:
            if current == "'":
                lexem += current
                return token("CON_CHAR", lexem, row, column)
             else:
                return str("Unknown character: [" + current + "]", row, column)

        if state == 24:
            if current == '":
                lexem += current
                state = 25
                break
            else:
                lexem += current
                state = 24
                break

        # Estado final para string
        if state == 25:
            return token("LIT", current, row, column)

        if state == 26:
            if current == '/':
                state = 27
                break
            elif current = '*':
                state = 28
                break
            elif current.isdigit():
                state = ESTADO DO NUMERO
                break
            else:
                return str("Unknown character: [" + current + "]", row, column)

        # Estado final para comentário //
        if state == 27:
            if current == '\n':
                state = 1
                break
        
        if state == 28:
            if current == '*':
                state = 29
                break
        
        # Estado final para comentário /* */
        if state == 29:
            if current == '/':
                state = 1
                break
            else:
                state = 28
                break

        # Estado final Variável
        if state == 30:
            if current.isalpha or current.isdigit:
                state = 30
            else:
                return token()

lexem = ''
textArq = openFile("pasC1.txt")
for line in textArq:
    row += 1
    column = 0
    for char in line:
        column += 1
        tokenHelper = switch_demo(char, row, column)
        if tokenHelper != None:
            print(tokenHelper)
print(token("EOF", "EOF", row, column))
