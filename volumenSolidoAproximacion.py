import math
from tabulate import tabulate
import numpy as np

print("\tVolumen de un solido por aproximaciones")
xInicial = int(input("x inicial: "))
xFinal = int(input("x final: "))
divisiones = int(input("Numero de divisiones: "))
difX=(xFinal-xInicial)/divisiones
x = []
y = []

i=xInicial
while i<=xFinal:
    x.append(i)
    i+=difX

print("\n\tEntra al codigo para cambiar la funcion de Y en la linea 23")
#y=sqrt(x^2-1)

i=0
while i<len(x):
    y.append( math.sqrt((math.pow((x[i]),2))-1) )
    i += 1

puntos = np.column_stack((x, y))
print(tabulate(puntos, headers=["X","Y"], tablefmt="grid"))

print("\n\tVolumenes")
volumenes=[]
for i in range((len(x))-1):
    volumen = ((math.pi/3)*difX) * (math.pow(y[i],2) + (y[i])*(y[i+1]) + math.pow(y[i+1],2))
    print("y_i: {}\ny_i+1: {}\nvolumen: {}".format(y[i], y[i+1], volumen))
    print("-----------------")
    volumenes.append(volumen)

print("\n\tVolumen total")
suma=0
for i in range(len(volumenes)):
    suma+=volumenes[i]

print("Volumen total:",suma)