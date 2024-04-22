import cesar

mensaje_en_claro = input("Dime algo para Elena:")
print("En origen", mensaje_en_claro)
input()

mensaje_cifrado = cesar.cifradorDidier(mensaje_en_claro)
print("Lo que viaja", mensaje_cifrado)
input()


print("En destino")
print(cesar.cifradorElena(mensaje_cifrado))