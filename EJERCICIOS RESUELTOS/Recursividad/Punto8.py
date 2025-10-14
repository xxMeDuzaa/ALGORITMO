#8. Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
#deci_bin(n)= deci_bin(n//2) + str(n%2) -> si (n==0) Return "0" / si (n==1) Return "1"

def deci_bin(n):
    if n==0:  
        return "0"
    elif n==1:
        return "1"
    else:
        return deci_bin(n//2) + str(n%2) #el str(n%2) es para convertir resto de la division en un string y concatenarlo al resultado de la llamada recursiva

print(f'El numero entero 13 en binario es: {deci_bin(13)}')