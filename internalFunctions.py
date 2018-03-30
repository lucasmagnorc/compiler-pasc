from tokens import token
from symbolTable import symbolTable

Ts = symbolTable()
row = 0
column = 0
state = 1
lexem = ''

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

def switch_demo(current):
    global state
    global lexem
    global row
    global column
    while 1:
        if state == 1:
            if current == ' ' or current == '\t' or current == '\n' or current == '\r':
                break
            elif current.isdigit():
                lexem += current
                state = 13
                break
            elif current.isalpha():
                lexem += current
                state = 16
                break
            elif current == '=':
                state = 2
                break
            elif current == '!':
                state = 3
                break
            elif current == '>':
                state = 4
                break
            elif current == '<':
                state = 5
                break
            elif current == '+':
                state = 1
                return token("OP_AD", "+", row, column)
            elif current == '-':
                state = 1
                return token("OP_MIN", "-", row, column)
            elif current == "*":
                state = 1
                return token("OP_MUL", "*", row, column)
            elif current == ';':
                state = 1
                return token("SMB_SEM", ";", row, column)
            elif current == ',':
                state = 1
                return token("SMB_COM", ",", row, column)
            elif current == '(':
                state = 1
                return token("SMB_OPA", "(", row, column)
            elif current == ')':
                state = 1
                return token("SMB_OPA", ")", row, column)
            elif current == '{':
                state = 1
                return token("SMB_CBC", "{", row, column)
            elif current == '}':
                state = 1
                return token("SMB_CBC", "}", row, column)
            elif current == "'":
                lexem += current
                state = 6
                break
            elif current == '"':
                lexem += current
                state = 8
                break
            elif current == '/':
                state = 9
                break
            else:
                state = 1
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        if state == 2:
            if current == '=':
                state = 1
                return token("OP_EQ", "==", row, column)
            else:
                state = 1
                return token("OP_ASS", "=", row, column)

        if state == 3:
            if current == '=':
                state = 1
                return token("OP_NE", "!=", row, column)
            else:
                state = 1
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        if state == 4:
            if current == '=':
                state = 1
                return token("OP_GE", ">=", row, column)
            else:
                state = 1
                return token("OP_GT", ">", row, column)

        if state == 5:
            if current == '=':
                state = 1
                return token("OP_LE", "<=", row, column)
            else:
                state = 1
                return token("OP_LT", "<", row, column)


        if state == 6:
            if current.isalpha:
                lexem += current
                state = 7
                break
            else:
                state = 1
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        # Estado final char
        if state == 7:
            if current == "'":
                lexem += current
                state = 1
                return token("CON_CHAR", lexem, row, column)
            else:
                state = 1
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        # Estado final para string
        if state == 8:
            if current == '"':
                lexem += current
                state = 1
                tokenHelper = token("LIT", lexem, row, column)
                lexem = ''
                return tokenHelper
            else:
                lexem += current
                state = 8
                break

        if state == 9:
            if current == '/':
                state = 10
                break
            elif current == '*':
                state = 11
                break
            else:
                state = 1
                return token("OP_DIV", "/", row, column)

        # Estado final para comentário //
        if state == 10:
            if current != '\n':
                state = 10
                break
            else:
                state = 1

        if state == 11:
            if current == '*':
                state = 12
                break
            else:
                state = 11;
                break

        # Estado final para comentário /* */
        if state == 12:
            if current == '/':
                state = 1
                break
            else:
                state = 11
                break

        # Estado final para digito
        if state == 13:
            if current.isdigit():
                lexem += current
                state = 13
                break
            elif current == '.':
                lexem += current
                state = 14
                break
            else:
                state = 1
                tokenHelper = token("CON_NUM", lexem, row, column)
                lexem = ''
                return tokenHelper

        if state == 14:
            if current.isdigit():
                lexem += current
                state = 15
                break
            else:
                state = 1
                lexem = ''
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        # Estado final para número decimal
        if state == 15:
            if current.isdigit():
                lexem += current
                state = 15
                break
            else:
                state = 1
                tokenHelper = token("CON_NUM", lexem, row, column)
                lexem = ''
                return tokenHelper
   
        # Estado final para Letras
        if state == 16:
            if current.isalpha() or current.isdigit():
                lexem += current
                state = 16
                break
            else:
                state = 1
                tokenHelper = token("ID", lexem, row, column)
                lexem = ''
                return tokenHelper


textArq = openFile("pasC1.txt")
for line in textArq:
    i = 0
    while i < len(line):
        if line[i] == '\t':
            column +=3
        elif line[i] == '\n' or line[i] == '\r':
            row += 1
            column = 0
        else:
            column += 1
        tokenHelper = switch_demo(line[i])
        if tokenHelper != None:
            if tokenHelper.getTag() == "ID":
                print(Ts.getToken(tokenHelper))
            elif tokenHelper.getTag() == "CON_NUM":
                print(tokenHelper)
            else:
                i += 1
                print(tokenHelper)
        else:
            i += 1
print(token("EOF", "EOF", row, column+1))
