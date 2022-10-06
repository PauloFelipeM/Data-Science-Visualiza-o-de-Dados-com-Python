#%%
import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y3 = [5, 1, 3, 7, 4]

titulo = "Gráfico de barras"
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Título
plt.title(titulo)

# Eixos
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.bar(x1, y1, label = 'Grupo 1')
plt.bar(x2, y3, label = 'Grupo 2')

plt.legend()
plt.show()
# %%
