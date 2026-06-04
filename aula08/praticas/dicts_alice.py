palavras_ing = ['dog', 'lion', 'cat', 'tiger']

dicionarios = {
    'cachorro': 'dog',
    'leao': 'lion',
    'gato': 'cat',
    'tigre': 'tiger'
}

print(dicionarios['tigre'])


enderecos = {
    '52021220': ['Rua Dr Geraldo de Andrade', '75', 'Drogasil'],
    '56310222': ['Rue des Yuccas', '190', 'LIDL']
} #as chaves podem ser de qualquer tipo

print(dicionarios)
print(enderecos)

dados = dict()

dados['bear'] = 'urso'

'''for _ in range(3):
    chave, valor = input('Insira chave e valor: ').split()
    dados[chave] = valor'''

#print(dados)

infos = [('monkey', 'macaco'), ('rabbit', 'coelho'), ('fish', 'peixe')]
dados.update(infos)
print(dados)

removido = dados.pop('rabbit')
print(dados)
print(removido)

dados.popitem() #remove o ultimo elemento

'''dados.clear()
print(dados)'''

print(dados.get('wolf', 'Animal não encontrado'))

print(dados.keys())

print(dados.values())

print(dados.items())

for chave, coisa in dados.items():
    print(f'{chave} - {coisa}')