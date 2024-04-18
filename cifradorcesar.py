
from cesar import cifrar, alfabeto
"""
El programa me pide una frase
despues me pide una distancia
y al final me imprime mi frase cifrada

"""

frase = input("Dime algo: ")
distancia = int(input("Dime la distancia: "))
frase_cifrada = cifrar(frase, distancia)
print(frase_cifrada)

print(alfabeto)

