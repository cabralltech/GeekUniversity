def validate(fn):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return fn(*args, **kwargs)
            except ValueError:
                print('\033[31mERRO! Dados inválidos\033[m')
    return wrapper


def go_on():
    while True:
        ans = input('Deseja cadastrar outro produto? ').strip().upper()[0]
        if ans not in 'NS':
            print('\033[31mERRO! Resposta inválida\033[m')
        else:
            return ans


class Produto:
    @validate
    def __init__(self):
        self.nome = input('Produto: ').title().strip()
        self.preco = float(input('Preço: ').replace(',', '.'))

    def __repr__(self):
        return f'{self.nome:<20} R$ {self.preco}'


# with open('produtos.txt', 'w') as prod:
#     while True:
#         produto = Produto()
#         prod.write(f'{repr(produto)} \n')
#         if go_on() == 'N':
#             break
with open('produtos.txt') as pr:
    lista = pr.read()
soma = sum(float(x) for x in lista.split() if x[0].isnumeric())
print('- ' * 5)
print(f'A total dos produtos é R$ {soma}')