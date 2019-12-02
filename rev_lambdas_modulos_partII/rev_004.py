def quad_perf(n):
    if ((n ** 0.5) / 0.01) % 10 == 0:
        return f'{n} é um quadrado perfeito'
    return f'{n} não é um quadrado perfeito'


num = int(input('Valor: '))
print(quad_perf(num))

