#7. Desarrollar un algoritmo que permita calcular la siguiente serie: h(n)=1+1/2+1/3...+1/n
# serie(n)= 1/n+serie(n-1) ->si (n==1) Return 1
def serie(n):
    if (n==1):
        return 1
    else:
        return 1/n + 1/serie(n-1)

print(f"La serie de 4 es: {serie(4)}")