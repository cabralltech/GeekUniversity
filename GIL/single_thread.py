import time
from threading import Thread

CONTADOR = 50000000


def contagem_regressiva(valor):
    while valor > 0:
        valor -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo de execução {fim - inicio}')