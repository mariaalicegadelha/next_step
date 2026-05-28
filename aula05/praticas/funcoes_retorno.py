def velocidade(distancia, tempo):

    velocidade = distancia / tempo

    return velocidade

def avaliar_multa():
    velo = velocidade(120, 2)
    if velo > 50:
        print('Multa')
    else:
        print('Ok')

avaliar_multa()

def muda_nome(primeiro_nome, segundo_nome):
    primeiro_nome = primeiro_nome.capitalize()
    segundo_nome = segundo_nome.capitalize()

    return f'{primeiro_nome} {segundo_nome}'

nome_completo = muda_nome('PEDRO', 'LINS')
print(nome_completo)

nomes = []

for _ in range(4):
    print('Cadastro do Nomes')
    primeiro_nome = input('Informe o primeiro nome: ')
    segundo_nome = input('Informe o segundo nome: ')
    nome_completo = muda_nome(primeiro_nome, segundo_nome)
    nomes.append(nome_completo)

print(nomes)