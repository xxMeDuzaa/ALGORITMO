#3. Implementar una función para calcular el producto de dos números enteros dados.

#producto(5,2)= a+producto(a,b-1) -> si (b==0 Return 0)
def producto(a,b):
    if b==0:
        return 0
    else:
        return a+producto(a,b-1) 

print(f"El producto de 5 y 3 es: {producto(5,3)} ")