#10. Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
#cant_digitos(digito)= 1+cant_digitos(digito//n) -> Si (digito<10) Return 1
def cant_digitos(digito):
    if not digito: #Si la cadena esta vacia, devuelve cero.
        return 0
    else:
        return 1 + cant_digitos(digito[0:-1])  # Va quitando un dígito por llamada

numero_str=str(100)  # Convertimos a string
print(f"La cantidad de dígitos que tiene el número 100 es: {cant_digitos(numero_str)}")

