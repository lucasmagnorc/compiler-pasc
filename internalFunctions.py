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
                state = 30
                break
            elif current.isalpha():
                lexem += current
                state = 33
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
                state = 1
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        if state == 2:
            if current == '=':
                state = 3
                break
            else:
                state = 1
                return token("OP_ASS", "=", row, column)

        # Estado final '=='
        if state == 3:
            state = 1
            return token("OP_EQ", "==", row, column)

        if state == 5:
            if current == '=':
                state = 6
                break
            else:
                state = 1
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        # Estado final '!='
        if state == 6:
            state = 1
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
            state = 1
            return token("OP_GE", ">=", row, column)

        # Estado final '>'
        if state == 9:
            state = 1
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
            state = 1
            return token("OP_LE", "<=", row, column)

        # Estado final '<'
        if state == 12:
            state = 1
            return token("OP_LT", "<", row, column)

        # Estado final '+'
        if state == 13:
            state = 1
            return token("OP_AD", "+", row, column)

        # Estado final '-'
        if state == 14:
            state = 1
            return token("OP_MIN", "-", row, column)

        # Estado final '*'
        if state == 15:
            state = 1
            return token("OP_MUL", "*", row, column)

        # Estado final ';'
        if state == 16:
            state = 1
            return token("SMB_SEM", ";", row, column)

        # Estado final ','
        if state == 17:
            state = 1
            return token("SMB_COM", ",", row, column)

        # Estado final '('
        if state == 18:
            state = 1
            return token("SMB_OPA", "(", row, column)

        # Estado final ')'
        if state == 19:
            state = 1
            return token("SMB_OPA", ")", row, column)

        # Estado final '{'
        if state == 20:
            state = 1
            return token("SMB_CBC", "{", row, column)

        # Estado final '}'
        if state == 21:
            state = 1
            return token("SMB_CBC", "}", row, column)

        if state == 22:
            if current.isalpha:
                lexem += current
                state = 23
                break
            else:
                state = 1
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        # Estado final char
        if state == 23:
            if current == "'":
                lexem += current
                state = 1
                return token("CON_CHAR", lexem, row, column)
            else:
                state = 1
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        # Estado final para string
        if state == 24:
            if current == '"':
                lexem += current
                state = 1
                tokenHelper = token("LIT", lexem, row, column)
                lexem = ''
                return tokenHelper
            else:
                lexem += current
                state = 24
                break

        if state == 26:
            if current == '/':
                state = 27
                break
            elif current == '*':
                state = 28
                break
            else:
                state = 1
                return token("OP_DIV", "/", row, column)

        # Estado final para comentário //
        if state == 27:
            if current == '\n':
                state = 1
                break

        if state == 28:
            if current == '*':
                state = 29
                break
            else:
                state = 28;
                break

        # Estado final para comentário /* */
        if state == 29:
            if current == '/':
                state = 1
                break
            else:
                state = 28
                break

        # Estado final para digito
        if state == 30:
            if current.isdigit():
                lexem += current
                state = 30
                break
            elif current == '.':
                lexem += current
                state = 31
                break
            else:
                state = 1
                tokenHelper = token("CON_NUM", lexem, row, column)
                lexem = ''
                return tokenHelper

        if state == 31:
            if current.isdigit():
                lexem += current
                state = 32
                break
            else:
                state = 1
                lexem = ''
                print("Unknown character: [" + str(current) + "]", str(row), str(column))
                break

        # Estado final para número decimal
        if state == 32:
            if current.isdigit():
                lexem += current
                state = 32
                break
            else:
                state = 1
                tokenHelper = token("CON_NUM", lexem, row, column)
                lexem = ''
                return tokenHelper
        # Estado final para Letras
        if state == 33:
            if current.isalpha() or current.isdigit():
                lexem += current
                state = 33
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
print(token("EOF", "EOF", row, column))
