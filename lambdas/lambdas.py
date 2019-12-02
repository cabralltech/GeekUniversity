def funcao_quadratica(a, b, c):
    """Returns a quadratic function: f(x) = a * x ** 2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c


autores = ['Fiodor Dostoievski', 'Liev Tolstoi', 'Mikhail Bugalkov',
           'Andrei Tarkovski', 'Nikolai Gogol', 'Maksim Gorki']
aut = sorted(autores, key=lambda sb: sb.split(' ')[-1])
print(aut)

teste = funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

