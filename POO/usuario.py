from passlib.hash import pbkdf2_sha256 as cryp
from validacao import validar


@validar(ValueError)
def entrada_usuario():
        nome = input('Nome: ').strip().title()
        sobrenome = input('Sobrenome: ').strip().title()
        email = input('E-mail: ').strip().lower()
        senha = input('Senha: ').strip()
        while True:
            print('- ' * 5)
            confirma_senha = input('Confirme a senha: ').strip()
            if senha == confirma_senha:
                return Usuario(nome, sobrenome, email, senha)
            else:
                print('Senha não confere')


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        return f'Temos {cls.contador} usuários no sistema'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self._gera_usuario()}')


    def nome_completo(self):
        """Retorna o nome completo do usuário"""
        return f'{self.__nome} {self.__sobrenome}'

    def _gera_usuario(self):
        return self.__email.split('@')[0]

    def checa_acesso(self, user, pwd):
        """Checa email e senha para permitir acesso"""
        if user == self._gera_usuario() and cryp.verify(pwd, self.__senha):
            return 'Acesso permitido'
        return 'Acesso negado'


user1 = entrada_usuario()
print('- ' * 15)
email = input('Digite o nome de usuario: ').strip().lower()
senha = input('Senha: ').strip()
print(user1.checa_acesso(email, senha))
print('- ' * 15)
print(Usuario.conta_usuarios())
