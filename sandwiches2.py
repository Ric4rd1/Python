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

import numpy as np
import matplotlib.pyplot as plt
from art import tprint
import pandas as pd

#Crear una lista random para las ventas de sandwiches en un mes
#Se crea una matriz de 4x7
lista_ventas = np.random.randint(5, 15, size=(4, 7))
calendario = (f"""Calendario:
   L  M  M  J  V  S  D
{lista_ventas}
   ------------------------""")
print(calendario)
#Crear el menu
def menu ():
    tprint("""  MENU""", font = "small")
    print(
"""- - - - - - - - - - - - - - - - - - - - - - - 
| [1] Registro semana anterior                   |
| [2] Salmones por desconjelar                   |
| [3] Consultar promedio de ventas de sandwiches |
| [4] Mostrar calendario de ventas               |
| [5] Graficar                                   |
| [6] Salir                                      |
   - - - - - - - - - - - - - - - - - - - - - - - 
""")


#Salmones por comprar para la semana
def totales_semana():
    semana_1 = (sum(list(lista_ventas[0,:])))
    semana_2 = (sum(list(lista_ventas[1,:])))
    semana_3 = (sum(list(lista_ventas[2,:])))
    semana_4 = (sum(list(lista_ventas[3,:])))
    return [semana_1, semana_2, semana_3, semana_4]
mes = totales_semana()

#pandas table
def table_calendario ():
    titled_column = {"Ventas": mes,
                     "Promedio semana": [[mes[0]/7], [mes[1]/7], [mes[2]/7], [mes[3]/7]]}
    data = pd.DataFrame(titled_column)
    data.index = ["semana 1", "semana 2", "semana 3", "semana 4"] 
    print(data)

# Diccionario reporte de la nueva semana 
def reporte_semana():
    global reporte_semana_dict
    lun = int(input("Ventas del lunes: "))
    mar = int(input("Venas del martes: "))
    mie = int(input("Venas del miércoles: "))
    jue = int(input("Venas del jueves: "))
    vie = int(input("Venas del viernes: "))
    sab = int(input("Venas del sábado: "))
    dom = int(input("Venas del domingo: "))

    reporte_semana_dict = dict.fromkeys(["lunes", 
                                    "martes", 
                                    "miercoles",
                                    "jueves", 
                                    "viernes", 
                                    "sabado", 
                                    "domingo"])
    
    reporte_semana_dict["lunes"] = lun
    reporte_semana_dict["martes"] = mar
    reporte_semana_dict["miercoles"] = mie
    reporte_semana_dict["jueves"] = jue
    reporte_semana_dict["viernes"] = vie
    reporte_semana_dict["sabado"] = sab
    reporte_semana_dict["domingo"] = dom
    return reporte_semana_dict
    
# Diccionario de totale de ventas por dia del mes anterior
def reporte_mes():
    global reporte_mes_dict 
    reporte_mes_dict = dict.fromkeys(["lunes", 
                                 "martes", 
                                 "miercoles",
                                 "jueves", 
                                 "viernes", 
                                 "sabado", 
                                 "domingo"])
    reporte_mes_dict["lunes"] = float((np.sum(lista_ventas[:,0]))/4)
    reporte_mes_dict["martes"] = float((np.sum(lista_ventas[:,1]))/4)
    reporte_mes_dict["miercoles"] = float((np.sum(lista_ventas[:,2]))/4)
    reporte_mes_dict["jueves"] = float((np.sum(lista_ventas[:,3]))/4)
    reporte_mes_dict["viernes"] = float((np.sum(lista_ventas[:,4]))/4)
    reporte_mes_dict["sabado"] = float((np.sum(lista_ventas[:,5]))/4)
    reporte_mes_dict["domingo"] = float((np.sum(lista_ventas[:,6]))/4)
    
    return reporte_mes_dict
    

#Buscar el nuevo promedio
def nuevo_reporte(): 
    reporte_mes()
    reporte_semana()
    reporte_mes_values = list(reporte_mes_dict.values())
    reporte_semana_values = list(reporte_semana_dict.values())
    np_reporte_mes_values = np.array(reporte_mes_values)
    np_reporte_semana_values = np.array(reporte_semana_values)
    update_reporte = ((np_reporte_mes_values) + (np_reporte_semana_values))/2
    return update_reporte 

#tabla del promedio acutalizado
def table_registro():
    lista_update = nuevo_reporte()
    columna = {
        "Lunes": lista_update[0],
        "Martes": lista_update[1],
        "Miércoles": lista_update[2],
        "Jueves": lista_update[3],
        "Viernes": lista_update[4],
        "Sábado": lista_update[5],
        "Domingo": lista_update[6]
    }
    return columna
    
    

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
#print(f"Los salmones que se compran al mes son: {mes}")

#ejecutar el menu
menu()
opcion =  int(input("Elige una opcion: "))
while opcion != 6:
    if opcion == 1:
        table_registro()
    elif opcion == 2:
        pass
    elif opcion == 3:
        totales_semana()
        dia_input = str(input("Escriba el día de la semana que requiera el promedio de ventas: "))
        print(f"El promedio del {dia_input} es: {promedio(dia_input)} sandwiches")
    elif opcion == 4:
        print(calendario)
        table_calendario()
    elif opcion == 5:
            plt.hist(lista_ventas, bins = 7)
            plt.show()
    else:
        print("opción no valida")
    
    menu()
    opcion =  int(input("Elige una opcion: "))
print("Gracias por usar el programa")



#plt.hist(lista_ventas, bins = 7)
#plt.show()
