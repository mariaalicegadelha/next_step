try:
    num1 = int(input('Insira um número: '))
    num2 = int(input('Insira um outro número: '))
    resultado = num1 / num2
    print(resultado)

except (ZeroDivisionError, FileNotFoundError):
    print('Não podemos dividir número por 0')

#except ValueError:
    #print('Erro: Você deve digitar um número.')

except Exception as erro: #geral
    print(f'{type(erro).__name__}')
    print('Algo deu errado no seu código.')
print('acabou')