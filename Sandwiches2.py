"""
algoritmo para encontrar el numero promedio de sandwiches vendidos por días en un mes.

Estado inicial:
lista ventas = generada aleatoreamente
dia = input (string)

Algoritmo:

1.-Crear la matriz aleatoriamente de las ventas de sandwiches
2.-Pedir el día que se requiere para el promedio
3.-Sumar de las ventas en cada día de la semana y dividirlo para obtener el promedio de
ventas de cada día
4.-Mostrar el resultado
"""
#Importar librerias
import random
import numpy as np

#Crear una lista random para las ventas de sandwiches en un mes
#Se crea una matriz de 4x7
lista_ventas = np.random.randint(5, 15, size=(4, 7))
print(f"""Calendario:
   L  M  M  J  V  S  D
{lista_ventas}

------------------------
""")
#Salones por comprar para la semana
semana_1 = (sum(list(lista_ventas[0,:])))
semana_2 = (sum(list(lista_ventas[1,:])))
semana_3 = (sum(list(lista_ventas[2,:])))
semana_4 = (sum(list(lista_ventas[3,:])))
mes = semana_1 + semana_2 + semana_3 + semana_4

#Definir la función para obtener el promedio de ventas en cualquier día
def promedio (dia):
    if dia == "lunes":
        ventas_promedio = float((np.sum(lista_ventas[:,0]))/4)
        return ventas_promedio
    elif dia == "martes":
        ventas_promedio = float((np.sum(lista_ventas[:,1]))/4)
        return ventas_promedio
    elif dia == "miercoles":
        ventas_promedio = float((np.sum(lista_ventas[:,2]))/4)
        return ventas_promedio
    elif dia == "jueves":
        ventas_promedio = float((np.sum(lista_ventas[:,3]))/4)
        return ventas_promedio
    elif dia == "viernes":
        ventas_promedio = float((np.sum(lista_ventas[:,4]))/4)
        return ventas_promedio
    elif dia == "sabado":
        ventas_promedio = float((np.sum(lista_ventas[:,5]))/4)
        return ventas_promedio
    elif dia == "domingo":
        ventas_promedio = float((np.sum(lista_ventas[:,6]))/4)
        return ventas_promedio

#Salmones por comprar en el mes
print(f"Los salmones que se compran al mes son: {mes}")

#Preguntar que día necesitas saber el promedio de sandwiches vendidos
dia_input = str(input("Escriba el día de la semana que requiera el promedio de ventas: "))


#Print el resultado
print(f"El promedio es: {promedio(dia_input)} sandwiches")
