def meu_for(iteravel):
    it  = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


nome = 'mhirley'.upper()
meu_for(nome)
print('- ' * 15)
for num in Contador(1, 6):
    print(num, end=' ')

