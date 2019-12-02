nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

impares = [n for n in nums if n % 2]
pares = [c for c in nums if not c % 2]
print(pares)
print(impares)

aluno = {}.fromkeys(['name', 'email'], '-')
print(aluno)
cadastro = [{y: v for y, v in aluno.items()} for x in range(3)]
print(cadastro)

numeros = [1, 2, 3, 4, 5, 6]
square = {val: val ** 2 for val in numeros}
print(square)

triplos = [x * 3 for x in nums]
quadrados = [y ** 2 for y in triplos]
triple = {triplos[a]: quadrados[a] for a in range(len(triplos))}
print(triple)
