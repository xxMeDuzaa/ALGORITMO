#6. Dada una secuencia de caracteres, obtener dicha secuencia invertida.
#caracter(lista)= lista[-1]+caracter(lista[0:-1]) -> si not lista Return "" (vacio)
def caracter(lista):
    if not lista: #Si la cadena esta vacia, devuelve vacio.
        return ""
    else:
        return lista[-1] + caracter(lista[0:-1])

print(caracter("Hola"))