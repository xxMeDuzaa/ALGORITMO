# Archivo: main.py

from tablahash import TablaHash
from random import randint, choice

# Definir la estructura de un Stormtrooper.
class Stormtrooper:
    def __init__(self, codigo):
        self.codigo = codigo
    
    def __str__(self):
        return self.codigo

# Definir las legiones y las tablas hash
legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

# Instanciamos las dos tablas hash encadenadas
# La primera tabla agrupa por los últimos 3 dígitos
tabla_numeros = TablaHash(1000)
# La segunda tabla agrupa por las iniciales de la legión
tabla_letras = TablaHash(10)

def generar_stormtroopers(cantidad: int):
    """
    a. Genera una cantidad específica de Stormtroopers con códigos aleatorios.
    """
    stormtroopers_generados = []
    print(f"--- Generando {cantidad} Stormtroopers ---")
    for _ in range(cantidad):
        codigo = choice(legiones)
        numero = randint(1000, 9999)
        stormtrooper = Stormtrooper(f'{codigo}-{numero}')
        stormtroopers_generados.append(stormtrooper)
    return stormtroopers_generados

def cargar_stormtroopers(lista_stormtroopers):
    """
    b. Carga los Stormtroopers generados en las dos tablas hash encadenadas.
    """
    print("\n--- Cargando Stormtroopers en tablas hash ---")
    for trooper in lista_stormtroopers:
        # Clave para la tabla de números: los últimos 3 dígitos
        clave_numerica = int(trooper.codigo[-3:])
        tabla_numeros.add(clave_numerica, trooper)

        # Clave para la tabla de letras: las iniciales de la legión
        clave_legion = trooper.codigo[:2]
        tabla_letras.add(clave_legion, trooper)
    print("Carga completada.")

def quitar_traidor(codigo_traidor: str):
    """
    c. Determina si un Stormtrooper traidor está en la tabla y lo elimina.
    """
    print(f"\n--- Buscando y quitando Stormtrooper traidor: {codigo_traidor} ---")
    
    # Se busca por la clave numérica (últimos 3 dígitos)
    clave_numerica = int(codigo_traidor[-3:])
    
    # Usamos la lógica de búsqueda de la tabla para eliminar el elemento
    elemento_eliminado = tabla_numeros.remove(clave_numerica, codigo_traidor)
    
    if elemento_eliminado:
        print(f"El traidor {codigo_traidor} fue encontrado y eliminado.")
    else:
        print(f"El Stormtrooper {codigo_traidor} no se encontró en la tabla.")

def asignar_mision_por_sufijo(sufijo: str, tipo_mision: str):
    """
    d. Obtiene todos los Stormtroopers con un sufijo numérico específico y les asigna una misión.
    """
    print(f"\n--- Asignando misión de {tipo_mision} a Stormtroopers con sufijo '{sufijo}' ---")
    
    clave_numerica = int(sufijo)
    stormtroopers = tabla_numeros.search(clave_numerica)
    
    if stormtroopers:
        print(f"Stormtroopers para la misión de {tipo_mision}:")
        for trooper in stormtroopers:
            print(f"- {trooper}")
    else:
        print(f"No se encontraron Stormtroopers con el sufijo '{sufijo}'.")

def asignar_mision_por_legion(legion: str, tipo_mision: str):
    """
    e. Obtiene todos los Stormtroopers de una legión específica y les asigna una misión.
    """
    print(f"\n--- Asignando misión de {tipo_mision} a la legión {legion} ---")
    
    stormtroopers = tabla_letras.search(legion)
    
    if stormtroopers:
        print(f"Stormtroopers de la legión {legion} para la misión de {tipo_mision}:")
        for trooper in stormtroopers:
            print(f"- {trooper}")
    else:
        print(f"No se encontraron Stormtroopers en la legión {legion}.")

# --- Ejecución del programa ---

# Generar la lista de Stormtroopers
lista_de_stormtroopers=generar_stormtroopers(2000)

# Cargar los Stormtroopers en las tablas hash
cargar_stormtroopers(lista_de_stormtroopers)

# Eliminar el Stormtrooper traidor
quitar_traidor("FN-2187")

# Asignar misiones por sufijo numérico
asignar_mision_por_sufijo("781", "asalto")
asignar_mision_por_sufijo("537", "exploración")

# Asignar misiones por legión
asignar_mision_por_legion("CT", "custodiar a Darth Vader")
asignar_mision_por_legion("TF", "exterminación en Endor")