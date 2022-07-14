import numpy as np
import matplotlib.pyplot as plt

### Cria o array par armazenar os números primos ###
primos = [0]
num = 1
limite = int(input("defina quantas vezes quer rodar o programa: "))

### Verifica se o número é primo ###
for num in range(limite):
    primecheck = 0
    for i in range(1,num + 1):
        if (num % i) == 0:
            primecheck += 1        
    if primecheck == 2:
        primos.append(num)
print(primos)


### Gráfico ###
### Cria figura e eixos ###
fig, ax = plt.subplots(figsize = (9, 6))
nomefig = 'Primos.png'
fontsize = 20
xlab = f'Quantidade de primos no intervalo = {len(primos) - 1}'
ylab = 'Números verificados'

### Eixo x - numero de passos ###
ax.set_xlabel(xlab, fontsize = fontsize)

### Eixo y - valores intermediários ###
intervalo = np.array(primos)

### plotar dados ###
ax.plot(intervalo, marker = '.', ls = '', ms = 7, color = 'r')
ax.set_ylabel(ylab, fontsize = fontsize)
ax.tick_params('y', )
ax.grid(color = 'black')

### Salvar figura ###
#fig.savefig(nomefig)

### Mostra o plot no terminal ###
plt.show()
