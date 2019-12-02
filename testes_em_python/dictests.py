def soma(a, b):
    """

    :param a: int
    :param b: int
    :return: soma de a + b

    >>> soma(3, 5)
    8

    >>> soma(8, 17)
    25
    """
    return a + b

def duplicar(valores):
    """

    :param valores: lista
    :return: valores duplicados

    >>> duplicar([1, 2, 3,])
    [2, 4, 6]

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * x for x in valores]


lista = [True, None]
print(duplicar(lista))
