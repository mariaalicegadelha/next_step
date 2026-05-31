import csv

eleitor = 0

with open('next_step/aula06/dados_eleicao.csv', 'r', encoding='UTF-8') as arquivo_eleicao:

    reader = csv.reader(arquivo_eleicao)

    next(reader)
    
    candidatos = []

    for col in reader:
        eleitor += 1
        candidatos.append(col[2])
    
    candidatos_unicos = list(set(candidatos))

    votos = {}
    linhas_candidatos = ''

    for candidato in candidatos_unicos:
        votos[candidato] = candidatos.count(candidato)

    resultado_ordenado = sorted(
        votos.items(),
        key=lambda d: d[1],
        reverse=True
    )

    for candidato, qnt_votos in resultado_ordenado:
        porcentagem = (qnt_votos / eleitor) * 100
        linhas_candidatos += (
        f"{candidato}: {porcentagem:.2f}% ({qnt_votos})\n"
        )
    
    mais_votado = max(votos, key=lambda k: votos[k])
  
resumo = f"""Resultados Eleitorais
-------------------------
Total de votos: {eleitor}
-------------------------
{linhas_candidatos}-------------------------
Vencedor: {mais_votado}
-------------------------
"""
with open('next_step/aula06/resultado.txt', 'w', encoding='UTF-8') as resultado:
    resultado.write(resumo)
