from cesar import cifrar
def test_cesar_una_letra():
    assert cifrar("H", 1) == "I"


def test_crear_cifrador():
    cifrar3 = crearCesar(3)
    descifrar3 = crearCesar(-3)

    assert cifrar3("H") == "K"
    assert descifrar3("K") == "H"

def otra_funcion():
    assert "lolailo" == "lere"