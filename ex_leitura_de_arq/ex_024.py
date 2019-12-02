import cadastro as c


class Mercadoria:
    @c.validate
    def __init__(self):
        print('- ' * 15)
        self.cod = int(input('Código: ').strip())
        self.nome = input('Nome: ').strip().title()
        self.qtd = int(input('Quantidade: ').strip())

    def __repr__(self):
        return f'{self.cod:<5}{self.nome:<40}{self.qtd} \n'

    @c.validate
    def entrada(self):
        num = int(input('Quantidade comprada: ').strip())
        self.qtd += num
        return self.qtd

    @c.validate
    def saida(self):
        sai = int(input('Quantidade usada: ').strip())
        self.qtd -= sai
        return self.qtd


despensa = []
while True:
    merc = Mercadoria()
    print('- ' * 5)
    merc.entrada()
    merc.saida()
    despensa.append(merc)
    if c.go_on() == 'N':
        break
with open('despensa.bin', 'w+b') as des:
    des.write(b'LISTA PRODUTOS DESPENSA\n\n')
    for i in despensa:
        var = repr(i)
        des.write(var.encode())
