#9. Implementar una función para calcular el logaritmo entero de número n en una base b. 
# Recuerde que: Logᵦ(n/b)= logᵦ n + logᵦ b
#logaritmo_entero(n,b)= 1+logaritmo_entero(n//b,b) -> si (n<b) Return 0

def logaritmo_entero(n,b):
    if n < b: 
        return 0
    else:
        return 1 + logaritmo_entero(n//b,b) 
    #Vamos dividiendo n por b, y contando cuentas veces podemos hacerlo antes de que se vuelva menor que b

print(f"El logaritmo entero de numero 80 en una base 3 es: {logaritmo_entero(80,3)}") 
# Salida: 3, porque 3^3 = 27 y 3^4 = 81 > 80 | ACA SERIE LA FORMULA 3^x=80 SIENDO LO MISMO QUE Log₃80=x|