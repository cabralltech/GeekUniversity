from multiprocessing import Pool
from time import time

CONTADOR = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time()
    p1 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    p2 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    fim = time()
    print(f'Tempo execução {fim - inicio}')