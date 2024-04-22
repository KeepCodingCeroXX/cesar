from cesar import crearPareja

d = int(input("Que distancia quieres"))

encryptor, decryptor = crearPareja(d)

mensaje_en_claro = input("Dime algo para Elena:")
print("En origen", mensaje_en_claro)
input()

mensaje_cifrado = encryptor(mensaje_en_claro)
print("Lo que viaja", mensaje_cifrado)
input()


print("En destino")
print(decryptor(mensaje_cifrado))

