# Cresimento da população brasileira 1980-2016
#%%
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt

dados = open('arqs/populacao_brasileira.csv').readlines()

years = []
people = []

for i in range(len(dados)):
  if i != 0:
    dado = dados[i].split(';')
    years.append(int(dado[0]))
    people.append(int(dado[1]))

# Título
plt.title('Crescimento da população brasileira 1980-2016')

plt.xlabel('Ano')
plt.ylabel('População x100.000.000')

plt.bar(years, people, color = '#e4e4e4')
plt.plot(years, people, color = 'k', linestyle = '--')
plt.show()