# Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:


from heap import HeapMax

# Crear la cola de impresión
cola_impresion = HeapMax()

# a.a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
print("Los tres documentos de empleados se han cargado exitosamente.")
cola_impresion.arrive("doc_empleado_1", 1)
cola_impresion.arrive("doc_empleado_2", 1)
cola_impresion.arrive("doc_empleado_3", 1)
print()

#b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print("Imprimo el primer documento de la cola:", cola_impresion.attention()[1])

print()

#c. cargue dos documentos del staff de TI.
print("Los dos documentos del staff de TI han sido cargados.")
cola_impresion.arrive("doc_ti_1", 2)
cola_impresion.arrive("doc_ti_2", 2)
print()

#d. cargue un documento del gerente.
print("Se cargo un documento del gerente.")
cola_impresion.arrive("doc_gerente_1", 3)
print()

# e. imprimir los dos primeros documentos
print("Imprimo los dos primeros documentos: ")
print("-", cola_impresion.attention()[1])
print("-", cola_impresion.attention()[1])
print()

#f. cargue dos documentos de empleados y uno de gerente.
print("Los dos documentos de empleado y uno de gerente han sido cargados.")
cola_impresion.arrive("doc_empleado_4", 1)
cola_impresion.arrive("doc_empleado_5", 1)
cola_impresion.arrive("doc_gerente_2", 3)
print()

# g. imprimir todos los documentos restantes
print("Imprimo todos los documentos restantes: ")
while cola_impresion.size() > 0:
    print("-", cola_impresion.attention()[1])