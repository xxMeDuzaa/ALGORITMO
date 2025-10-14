def invertirVector(vector):
    if not vector:  # Si el vector está vacío
        return []
    else:
        return [vector[-1]] + invertirVector(vector[:-1])  # Último + recursivo con el resto

# Vector original
vectorValores = [1, 2, 3]

# Invertir y mostrar
print(f"El vector invertido quedaría: {invertirVector(vectorValores)}")