#12. Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos número entero.
#euclides(a,b)=euclides(b,a % b) -> Si (b==0) Return a
def euclides(a, b):
    
    if b == 0: 
        return a 
    else:
        return euclides(b, a % b) #b es el nuevo a y (a % b) es el nuevo b, el valor de (a % b) seria el residuo

print(f"El MCD de 156 y 120 es: {euclides(156,120)}")