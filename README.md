# Ricard Catalá Garfias - A01710071
# Restaurante sandwiches de salmón

## Contexto: 

En las últimas semanas los trabajadores de un restaurante donde venden principalmente sandwiches de salmón han experimentado un desperdicio de salmón ya que pasan su fecha de caducidad. La razón de esto es que se descongelan más salmones de los que se venden. El salmón tarda de 1-2 días en echarse a perder después de ser descongelado y es por esto que se necesita un programa que pueda ayudar en analizar cuando se deben de descongelar los salmones para evitar el desperdicio de estos, esto con base a las ventas anteriores.

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


**Registro Semana Anterior** ventas previas
Se crea una lista nueva de valores que se piden al usuario y se promedian con los datos anteriores del calendario.

**Salmones por desconjelar**
Calucula la diferencia entre la predicion de ventas del dia que se pida y los salmones desconjelados del día anterior para poder regresar el número de salmones que se necesitan desconjelar para ese día.

**Consultar ventas** 
Crea una tabla de la libreria pandas en donde se despliegan las ventas de las semanas anteriores y el promedio de venta de estas. Además se pueden consultar los promedios de ventas por dias de la semana con base a los datos anteriores.

**Graficar**
Se grafican los promedios de ventas por día 

**Mejor día para aplicar ofertas** 
Calcula el mejor día para aplicar ofertas

