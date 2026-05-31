'''i = 0
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
            leitura_animal.write(f'{animais}\n')'''

lista_notas = []
with open('next_step/aula06/notas.txt', 'w', encoding='UTF-8') as boletim: 
    for _ in range(4):
        nota = float(input('Insira uma nota: '))
        lista_notas.append(nota)
    boletim.write(f'As suas notas foram: {lista_notas}\n')
    boletim.write(f'A sua maior nota foi: {max(lista_notas)}\n')
    boletim.write(f'A sua menor nota foi: {min(lista_notas)}\n')
    boletim.write(f'A sua média foi: {sum(lista_notas)/len(lista_notas)}\n')


