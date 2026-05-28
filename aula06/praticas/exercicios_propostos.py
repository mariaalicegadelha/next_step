i = 0
animais_terrestres = []

with open ('aula06/arquivo_animais.txt', 'w', encoding='UTF-8') as animais_habitat:
    n = int(input('Quantos animais vc quer analisar? '))
    for _ in range(n):
        animais, habitat = input('Insira o animal e seu habitat: ').strip().split(',')
        animais = animais.strip()
        habitat = habitat.strip()

        animais_habitat.write(f'{animais},{habitat}\n')
        if habitat.lower() == 'terrestre':
            i += 1
            animais_terrestres.append(animais)

with open('aula06/arquivo_animais_leitura.txt', 'w', encoding='UTF-8') as leitura_animal:
    with open('aula06/arquivo_animais.txt', 'r', encoding='UTF-8') as animais_habitat:
        for animais in animais_terrestres:
            leitura_animal.write(f'{animais}\n')

