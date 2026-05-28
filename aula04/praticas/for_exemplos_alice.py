''' frutas = ['maçã', 'banana', 'laranja', 'uva', 'ração', 'desodorante']


i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

for item in frutas:
    print(item)


idades = [19, 45, 30, 35, 33, 13, 67, 22]

for idade in idades:
    if idade > 35:
        print(idade)


nome_completo = input('Insira o seu nome completo: ')

for letra in nome_completo:
    print(letra)

for palavra in nome_completo.split():
    print(palavra)

for _ in range(10):
     print('eita')

notas = []

quant_notas = int(input('Quantas notas você quer ler? '))

for _ in range(quant_notas):
    nota = float(input('Insira uma nota: '))
    notas.append(nota)

print(notas)

media = sum(notas) / len(notas)
print(media)

for num in range(1, 101):
    if num % 2 == 0:
        print(num)

for num in range(2, 101, 2):
    print(num)

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for elemento in matriz:
    for item in elemento:
        print(item)

print(matriz[2][1])

print(len(matriz))

nomes_original = ['Miguel', 'Arthur', 'Heitor', 'Helena', 'Alice', 'Laura', 'Gabriel', 'Davi', 'Maria Clara', 'Pedro', 'Yoda', 'Caio']
nomes_selecionados = []

for nomes in nomes_original:
    if len(nomes) <= 5:
        nomes_selecionados.append(nomes)
        #nomes_original.remove(nomes) 

print(nomes_selecionados)'''

x = int(input())

for num in range(1, x + 1):
    if num % 2 != 0:
        print(num)

n = int(input())

for num in range(1, 10001):
    if num % n == 2:
        print(num)    