from random import randint

vetor = (randint(0, 50) for x in range(10))
with open('numeros_binarios.txt', 'a') as bina:
    for i in vetor:
        bina.write(f'{i:.<15}{bin(i)[2:]}\n')

