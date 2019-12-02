cms = float(input('Centímetros: '))
pol = cms / 2.54
print(f'{cms}cm -› {pol:.1f}pol')

pol = float(input('Polegadas: '))
cms = pol * 2.54
print(f'{pol}pol -› {cms:.1f}cm')
