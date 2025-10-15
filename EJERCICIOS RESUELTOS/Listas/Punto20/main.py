# 20. Una empresa meteorológica necesita registrar los datos de sus distintas estaciones en las cua-
# les recolecta la siguiente información proveniente de sus distintas estaciones de adquisición
# de datos diariamente, implemente las funciones para satisfacer los siguientes requerimientos:

from list_ import List
from empresa import EstacionMeteorologica, Medicion
from datetime import datetime

list_estaciones = List()

estaciones = [
    EstacionMeteorologica("Argentina", "Ushuaia", -54.8, -68.3, 50),
    EstacionMeteorologica("Chile", "Punta Arenas", -53.1, -70.9, 34),
    EstacionMeteorologica("Canadá", "Toronto", 43.7, -79.4, 76),
    EstacionMeteorologica("Japón", "Tokio", 35.6, 139.7, 40),
    EstacionMeteorologica("Brasil", "Manaus", -3.1, -60.0, 92),
    EstacionMeteorologica("Noruega", "Oslo", 59.9, 10.8, 23),
]

mediciones = [
    Medicion(12, 1010, 85, "lloviendo", "Ushuaia", datetime(2025, 5, 3, 14, 0)),
    Medicion(18, 1008, 70, "nublado", "Punta Arenas", datetime(2025, 5, 15, 10, 0)),
    Medicion(25, 1015, 60, "soleado", "Toronto", datetime(2025, 6, 1, 9, 0)),
    Medicion(29, 1005, 88, "tormenta eléctrica", "Manaus", datetime(2025, 5, 20, 16, 0)),
    Medicion(5, 990, 92, "nevando", "Oslo", datetime.now()),
]

# a. se deben poder cargar estaciones meteorológicas, de cada una de estas se sabe su país de
# ubicación, coordenadas de latitud, longitud y altitud;
def cargarEstaciones(list_est, estaciones):
    for estacion in estaciones:
        list_est.append(estacion)

# b. estas estaciones registran mediciones de temperatura, presión, humedad y estado del cli-
# ma –como por ejemplo soleado, nublado, lloviendo, nevando, etcétera– en distintos lapsos
# temporales, estos datos deberán guardarse en la lista junto con la fecha y la hora de la me-
# dición;
def cargarMediciones(list_estaciones, mediciones):
    for medicion in mediciones:
        for estacion in list_estaciones:
            if estacion.ubicacion == medicion.ubicacion:
                estacion.registro.append(medicion)

# c. mostrar el promedio de temperatura y humedad de todas las estaciones durante el mes
# de mayo;
def promedioTempHum(list_est):
    total_temp = 0
    total_hum = 0
    cantidad = 0

    for estacion in list_est:
        for medicion in estacion.registro:
            if medicion.fecha_hora.month == 5:  # Mayo
                total_temp += medicion.temperatura
                total_hum += medicion.humedad
                cantidad += 1
                
    if cantidad > 0:
        prom_temp = (total_temp / cantidad)
        prom_hum = (total_hum / cantidad)
        print(f"Promedio de temperatura en mayo: {prom_temp:.2f}°C")
        print(f"Promedio de humedad en mayo: {prom_hum:.2f}%")
    else:
        print("No hay mediciones registradas en el mes de mayo.")


# d. indicar la ubicación de las estaciones meteorológicas en las que en el día actual está llo-
# viendo o nevando;
def estacionLluviaNevada(list_est):
    encontrado=False
    hoy = datetime.now().date()
    for estacion in list_est:
        for medicion in estacion.registro:
            if medicion.fecha_hora.date() == hoy:
                estado = medicion.estado.lower()
                if estado == "lloviendo" or estado == "nevando":
                    encontrado=True
                    print(medicion.ubicacion)
                    
    if not encontrado:
        print("No hay ubicaciones de las estaciones meteorologicas en las que el dia actual esta lloviendo o nevando.")

# e. mostrar los datos de las estaciones meteorológicas que hayan registrado estado del clima
# tormenta eléctrica o huracanes;
def mostrarEstaciones(list_est): 
    encontrado=False               
    for estacion in list_est:
        for medicion in estacion.registro:
            if medicion.estado=="tormenta eléctrica" or medicion.estado=="huracanes":
                encontrado=True
                print(estacion)
                print("Registro: ")
                print(medicion)
                
    if not encontrado:
        print("No hay estaciones meteorológicas que hayan registrado estado del clima tormenta eléctrica o huracanes.")
            
            
            
#CP
cargarEstaciones(list_estaciones, estaciones)
cargarMediciones(list_estaciones, mediciones)
#list_estaciones.show_list_of_list()
promedioTempHum(list_estaciones)
print()
print("Ubicación de las estaciones meteorológicas en las que en el día actual está lloviendo o nevando: ")
estacionLluviaNevada(list_estaciones)
print()
print("Estaciones meteorológicas que hayan registrado estado del clima tormenta eléctrica o huracanes: ")
mostrarEstaciones(list_estaciones)