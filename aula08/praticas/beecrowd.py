#Problema DDD

'''dict_ddd = {61: 'Brasilia',
            71: 'Salvador',
            11: 'Sao Paulo',
            21: 'Rio de Janeiro',
            32: 'Juiz de Fora',
            19: 'Campinas',
            27: 'Vitoria',
            31: 'Belo Horironte'
        }

ddd = int(input())


if ddd not in dict_ddd:
    print('DDD nao cadastrado')
else:
    print(dict_ddd.get(ddd))'''

#Problema LED

'''dict_leds = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}
while True:
    try:

        test_case = int(input())
        lista_numeros = []

        for _ in range(test_case):
            numeros = input()
            lista_numeros.append(numeros)

        for num in lista_numeros:
            leds = 0
            for digito in num:
                leds += dict_leds[digito]
            print(f'{leds} leds')
    except EOFError:
        break'''

#Problema 3

'''dict_animais = {
    'aguia': ['vertebrado', 'ave', 'carnivoro'],
    'pomba': ['vertebrado', 'ave', 'onivoro'],
    'homem': ['vertebrado', 'mamifero', 'onivoro'],
    'vaca':  ['vertebrado', 'mamifero', 'herbivoro'],
    'pulga': ['invertebrado', 'inseto', 'hematofago'],
    'lagarta': ['invertebrado', 'inseto', 'herbivoro'],
    'sanguessuga': ['invertebrado', 'anelideo', 'hematofago'],
    'minhoca': ['invertebrado', 'anelideo', 'onivoro'],
}

mapa_animais = []

for _ in range(3):
    palavras = input()
    mapa_animais.append(palavras)

for animais, descricao in dict_animais.items():
    if descricao == mapa_animais: 
        print(animais)'''

#Problema 4

'''pares = []
impares = []

for _ in range(15):
    n = int(input())

    if n % 2 == 0:
        pares.append(n)

        if len(pares) == 5:
            for i, valor in enumerate(pares):
                print(f'par[{i}] = {valor}')
            pares = []

    else:
        impares.append(n)

        if len(impares) == 5:
            for i, valor in enumerate(impares):
                print(f'impar[{i}] = {valor}')
            impares = []

# imprime o restante dos ímpares
for i, valor in enumerate(impares):
    print(f'impar[{i}] = {valor}')

# imprime o restante dos pares
for i, valor in enumerate(pares):
    print(f'par[{i}] = {valor}')'''

#Problema 5


lista_joias = []

while True:
    try:
        joia = input()
        lista_joias.append(joia)

    except EOFError:
        break

print(len(set(lista_joias)))