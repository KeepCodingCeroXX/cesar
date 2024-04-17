alfabeto = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def cifrar(frase, distancia):
    """
    Crear una cadena vacia 
    Para cada letra de frase
        Buscar la posicion de la letra en alfabeto
        posicion += distancia
        añado a la cadena la letra en la nueva posicion
    devolver cadena
    """