from passlib.hash import pbkdf2_sha256 as cryp


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, percentagem):
        """Retorna o valor do produto com desconto"""
        return self.__valor * (100 - percentagem)/100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


user1 = Usuario('Mhirley', 'Lopes', 'mhiloca@gmail.com', '12345')
print(user1.nome_completo())
print('- ' * 15)
# print(user1._Usuario__sobrenome) # acesso de modo desaconselhado
# print(user1._Usuario__senha)
print(user1.checa_senha('12305'))

print('- ' * 15)
p1 = Produto('PS4', 'VideoGame', 2300)
print(p1.desconto(40))
print('- ' * 15)
print(Produto.desconto(p1, 40))
