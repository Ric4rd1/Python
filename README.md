#Ricard Catalá Garfias - A01710071
# Restaurante sandwiches de salmón

## Contexto: 

En las últimas semanas los trabajadores de un restaurante donde venden principalmente sandwiches de salmón han experimentado un desperdicio de salmón ya que pasan su fecha de caducidad. La razón de esto es que se descongelan más salmones de los que se venden. El salmón tarda de 1-2 días en echarse a perder después de ser descongelado y es por esto que se necesita un programa que pueda ayudar en analizar cuando se deben de descongelar los salmones para evitar el desperdicio de estos. Otros ingredientes que se tomarán en cuenta también son el pan y la lechuga.

El programa servirá para hacer un uso inteligente de los ingredientes, principalmente salmón. Además de esto el programa va a ser capaz de analizar las ganancias, y buscar los días más oportunos para hacer promociones y subir las ventas del establecimiento.

------------


##  Pseudocódigo:

###  Inicio
**DEFINIR VARIABLES**
- Fecha_caducidad_salmón (días)  [número entero]
- Ventas_sandwiches_últimas_semanas (n° sandwiches) [Lista]
Lunes 
Martes
Miércoles
Jueves
Viernes
Sábado 
- Ventas_esperados_por_día(n° sandwiches) [Lista]
- Ventas_reales_del_día_anterior (n° sandwiches) [número entero]


**PROMEDIO** ventas previas
Hacer un promedio de Ventas sandwiches últimas semanas por cada día  
y de ahí calcular Ventas_esperados_por_día.

Descongelar los salmones dependiendo de la fecha de caducidad que depende del tiempo de transporte

**INPUT** Ventas_reales_del_día_anterior

**WHILE** 0 < Ventas_esperados_por_día  -  Ventas_reales_del_día_anterior <  5
Ventas_esperados_por_día = Ventas_esperados_por_día

**IF NOT**

**IF** 0 >  Ventas_esperados_por_día  -  Ventas_reales_del_día_anterior
   Ventas_esperados_por_día = Ventas_esperados_por_día + 2

**ELSE**
   Ventas_esperados_por_día = Ventas_esperados_por_día - 2
