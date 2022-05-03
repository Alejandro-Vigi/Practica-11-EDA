#Modelo RAM
#Cuando se realiza un análisis de complejidad utilzando el modelo RAM, se debe contabilizar las veces 
#que se ejecuta una función o un ciclo, en lugar de medir el tiempo de ejecución.

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

times = 0

def insertionSort_graph(n_lista):
    global times
    for index in range(1,len(n_lista)):
        times += 1
        actual = n_lista[index]
        posicion = index
        while posicion>0 and n_lista[posicion-1]>actual:
            times += 1
            n_lista[posicion]=n_lista[posicion-1]
            posicion = posicion-1           
        n_lista[posicion]=actual
    return n_lista


TAM = 101
eje_x = list(range(1,TAM,1))
eje_y = []
lista_variable = []

for num in eje_x:
    lista_variable = random.sample(range(0, 1000), num)
    times = 0
    lista_variable = insertionSort_graph(lista_variable)
    eje_y.append(times)
    
    
    
fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(eje_x, eje_y, marker="o",color="b", linestyle='None')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend(["Insertion sort"])

plt.title('Insertion sort')
plt.show()