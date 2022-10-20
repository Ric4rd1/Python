#Importar librerias
import numpy as np
import matplotlib.pyplot as plt
from art import tprint
import pandas as pd
import os
clear = lambda: os.system('cls')
clear()

###################################################
#Crear una lista random para las ventas de sandwiches en un mes
#Se crea una matriz de 4x7
lista_ventas = np.random.randint(5, 15, size=(4, 7))

#Crear el menu
def texto():
    global lista_ventas
    calendario = (f"""Calendario:
   L  M  M  J  V  S  D
{lista_ventas}
   """)
    print(calendario)

    print("- - - - - - - - - - - - - - - - - - - - - - ")
    tprint("""  MENU""", font = "small")
    print(
"""- - - - - - - - - - - - - - - - - - - - - - - 
| [1] Registro semana anterior                   |
| [2] Salmones por desconjelar                   |
| [3] Consultar ventas                           |
| [4] Graficar                                   |
| [5] Mejor día para aplicar una oferta          |
| [6] Salir                                      |
   - - - - - - - - - - - - - - - - - - - - - - - 
""")
#print calendario
calendario = (f"""Calendario:
   L  M  M  J  V  S  D
{lista_ventas}
   """)
#--------------OPCIÓN 1--------------------------------

# Diccionario reporte de la nueva semana 
def registro_semana():
    lun = int(input("Ventas del lunes: "))
    mar = int(input("Ventas del martes: "))
    mie = int(input("Ventas del miércoles: "))
    jue = int(input("Ventas del jueves: "))
    vie = int(input("Ventas del viernes: "))
    sab = int(input("Ventas del sábado: "))
    dom = int(input("Ventas del domingo: "))

    registro_semana_dict = dict.fromkeys(["lunes", 
                                    "martes", 
                                    "miercoles",
                                    "jueves", 
                                    "viernes", 
                                    "sabado", 
                                    "domingo"])
    
    registro_semana_dict["lunes"] = lun
    registro_semana_dict["martes"] = mar
    registro_semana_dict["miercoles"] = mie
    registro_semana_dict["jueves"] = jue
    registro_semana_dict["viernes"] = vie
    registro_semana_dict["sabado"] = sab
    registro_semana_dict["domingo"] = dom
    
    return registro_semana_dict

#registro_semana_dict  = registro_semana()

#--------------OPCIÓN 2--------------------------------
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

def nuevo_reporte(): 
    reporte_mes()
    registro_semana_dict = registro_semana()
    reporte_mes_values = list(reporte_mes_dict.values())
    reporte_semana_values = list(registro_semana_dict.values())
    np_reporte_mes_values = np.array(reporte_mes_values)
    np_reporte_semana_values = np.array(reporte_semana_values)
    update_reporte = ((np_reporte_mes_values) + (np_reporte_semana_values))/2
    
    return update_reporte 

#--------------OPCIÓN 3--------------------------------
#Salmones por desconjelar
def por_desconjelar():
    dia = str(input("Ingrese el día de hoy: "))
    while dia not in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]:
        dia = str(input("Ingrese un día correcto: "))
    promedio_xdia = promedio(dia)
    sobra = int(input("¿Cuántos salmones desconjelados hay?: "))
    por_desconjelar = promedio_xdia-sobra
    return por_desconjelar
#--------------OPCIÓN 4--------------------------------
#Salmones vendidos por semana
def totales_semana():
    semana_1 = (sum(list(lista_ventas[0,:])))
    semana_2 = (sum(list(lista_ventas[1,:])))
    semana_3 = (sum(list(lista_ventas[2,:])))
    semana_4 = (sum(list(lista_ventas[3,:])))
    mes = [semana_1, semana_2, semana_3, semana_4]
    return mes

#Tabla ventas por semana
def table_ventas ():
    mes = totales_semana()
    titled_column = {"Ventas": mes,
                     "     Promedio semana": [[mes[0]//7], [mes[1]//7], [mes[2]//7], [mes[3]//7]]}
    data = pd.DataFrame(titled_column)
    data.index = ["semana 1", "semana 2", "semana 3", "semana 4"] 
    print(data)

#promedio por dia 
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

#--------------MENU--------------------------------

texto()
print("")
opcion =  int(input("Elige una opcion: "))
while opcion != 6:
    
    if opcion == 1:
            nuevo_reporte = list(nuevo_reporte())
            u = {"lunes":nuevo_reporte[0],
                  "martes":nuevo_reporte[1],
                  "miercoles":nuevo_reporte[2],
                  "jueves":nuevo_reporte[3],
                  "viernes":nuevo_reporte[4],
                  "sabado":nuevo_reporte[5],
                  "domingo":nuevo_reporte[6]
                  }
            datau = pd.DataFrame(u, index=[0])
            print("")
            print("El nuevo promedio por dia es: ")
            print("")
            print(datau)
            print("")
    elif opcion == 2:
        print(f"Los salmones por desconjelar calculados son: {por_desconjelar()}")
    elif opcion == 3:
        table_ventas()
        print("")
        ask = str(input("¿Quiere consultar el promedio por día? si-->[s]  no-->[n]: "))
    
        if ask == "n" or "s":
            while ask == "s":
                dia_input = str(input("Escriba el día de la semana que requiera el promedio de ventas: "))
                print(f"El promedio del {dia_input} es: {promedio(dia_input)} sandwiches")
                ask = str(input("¿Quiere consultar el promedio de otro día? si-->[s]  no-->[n]"))
        else:
            print("Ingrese un valor correcto")
            ask = str(input("¿Quiere consultar el promedio por día? si-->[s]  no-->[n]"))
        
    elif opcion == 4:
            ax= plt.plot(["lunes", "martes", "miercoles","jueves", "viernes", "sabado", "domingo"], nuevo_reporte )
            plt.show()

    elif opcion == 5:
        
        minimo = min(nuevo_reporte)
        print("************************************************")
        for i in range(len(nuevo_reporte)):
            if nuevo_reporte[i] == minimo:
                if i == 0:
                    print("El día mejor para aplicar una ofreta es el lunes")
                elif i == 1:
                    print("El día mejor para aplicar una ofreta es el martes")
                elif i == 2:
                    print("El día mejor para aplicar una ofreta es el miercoles")
                elif i == 3:
                    print("El día mejor para aplicar una ofreta es el jueves")
                elif i == 4:
                    print("El día mejor para aplicar una ofreta es el viernes")
                elif i == 5:
                    print("El día mejor para aplicar una ofreta es el sabado")
                elif i == 6:
                    print("El día mejor para aplicar una ofreta es el domingo")
        print("************************************************")
        print("")
    else:
        print("opción no valida")
    
    texto()
    opcion =  int(input("Elige una opcion: "))
    clear()
print("Gracias por usar el programa")
