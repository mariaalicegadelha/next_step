#Problema 1

'''while True:
    try:
        N = input()

        lista_parenteses = []

        for c in N:
            if c == '(' or c == ')':
                lista_parenteses.append(c)

        saldo = 0
        erro = False

        for p in lista_parenteses:

            if p == '(':
                saldo += 1

            elif p == ')':
                saldo -= 1

            if saldo < 0:
                erro = True
                break

        if saldo != 0:
            erro = True

        if erro:
            print('incorrect')
        else:
            print('correct')

    except EOFError:
        break'''


#Problema 2

'''dict_santa = {'@': 'a',
              '&': 'e',
              '!': 'i',
              '*': 'o',
              '#': 'u'
}

while True:
    try:
        frase = input()

        for i in frase:
            if i in dict_santa:
                frase = frase.replace(i, dict_santa[i])
        print(frase)
    except EOFError:
        break'''

#Problema 3

'''while True:
    try:
        numeros = list(map(int, input().split()))


        if numeros[0] != numeros[1] and numeros[0] != numeros[2]:
            vencedor = 'A'
        elif numeros[1] != numeros[0] and numeros[1] != numeros[2]:
            vencedor = 'B'
        elif numeros[2] != numeros[0] and numeros[2] != numeros[1]:
            vencedor = 'C'
        elif numeros[0] == numeros[1] == numeros[2]:
            vencedor = '*'


        print(vencedor)

    except EOFError:
        break'''

#Problema 4
'''while True:
    try:
        L = int(input())

        numeros = list(map(int, input().split()))

        maior = max(numeros)

        if maior < 10:
            print(1)

        elif 10 <= maior < 20:
            print(2)

        else:
            print(3)

    except EOFError:
        break'''
