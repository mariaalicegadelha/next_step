#Problema 1

lista_numeros = []

'''for i in range(0, 5):
    N = int(input())
    lista_numeros.append(N)

print(max(lista_numeros))'''

#Problema 2 

'''for i in range(1, 51):
    if i % 2 != 0:
        print(i)'''

#Problema 3

'''N = int(input())

for i in range(0, 11):
    numero = N * i
    print(f'{N} x {i} = {numero}')'''

#Problema 4

'''lista_numeros = []

for i in range(0, 10):
    numeros = int(input())
    lista_numeros.append(numeros)

print(f'O maior número é {max(lista_numeros)} e sua posição é {lista_numeros.index(max(lista_numeros))}')'''

#Problema 5

while (True):
    nota = int(input())
    print(f'Você digitou {nota}')
    if nota > 10 or nota < 0:
        print('Valor inválido')
    else:
        break
