# 17. Se cuenta con los vuelos del aeropuerto de Heraklion en Creta, de estos se sabe la siguiente
# información: empresa, número del vuelo, cantidad de asientos del avión, fecha de salida, des-
# tino, kms del vuelo. Y además se conoce los datos de cantidades de asientos totales y ocupados
# por clase (primera y turista). Implemente las funciones necesarias que permitan realizar las
# siguiente actividades:

from vuelos import vuelos, order_by_numero
from list_ import List

list_vuelos=List()

def cargar_vuelos(list_vue, vuelos):
    for vuelo in vuelos:
        list_vue.append(vuelo)

def ordenarCriterios(list_SH):
    list_SH.add_criterion("numeroVuelo", order_by_numero)
    
def ordenarNumeroVuelo(list_SH):
    list_SH.sort_by_criterion("numeroVuelo")


#a. mostrar los vuelos con destino a Atenas, Miconos y Rodas;
def mostrarDestinosEspecificos(list_vue): #DEBO RECORRER TODA LA LISTA
    buscados=["Atenas","Miconos","Rodas"]
    
    for vuelo in list_vue:
        if vuelo.destino in buscados:
            print(vuelo)

# b. mostrar los vuelos con asientos clase turista disponible;
def mostrarVuelosAsientos(list_vue):
    for vuelo in list_vue:
        disponibles = vuelo.cantAsientosTotal - vuelo.ocupadosPrimera - vuelo.ocupadosTurista
        if disponibles > 0:
            print(vuelo)

# c. mostrar el total recaudado por cada vuelo, considerando clase turista ($75 por kilómetro) y
# primera clase ($203 por kilómetro);
def totalRecaudadoVuelo(list_vue):
    TotalVuelo=0
    for vuelo in list_vue:
        RecaudadoTurista=0
        RecaudadoPrimera=0
        if vuelo.ocupadosTurista>0:
            RecaudadoTurista=vuelo.ocupadosTurista * vuelo.KmVuelo * 75
            
        if vuelo.ocupadosPrimera>0:
            RecaudadoPrimera=vuelo.ocupadosPrimera * vuelo.KmVuelo * 203
            
        TotalVuelo=RecaudadoPrimera+RecaudadoTurista
        print(f"Vuelo {vuelo.numeroVuelo}: {TotalVuelo}$")


# d. mostrar los vuelos programados para una determinada fecha;
def mostrarVuelosFecha(list_vue):
    for vuelo in list_vue:
        if vuelo.fechaSalida==2023: #elijo esta por ejemplo
            print(f"Vuelos programados para el año 2023 {vuelo}")

# e. vender un asiento (o pasaje) para un determinado vuelo;
def venderPasaje(lista_vuelos):
    numero_vuelo = input("Ingrese el número del vuelo: ")
    clase = input("Ingrese la clase ('turista' o 'primera'): ").lower()

    for vuelo in lista_vuelos:
        if vuelo.numeroVuelo == numero_vuelo:
            ocupados_totales = vuelo.ocupadosPrimera + vuelo.ocupadosTurista #calculo asientos ocupados totales
            
            if ocupados_totales >= vuelo.cantAsientos: # verifico si hay espacio en general
                print("No hay asientos disponibles en el vuelo.")
                return

            if clase == "turista": # Ahora verifico por clase y vendo asiento
                # Si hay espacio en general, incremento turista
                vuelo.ocupadosTurista += 1
                print(f"Asiento vendido en clase turista para el vuelo {numero_vuelo}.")
                return

            elif clase == "primera":
                vuelo.ocupadosPrimera += 1
                print(f"Asiento vendido en primera clase para el vuelo {numero_vuelo}.")
                return

            else:
                print("Clase inválida. Debe ser 'turista' o 'primera'.")
                return

    print(f"No se encontró el vuelo con número {numero_vuelo}.")



# f. eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, se debe indicar la canti-
# dad de dinero a devolver;
def eliminarVuelo(list_vue):
    numero_vuelo = "SE456"  # elijo vuelo a eliminar
    encontrado = False
    for vuelo in list_vue:
        if vuelo.numeroVuelo == numero_vuelo:
            encontrado = True
            pasajes_vendidos = vuelo.ocupadosPrimera + vuelo.ocupadosTurista
            if pasajes_vendidos > 0:
                dinero_a_devolver = (vuelo.ocupadosPrimera * vuelo.KmVuelo * 203) + (vuelo.ocupadosTurista * vuelo.KmVuelo * 75)
                print(f"El vuelo eliminado tiene pasajes vendidos. Dinero a devolver: ${dinero_a_devolver}")
            else:
                print("No hay pasajes vendidos, no hay dinero que devolver.")
            
            list_vue.delete_value(numero_vuelo, "numeroVuelo")

    if not encontrado:
        print(f"No se encontró el vuelo con número {numero_vuelo}.")


# g. mostrar las empresas y los kilómetros de vuelos con destino a Tailandia.
def empresasKilometros(list_value):
    encontrado=False
    print("Empresas y los kilómetros de vuelos con destino a Tailandia: ")
    for vuelo in list_value:
        if vuelo.destino=="Tailandia":
            encontrado=True
            print(f"Empresa: {vuelo.empresa}, Kilometros: {vuelo.KmVuelo}")
    
    if not encontrado:
        print("No se encontro empresas con destino a Tailandia.")
            



#CP
cargar_vuelos(list_vuelos, vuelos)
ordenarCriterios(list_vuelos)
ordenarNumeroVuelo(list_vuelos)
# print("Lista de vuelos: ")
# list_vuelos.show()
print("Vuelos con destino a Atenas, Miconos y Rodas: ")
mostrarDestinosEspecificos(list_vuelos)
print()
print("Vuelos con asientos clase turista disponible: ")
mostrarVuelosAsientos(list_vuelos)
print()
print("Total recaudado de cada vuelo: ")
totalRecaudadoVuelo(list_vuelos)
print()
mostrarVuelosFecha(list_vuelos)
print()
venderPasaje(list_vuelos)
eliminarVuelo(list_vuelos)
print()
empresasKilometros(list_vuelos)