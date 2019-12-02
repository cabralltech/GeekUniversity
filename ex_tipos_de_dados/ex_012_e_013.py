kms = float(input('Quilômetros: '))
miles = kms / 1.61
print(f'{kms}km -› {miles:.2f}mi')

miles = float(input('Milhas: '))
kms = miles * 1.61
print(f'{miles}mi -› {round(kms, 1)}km')
