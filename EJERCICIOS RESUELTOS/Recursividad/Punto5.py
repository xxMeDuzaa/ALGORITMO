#5. Desarrollar una función que permita convertir un número romano en un número decimal.

romanos = { #hacemos un diccionario
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,    
}

def roman(string):
    if not string:  # si la cadena está vacía se returna cero
        return 0
    else:
        decimal = romanos[string[0]]
        if len(string) > 1:
            if decimal < romanos[string[1]]:
                return -decimal + roman(string[1:])
    return decimal + roman(string[1:])  # Llama la cadena a partir del 2° caracter

print(roman('MMXXV'))
