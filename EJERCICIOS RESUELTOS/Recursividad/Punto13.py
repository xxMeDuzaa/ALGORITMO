#13. Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM) de dos número entero.
#MCM(a,b) = (a*b)/MCD(a,b) ->Si (mcd==0) Return 0

def euclides(a, b):
    
    if b == 0: 
        return a 
    else:
        return euclides(b, a % b) #b es el nuevo a y (a % b) es el nuevo b, el valor de (a % b) seria el residuo


def MCM(a,b):
    mcd=euclides(a,b)
    if (mcd==0): #aca no es necesario el caso base ya que en la funcion de euclides si b es cero entonces returna a, asi que el denominador no va a poder ser nunca cero en este caso.
        return "Math ERROR"
    else:
        return (a*b)/mcd

print(f"El MCM de 156 y 120 es: {MCM(156,120)}")
  