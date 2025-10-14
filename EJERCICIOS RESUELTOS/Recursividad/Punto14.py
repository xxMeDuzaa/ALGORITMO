#14. Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir el número a cadena.
#suma_digitos(digito)= ultimo + suma_digito(digito//10) ->Si (digito==0) Return 0 

def suma_digitos(digito):
    if (digito==0): 
        return 0
    else:
        ultimo = digito % 10 #Se obtiene el modulo, entonces se consigue el ultimo digito
        return ultimo + suma_digitos(digito//10)  # Va quitando un dígito por llamada
print(f"La suma de dígitos del 123 es: {suma_digitos(123)}")