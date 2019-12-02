# def horas(hora=0, minuto=False):
#     horas.hora = hora
#     return f'{hora}:{minuto}'
#
#
# print(dir(horas))
# print(horas.__defaults__[0])


def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        print(a)
        array = list(zip(*array))
        print(array)
        array = reversed(array)
    return a


array1 = [[x for x in range(3)] for y in range(3)]
ans = []
ans.extend(array1)
print(ans)