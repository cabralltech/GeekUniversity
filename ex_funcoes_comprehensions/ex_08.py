def hyp(cat1, cat2):
    """
    Returns the hypotenuse by the square root of the sum of the square of the catheti given
    :param cat1: float
    :param cat2: float
    :return: hypotenuse with one decimal floating point
    """
    hipo = ((cat1 ** 2) + (cat2 ** 2)) ** 0.5
    return f'O valor da hipotenusa é {hipo:.1f}'


# Programa Principal
a = float(input('Primeiro Cateto: '))
b = float(input('Segundo Cateto: '))
print(hyp(a, b))