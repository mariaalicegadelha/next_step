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
while True:
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
        break
