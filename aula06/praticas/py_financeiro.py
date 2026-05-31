import csv

soma = 0
contador = 0
diferenca = 0

with open('next_step/aula06/dados_financeiros.csv', 'r', encoding='UTF-8') as arquivo_financeiro:

    reader = csv.reader(arquivo_financeiro)

    next(reader)  # pula o cabeçalho
    
    valores = []
    datas = []

    for col in reader:
        contador += 1
        soma += int(col[1])
        valores.append(int(col[1]))
        datas.append(col[0])

    media = soma / contador

    balancos = []

    for i in range(1, len(valores)): #comeca do 1 para realizar as operacoes de diferenca corretamente
        balanco = valores[i] - valores[i-1]
        balancos.append(balanco)
        diferenca += (valores[i] - valores[i-1])

    media_mudancas = diferenca / (contador - 1)

    maximo_lucro = max(balancos)
    maxima_perda = min(balancos)

    data_maior_aumento = datas[balancos.index(maximo_lucro) + 1]
    data_maior_queda = datas[balancos.index(maxima_perda) + 1]

relatorio = f"""Analise Financeira
--------------------
Total de meses: {contador}
Total: ${soma}
Média: ${media:.2f}
Variação da média: ${media_mudancas:.2f}
Maior aumento nos lucros: {data_maior_aumento} ${maximo_lucro}
Maior redução nos lucros: {data_maior_queda} ${maxima_perda}
"""

with open('next_step/aula06/relatorio.txt', 'w', encoding='UTF-8') as resumo:
    resumo.write(relatorio)



