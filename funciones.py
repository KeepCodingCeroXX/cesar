def sumar(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i

    return suma

def sumarDoble(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i * 2

    return suma

def sumarPor3mas27(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i * 3 + 27

    return suma

def sumarF(n, el_parametro):
    suma = 0
    for i in range(1, n + 1):
        suma += el_parametro(i)
    return suma

