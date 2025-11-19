"""Desarrollar una función que permita convertir un número romano en un número decimal."""

def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}

    """Pasamos todo a mayúsculas para soportar minúsculas"""
    romano = romano.upper()

    """Validación de caracteres inválidos"""
    for letra in romano:
        if letra not in valores:
            raise ValueError(f"Carácter inválido en número romano: '{letra}'")

    """Función recursiva interna"""
    def convertir(s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return valores[s[0]]
        if valores[s[0]] < valores[s[1]]:
            return valores[s[1]] - valores[s[0]] + convertir(s[2:])
        else:
            return valores[s[0]] + convertir(s[1:])

    return convertir(romano)
