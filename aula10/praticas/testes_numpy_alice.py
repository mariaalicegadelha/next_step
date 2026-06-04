import numpy as np

#print(np.__version__)

notas = np.array([1.9, 10, 25, 1.4]) #ele vai reconhecer que existem floats, por isso ele converte todos p/ float

#print(notas)

lista = [14, 20, 12]

array = np.array([14, 20, 12])

#print(lista + [5]) #tipo append
#print(array + 5) #vetorizaçao

precos = np.array([100, 150, 200])

precos_com_desconto = precos * 0.9

#print(precos_com_desconto)

numeros = np.arange(0, 10, 2)
#print(numeros)

valores = np.ones((4, 5)) #vai criar arrays de 1

#print(valores)

intervalos = np.linspace(0, 10, 4)

#print(intervalos)

notas = np.array([
    [1.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 9.9]
])

'''print(notas.ndim)
print(notas.shape) #linhas e colunas
print(len(notas))
print(notas.dtype) #64 bytes

print(notas[-1][-1])
print(notas[:, 0])'''

'''print(notas + 1)
print(notas / 2)'''

'''notas_unidade_1 = np.array([7.0, 8.0, 6.0])
notas_unidade_2 = np.array([8.0, 7.5, 9.0])

media = (notas_unidade_1 + notas_unidade_2) / 2 #precisam ter o mesmo tamanho
print(media)'''

'''print(notas_unidade_1.mean())
print(notas_unidade_2.mean())
print(notas_unidade_1.sum())
print(notas_unidade_2.sum())
print(notas_unidade_1.std())
print(notas_unidade_2.std()) #desvio padrao
'''

'''turma_a = np.array([7.0, 7.1, 7.2, 7.0, 7.1])
turma_b = np.array([3.0, 5.0, 7.0, 9.5, 10.0])

print(turma_a.mean(), turma_a.std())
print(turma_b.mean(), turma_b.std())'''

turma = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [8.5, 5.6, 7.8],
    [7.5, 9.0, 9.0]
])


'''print(turma.mean())
print(turma.mean(axis=0)) #medias pelas colunas
print(turma.mean(axis=1)) #medias pelas linhas'''

'''notas = np.array([8.9, 5, 2, 8.4, 7.0])

print(notas >= 7)
print((notas >= 7).sum())
print(notas[notas >= 7])'''

nomes = np.array(['Ana', 'Breno', 'Carlos', 'Duda'])

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 5.0, 4.0],
    [9.5, 8.5, 10.0],
    [4.0, 5.6, 7.8],
])

medias = notas.mean(axis=1)
aprovados = medias >= 7
print(nomes[aprovados])
print(medias[aprovados])