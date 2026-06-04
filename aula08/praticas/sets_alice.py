t = (0, 1, 1, 2, 3, 5)
l = [0, 1, 1, 2, 3, 5]

numeros = set()

numeros.add(1)
numeros.add(2)
numeros.add(1)
numeros.add(3)
numeros.add(2)
numeros.add(2)
numeros.add(0)

print(sorted(numeros))

votos = ['aaa', 'bbb', 'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'bbb', 'bbb', 'aaa']

candidatos_unicos = set(votos)
print(candidatos_unicos) #set nao respeita a ordem dos elementos

for candidato in candidatos_unicos:
    print(candidato, votos.count(candidato))

candidatos_unicos.remove('bbb')
print(candidatos_unicos)

