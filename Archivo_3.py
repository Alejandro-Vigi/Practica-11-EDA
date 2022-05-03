def fibonacci_iterativo_v1(numero):
    f1=0
    f2=1
    tmp=0
    for i in range(1,numero-1):
        tmp = f1+f2
        f1=f2
        f2=tmp
    return f2

fibonacci_iterativo_v1(6)

"""
5
"""


#Tip: En Python se puede hacer una asignación paralela, esto va a servir para evitar 
#tener la variable auxiliar tmp, tal y como se muestra a continuación.


def fibonacci_iterativo_v2(numero):
    f1=0
    f2=1
    for i in range(1, numero-1):
        f1,f2=f2,f1+f2    #Asignación paralela
    return f2

fibonacci_iterativo_v2(6)

"""
5
"""


#Una vez que conocemos como calcular la sucesión de Fibonacci, ahora 
#vamos a aplicar la estrategia bottom-up. Partimos del hecho de que ya tenemos las soluciones para:

#f(0) = 0
#f(1) = 1
#f(2) = 1
#Estas soluciones previas son almacenadas en la tabla de soluciones f_parciales.

#f_parciales = [0, 1, 1]


def fibonacci_bottom_up(numero):
    f_parciales = [0, 1, 1]  #Esta es la lista que mantiene las soluciones previamente calculadas
    while len(f_parciales) < numero:
        f_parciales.append(f_parciales[-1] + f_parciales[-2])
        print(f_parciales)
    return f_parciales[numero-1]

fibonacci_bottom_up(5)

"""
[0, 1, 1, 2]
[0, 1, 1, 2, 3]

3

"""

#Memoria inicial
memoria = {1:0, 2:1, 3:1}

def fibonacci_top_down(numero):
    if numero in memoria:      #Si el número ya se encuentra calculado, se regresa el valor ya ya no se hacen más cálculos
        return memoria[numero]
    f = fibonacci_iterativo_v2(numero-1) + fibonacci_iterativo_v2(numero-2)
    memoria[numero] = f
    return memoria[numero]

#Como se muestra en el código anterior, para obtener n, se calculan n-1 y n-2 usando la versión 
# iterativa. La deficiencia de este algoritmo es que hay cálculos que es están repitiendo. 
# La ventaja, es que una vez que ya se calcularon, se guardan en una memoria, que en este caso es 
# un diccionario; en dado caso de que se necesite un valor que ya ha sido calculado, sólo regresa y ya 
# no se realizan los cálculos.

fibonacci_top_down(12)

"""
89
"""

#Memoria después de obtener el elemento 12 de la sucesión de Fibonacci
memoria

"""
{1: 0, 2: 1, 3: 1, 12: 89}
"""

#Memoria después de obtener el elemento 8 de la sucesión de Fibonacci
fibonacci_top_down(8)

"""
13
"""

memoria
"""
{1: 0, 2: 1, 3: 1, 8: 13, 12: 89}
"""

"""
Como se muestra en la impresión de la variable memoria, que contiene los resultados previamente calculados, 
los nuevos valores obtenidos se agregaron a ésta. El problema con esta versión es que se siguen haciendo 
cálculos de más, ya que la función fibonacci_iterativo_v2() no tiene acceso a la variable memoria, lo que 
implica que tenemos que hacer modificaciones a la implementación. Por ejemplo, si se quiere calcular el 
elemento 5, se tiene que calcular (n-2) y (n-1), aunque algunos valores ya existen en la variable memoria 
no hay una manera de acceder a ellos.

f(5) = 
    (n-1) = f(4)+f(3)+f(2)+f(1)
    (n-2) = f(3)+f(2)+f(1)
Ahora, se requiere que los valores ya calculados sean guardados en un archivo, de tal manera que se 
puedan utilizar en otro instante de tiempo. Para esto se va a hacer uso de la biblioteca pickle 
(https://docs.python.org/3.5/library/pickle.html). Los archivos que se generan con pickle están en binario, 
por lo que no se puede leer a simple vista la información que contienen, como se haría desde un archivo de 
texto plano.
"""


#Se carga la biblioteca
import pickle

#Guardar variable
#No hay restricción en lo que se pone como extensión del archivo, 
#generalmente se usa .p o .pickle como estandar.
archivo = open('memoria.p', 'wb')   #Se abre el archivo para escribir en modo binario
pickle.dump(memoria, archivo)       #Se guarda la variable memoria que es un diccionario
archivo.close()                     #Se cierra el archivo


#Leer variable
archivo = open('memoria.p', 'rb')          #Se abre el archivo para leer en modo binario
memoria_de_archivo = pickle.load(archivo)  #Se lee la variable
archivo.close()                            #Se cierra el archivo


#Si no se realizó un cambio en memoria, ésta variable y memoria_de_archivo deben contener los mismos datos.

memoria
"""
{1: 0, 2: 1, 3: 1, 8: 13, 12: 89}
"""

memoria_de_archivo
"""
{1: 0, 2: 1, 3: 1, 8: 13, 12: 89}
"""