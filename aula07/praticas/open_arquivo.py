try:
    nome_arquivo = input('Insira o nome do arquivo: ')
    with open(nome_arquivo, encoding='UTF-8') as arq:
        print(arq.read())
except FileNotFoundError as erro:
    print(f'Deu erro: {type(erro).__name__}')
    print('O arquivo está sendo criado')
    novo_arq = open(nome_arquivo, 'w')
    novo_arq.close()
else:
    print('nada errado')
finally:
    print('Acabou o programa')