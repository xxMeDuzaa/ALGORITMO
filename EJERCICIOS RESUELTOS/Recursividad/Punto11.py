#11. Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.

def invertir_numero(n, invertido=0):
    if n == 0:
        return invertido
    else:
        ultimo = n % 10 #se obtiene el modulo, entonces se consigue el ultimo digito
        invertido = invertido * 10 + ultimo
        return invertir_numero(n // 10, invertido) #eliminas el último dígito del número

print(f"El numero entero 123 invertido queda asi: {invertir_numero(123)}")