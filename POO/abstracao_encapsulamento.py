class Conta:

    contador = 400

    def __init__(self, titular, limite, saldo):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__limite = limite
        self.__saldo = saldo
        Conta.contador += 1

    def extrato(self):
        return f'O saldo da conta de {self.__titular} é de {round(self.__saldo, 1)} com limite de {self.__limite}'

    def depositar(self, valor):
        if valor < 0:
            print('Depósitos somente de valores positivos')
        else:
            self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo < valor:
            print('Saldo insuficiente')
        elif valor < 0:
            print('Valor deve ser positivo')
        else:
            self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        # Retirar valor do saldo
        self.sacar(valor)
        # Adcionar valor na conta de destino
        conta_destino.depositar(valor)
        # Taxa de transferência
        self.__saldo -= 10


c1 = Conta('Gustavo Cabezita', 1500, 345.78)
c2 = Conta('Mhirley Lopes', 1500, 54.90)
c1.transferir(200, c2)
print(c1.extrato())
print('- ' * 15)
print(c2.extrato())
