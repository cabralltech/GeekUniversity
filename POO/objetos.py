class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf


class ContaCorrente:

    contador = 495008

    def __init__(self, limite, saldo, cliente):
        self.__numero_conta = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero_conta

    def mostra_nome(self):
        return f'O cliente {self.__cliente._Cliente__nome}'  # modo não aconselhável de acesso


cli1 = Cliente('Mhirley Lopes', '123.456.789-00')
conta = ContaCorrente(2000, 158.90, cli1)
print(conta.mostra_nome())
