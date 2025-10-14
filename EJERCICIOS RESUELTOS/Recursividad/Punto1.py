# 1. Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.

#Fibonacci(n)= Fibonacci(n-1) + Fibonacci(n-2) -> si (n==0 or n==1 Return a)
def Fibonacci(n):
    if (n==0 or n==1):
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(f"El valor en la sucecion de Fibonacci del numero 8 es: {Fibonacci(8)} ")