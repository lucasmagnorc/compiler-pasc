from tokens import token
from symbolTable import symbolTable
from ErrorMessage import ErrorMessage

# Variáveis globais (tabela de símbolos, linha, coluna, estado, lexema e contador)
Ts = symbolTable()
row = 0
column = 0
state = 1
lexem = ""
i = 0

# Função para ler o arquivo texto, e retornar um erro caso não abra
def openFile(nameFile):
    try:
        file = open(nameFile, 'r')
        textArq = file.readlines()
        return textArq
    except IOError:
        print("Erro ao abrir o arquivo")

# Função principal que identifica os tokens e erros
def structureOptions(current):
    # Definindo que as variáveis globais podem ser modificadas dentro do escopo
    global state
    global lexem
    global row
    global column
    global i

    # Loop infinito até que retorne um estado ou token
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

            # Retornando Token do símbolo de adição
            elif current == '+':
                state = 1
                return token("OP_AD", "+", row, column)

            # Retornando Token do símbolo de subtração
            elif current == '-':
                state = 1
                return token("OP_MIN", "-", row, column)

            # Retornando Token do símbolo de multiplicação
            elif current == "*":
                state = 1
                return token("OP_MUL", "*", row, column)

            # Retornando Token do símbolo de ponto e vírgula
            elif current == ';':
                state = 1
                return token("SMB_SEM", ";", row, column)

            # Retornando Token do símbolo de vírgula
            elif current == ',':
                state = 1
                return token("SMB_COM", ",", row, column)

            # Retornando Token do símbolo de abre parênteses
            elif current == '(':
                state = 1
                return token("SMB_OPA", "(", row, column)

            # Retornando Token do símbolo de fecha parênteses
            elif current == ')':
                state = 1
                return token("SMB_CPA", ")", row, column)

            # Retornando Token do símbolo de abre chaves
            elif current == '{':
                state = 1
                return token("SMB_OBC", "{", row, column)

            # Retornando Token do símbolo de fecha chaves
            elif current == '}':
                state = 1
                return token("SMB_CBC", "}", row, column)

            elif current == "'":
                state = 6
                break

            elif current == '"':
                state = 8
                break

            elif current == '/':
                state = 9
                break

            # Retornando Token de erro léxico
            else:
                state = 1
                return ErrorMessage("LEXIC ERROR", "Unknown character", row, column)
                break

        if state == 2:
            # Retonando Token do símbolo de igual igual
            if current == '=':
                state = 1
                return token("OP_EQ", "==", row, column)

            # Retornando Token do símbolo de atribuição igual
            else:
                state = 1
                i -= 1
                column -= 1
                return token("OP_ASS", "=", row, column)

        if state == 3:
            # Retornando Token do símbolo de diferente
            if current == '=':
                state = 1
                return token("OP_NE", "!=", row, column)

            # Retornando Token de erro léxico
            else:
                state = 1
                return ErrorMessage("LEXIC ERROR", "incomplete token", row, column)

        if state == 4:
            # Retornando Token do símbolo de maior igual
            if current == '=':
                state = 1
                return token("OP_GE", ">=", row, column)

            # Retornando Token do símbolo de maior
            else:
                state = 1
                i -= 1
                column -= 1
                return token("OP_GT", ">", row, column)

        if state == 5:
            # Retornando Token do símbolo de menor igual
            if current == '=':
                state = 1
                return token("OP_LE", "<=", row, column)

            # Retornando Token do símbolo de menor
            else:
                state = 1
                i -= 1
                return token("OP_LT", "<", row, column)

        if state == 6:
            if current.isalpha:
                lexem += current
                state = 7
                break

            # Retornando Token de erro léxico
            else:
                state = 1
                return ErrorMessage("LEXIC ERROR", "Expecting character", row, column)

        if state == 7:
            # Retornando Token de char
            if current == "'":
                state = 1
                tokenHelper = token("CON_CHAR", lexem, row, column)
                lexem = ''
                return tokenHelper

            # Retornando Token de erro léxico
            else:
                state = 1
                return ErrorMessage("LEXIC ERROR", "Expecting character", row, column)

        if state == 8:
            # Retornando Token de string
            if current == '"':
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
                state = 11
                break

        if state == 12:
            if current == '/':
                state = 1
                break
            elif current == '*':
                state = 12
                break
            else:
                state = 11
                break

        if state == 13:
            if current.isdigit():
                lexem += current
                state = 13
                break
            elif current == '.':
                lexem += current
                state = 14
                break

            # Retornando Token de um inteiro
            else:
                state = 1
                tokenHelper = token("CON_NUM", lexem, row, column)
                i -= 1
                column -= 1
                lexem = ''
                return tokenHelper

        if state == 14:
            if current.isdigit():
                lexem += current
                state = 15
                break

            # Retornando Token de um número decimal
            else:
                state = 1
                i -= 2
                column -= 2
                lexem = lexem.replace('.','')
                tokenHelper = token("CON_NUM", lexem, row, column)
                lexem = ''
                return tokenHelper

        if state == 15:
            if current.isdigit():
                lexem += current
                state = 15
                break

            # Retornando Token de um número decimal
            else:
                state = 1
                i -= 1
                column -= 1
                tokenHelper = token("CON_NUM", lexem, row, column)
                lexem = ''
                return tokenHelper

        if state == 16:
            if current.isalpha() or current.isdigit():
                lexem += current
                state = 16
                break

            # Retornando Token de uma variável
            else:
                state = 1
                tokenHelper = token("ID", lexem, row, column)
                lexem = ''
                return tokenHelper


textArq = openFile("pasC1.txt")

# Loop que percorre linha por linha do arquivo
for line in textArq:
    i = 0
    
    # Loop quer percorre caractere por caractere da linha 
    while i < len(line):
        
        # Verifica se o caractere é um tab e soma 3 a coluna
        if line[i] == '\t':
            column +=3
        
        # Verifica se o caractere é uma quebra de linha e soma 1 a linha e zera o valor da coluna
        elif line[i] == '\n' or line[i] == '\r':
            row += 1
            column = 0
       
        # Adiciona mais 1 a coluna
        else:
            column += 1

        # Chamando a funcão principal passando um caractere
        tokenHelper = structureOptions(line[i])

        # Testa se o token não está vazio
        if tokenHelper != None:
            # Se o token for do tipo ID, verifica se ele está na tabela de símbolos, se não estiver adiciona
            if tokenHelper.getTag() == "ID":
                print(Ts.getToken(tokenHelper))
                Ts.addSymbolTable(tokenHelper)
            
            # Verifica se o token tem um erro léxico e exibe ele
            elif tokenHelper.getTag() == "LEXIC_ERROR":
                print(tokenHelper)
            
            # Se não entrar nas outras condições apenas exibe
            else:
                i += 1
                print(tokenHelper)
        else:
            i += 1

# Exibe o token de final de arquivo
print(token("EOF", "EOF", row, column+1))
#print("\nTABELA DE SIMBOLOS")
#print(Ts)
