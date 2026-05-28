with open('next_step/aula06/notas.txt', 'a') as notas: #sempre usar with, arquivo fecha automaticamente
    for _ in range(4):
        numero = input('Insira um número: ')
        notas.write(f'{numero}\n')
