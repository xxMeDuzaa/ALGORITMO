# 2. Implementar una función que calcule la suma de todos los números enteros comprendidos
# entre cero y un número entero positivo dado

#entero(a)= a+entero(a-1) -> si (a==0 or a==1 Return a)
def entero(a):
    if (a==0 or a==1):
        return a
    else:
        return a+entero(a-1)

print(f"La suma de todos los numeros comprendidos entre 0 y 3 es: {entero(3)}")