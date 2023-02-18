"""
Cree una función en Python que determine si una secuencia de caracteres es un palíndromo.
 La función debe retornar falso o verdadero (Booleanos no string).

Casos de prueba:
- palindromo(“race car”) debería retornar True
- palindromo(“not a palindrome”) debería retornar False
- palindromo(“A man, a plan, a canal. Panama”) debería retornar True
- palindromo(“never odd or even”) debería retornar True
- palindromo(“nope”) debería retornar False
- palindromo(“almostomla”) debería retornar False

"""

def polindromo (palabra):
    palabra = palabra.lower().replace(" ","").replace(",","").replace(".","")
    if palabra == palabra[::-1]:
        return True
    else:
         return False

print (polindromo("race car"))
print ( polindromo("not a palidrome"))
print (polindromo("A man, a plan, a canal. Panama")) 
print (polindromo("never odd or even")) 
print (polindromo("nope"))
print (polindromo("almostomla"))
    
""" 
Escenario 3
Dada una frase o palabra cuente el número de apariciones de cada carácter y retorne un diccionario donde las llaves son los caracteres
 y los valores es el número de veces que aparece el carácter en la frase o palabra.
"""
"""def obtener (diccionario):
    caracteres = 0 
    apariciones = 0
    texto=input("escriba una palabra o frase:  ")"""

  
def contador (n):
    resultado = {}
    for i in n:
        if i not in resultado:
            resultado[i] = 1
        else:
            resultado[i] += 1
    return resultado
    

print(contador("el real madrid es el mejor "))

   
