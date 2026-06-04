import random
from datetime import datetime, timedelta

print(random.randint(1, 30))

nomes = ['Alice', 'Carlos', 'Ayla', 'Marina', 'Ju']

print(random.choice(nomes))
print(random.sample(nomes, 2))

random.shuffle(nomes)

agora = datetime.now()
print(agora)

data_formatada = agora.strftime("%d%m/%y")
print(data_formatada)