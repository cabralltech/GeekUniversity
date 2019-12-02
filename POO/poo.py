class Produto:

    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


p1 = Produto('PS4', 'VideoGame', 2300)
p2 = Produto('XBOX', 'VideoGame', 4500)
print(p1.id)
print(p1.valor)

print(p2.valor)
print(p2.id)
print('- ' * 15)
print(p1.imposto)
print(p2.imposto)
print('- ' * 15)
p3 = Produto('PS5', 'VideoGame', 5600)
print(p3.id)
print('- ' * 15)
p1.peso = 5.0
print(p1.__dict__)
print(p2.__dict__)
del p1.peso
print(p1.__dict__)


