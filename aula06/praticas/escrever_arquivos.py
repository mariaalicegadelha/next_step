arquivo = open('next_step/aula06/praticas/arquivo-prototipo.txt', 'a', encoding='UTF-8') #cria o arquivo

arquivo.write('Vamos escrever\n') #\n nao eh automatico
arquivo.write('Não sei o que escrever\n') #o modo write ignora todo o conteudo original

arquivo.seek(0)

arquivo.write('First\n')
arquivo.close() #boa prática

outro_arq = open('next_step/aula06/praticas/arquivo-outro.txt', 'a', encoding='UTF-8')  

lista = ['ovos\n', 'banana\n', 'iogurte\n'] #espaço precisa ser manual

outro_arq.writelines(lista)

outro_arq.close()