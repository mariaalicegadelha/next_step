arquivo = open('next_step/aula06/praticas/arquivo-teste.txt', encoding='UTF-8') #colocar caminho até o arquivo... pasta a pasta

#conteudo = arquivo.read()

#print(conteudo)

'''print(arquivo.readline()) #leitura de linhas

for _ in range(5):
    print(arquivo.readline())'''

'''for linhas in arquivo.readlines():
    print(linhas.strip())'''

linhas = arquivo.readlines()
print(linhas)
arquivo.seek(0) #voltar para o início do arquivo
for linha in arquivo.readlines():
    print(linha.strip())