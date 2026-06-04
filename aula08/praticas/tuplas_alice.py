dias_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')

#dias_semana.pop(0) # pop não existe em tupla, por ser imutável

print(type(dias_semana), dias_semana)

print(dias_semana[0])

print(dias_semana[-1])

print(dias_semana.index('terça'))

#dias_semana[1] = 'domingo' nao podemos modificar

numeros = [1, 2, 3, 6, 4, 36, 9]

numeros_imutaveis = tuple(numeros)

print(numeros_imutaveis)

numeros_ordenados = sorted(numeros_imutaveis) #o sorted retorna um elemento novo

print(numeros_ordenados)

'''def sorted_mutavel(lista):
    lista.append('eita')

def sorted_normal(lista):
    nova_lista = lista.copy()
    nova_lista.append()
    return nova_lista'''
