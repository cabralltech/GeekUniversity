from random import choice


def make_me_laugh(pessoa):
    def laugh():
        laughter = choice(['hahaha', 'lololo'])
        return f'{pessoa}, {laughter}'
    return laugh


p = 'Mhirley'
rindo = make_me_laugh(p)
print(rindo())
