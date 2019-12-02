class Arquivo:
    def __init__(self):
        while True:
            try:
                arquivo = input('Digite um path absoluto: ')
                with open(arquivo) as arq:
                    file = arq.read()
                    break
            except FileNotFoundError:
                print('\033[31mArquivo não encontrado!\033[m Tente novamente')
        self.file = file.lower()

    def __repr__(self):
        return self.file

    def substituir(self):
        with open('new_file.txt', 'w') as nf:
            nf.write(self.file)
        with open('new_file.txt', 'r+') as new:
            res = new.read()
            new.seek(0)
            for i in res:
                if i in 'aáãeéiíoóuú':
                    new.write(i.replace(i, '*'))
                else:
                    new.write(i)
            new.seek(0)
            rest = new.read()
        return rest


arqu = Arquivo()
print(arqu.substituir())
