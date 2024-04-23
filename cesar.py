alfabeto = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def cifrar(frase, distancia):
    result = ""
    for letra in frase.upper():
        if letra in alfabeto:
            new_letra = alfabeto[(alfabeto.index(letra) + distancia) % len(alfabeto)]
        else:
            new_letra = letra
        result += new_letra
    return result

def cifradoElias(mensaje):
    return cifrar(mensaje, 3)

def descifradorMontse(mensaje):
    return cifrar(mensaje, -3)

def cifradorPablo(mensaje):
    return cifrar(mensaje, 5)

def descifradorFatima(mensaje):
    return cifrar(mensaje, -5)

def cifradorZoran(mensaje):
    return cifrar(mensaje, 7)

def descifradorLuis(mensaje):
    return cifrar(mensaje, -7)

def crearCifrador(distancia):
    def cifrador(mensaje):
        return cifrar(mensaje, distancia)
    
    return cifrador

cifradorDidier = crearCifrador(9)
cifradorElena = crearCifrador(-9)

def crearPareja(distancia):
    """
    """
    def cifrador(mensaje):
        return cifrar(mensaje, distancia)
    
    def descifrador(mensaje):
        return cifrar(mensaje, -distancia)
    
    return cifrador, descifrador

_cifrador, _descifrador = crearPareja(11)

def crearParejaLimitada(distancia, num_usos):
    contador =  0

    def cifrador(mensaje):
        nonlocal contador

        contador += 1
        if contador > num_usos:
            return "Cifrador agotado. Compre mas en www.secretum.com"
        return cifrar(mensaje, distancia)
    
    def descifrador(mensaje):
        return cifrar(mensaje, -distancia)
    
    return cifrador, descifrador

class Cifrador:
    def __init__(self, distance, num_usos):
        self.distancia = distance
        self.num_usos = num_usos

    def cifrar(self, mensaje):
        self.num_usos -= 1
        if self.num_usos <= 0:
            return "Pase por caja."
        
        return cifrar(mensaje, self.distancia)
    
    #def descifrar(self, )



cDidier = Cifrador(1, 1)
print(cDidier.cifrar("Hola")) # -> IPMB
print(cDidier.descifrar("ipmb")) #-> HOLA

print(cDidier.cifrar("Hola")) # -> "Pase por caja."

print(cDidier.distancia)
