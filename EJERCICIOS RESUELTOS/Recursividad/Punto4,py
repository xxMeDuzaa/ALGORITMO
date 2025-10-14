#Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente.
#potencia(a,b)= a*producto(a,b-1) -> si (b==0) Return 1 / (b==1) Return a
def potencia(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        return a*potencia(a,b-1) 
    
print(f"La potencia entre la base 5 y el exponente 2 es: {potencia(5,2)}")