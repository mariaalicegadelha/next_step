##Problema 1

''' N = int(input())

def odd_numbers(num1, num2):
    total = 0

    start = min(num1, num2)
    end = max(num1, num2)

    for number in range(start + 1, end):
        if number % 2 != 0:
            total += number

    print(total)

for i in range(N):
    x, y = map(int, input().split())
    odd_numbers(x, y)

Problema 2
N = int(input())

sequencia_fibonacci = [0]

def gerar_fibonacci(num):
    for _ in range(N):
        if _ == 0:
            sequencia_fibonacci.append(1)
        else:
            proximo = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]
            sequencia_fibonacci.append(proximo)

gerar_fibonacci(N)

print(*sequencia_fibonacci) '''

N = input()

def conversor(entrada):
    if entrada.isdigit():
        dict_conversor = {
            '0': 'zero',
            '1': 'um',
            '2': 'dois',
            '3': 'tres',
            '4': 'quatro',
            '5': 'cinco',
            '6': 'seis',
            '7': 'sete',
            '8': 'oito',
            '9': 'nove'
        }
    else:
        dict_conversor = {
            'zero': 0,
            'um': 1,
            'dois': 2,
            'tres': 3,
            'quatro': 4,
            'cinco': 5,
            'seis': 6,
            'sete': 7,
            'oito': 8,
            'nove': 9
        }

    return dict_conversor[entrada]

print(conversor(N))