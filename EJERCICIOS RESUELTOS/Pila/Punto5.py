#5. Determinar si una cadena de caracteres es un palíndromo.
from stack import Stack
cadena_stack = Stack()

cadena="neuquen"
def cargarPalabra(cade_stack,cadena):
   for caracter in cadena:
      cade_stack.push(caracter)
   
   
def verificarPalindromo(cad_stack,cadena):
   cadena_invertida = ""
   verificar=False
   while cad_stack.size()>0:
      cadena_invertida+=cad_stack.pop()  # voy armando la palabra invertida
      if cadena == cadena_invertida:
         verificar=True
   return verificar
      

cargarPalabra(cadena_stack,cadena)
print("Cadena ingresada: ")
cadena_stack.show()
print()
verificarP=verificarPalindromo(cadena_stack,cadena)
print(f"La cadena de caracteres es palindromo?: {verificarP}")