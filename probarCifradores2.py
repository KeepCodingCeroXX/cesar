from cesar import crearParejaLimitada

d = int(input("Que distancia quieres"))

encryptor, decryptor = crearParejaLimitada(d, 2)

for i in range(3):
    print(i+1, "vez")
    input()
    mensaje_en_claro = input("Dime algo para Elena:")
    print("En origen", mensaje_en_claro)
    input()

    mensaje_cifrado = encryptor(mensaje_en_claro)
    print("Lo que viaja", mensaje_cifrado)
    input()


    print("En destino")
    print(decryptor(mensaje_cifrado))



