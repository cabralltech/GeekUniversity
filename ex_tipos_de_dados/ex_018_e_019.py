mcub = float(input('Metros cúbicos: '))
litros = 1000 * mcub
print(f'{mcub}m3 -› {litros}l')

litros = float(input('Litros: '))
mcub = litros / 1000
print(f'{litros}l -› {mcub:.2f}m3')
