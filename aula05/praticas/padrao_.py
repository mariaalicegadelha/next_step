print(1, 2, 3, 'eita', True, sep=', ', end=' acabou ')
print(2, 8)

def velocidade(distancia, tempo=2):
    print(distancia / tempo)

velocidade(100, 3)
velocidade(50) #vai pegar tempo padrao = 2

def acai(*toppings, tamanho='P'): #esse * me deixa colocar quantos itens eu quiser
    for item in toppings:    #nao estimei valor para toppings, mas preciso passar valor default para a proxima variavel
        print(f' - {item}')
    print(f' - {tamanho}')
acai('Banana', 'Granola', 'Leite ninho')
acai('Banana', tamanho='G')
acai('Jujuba', tamanho='M')

