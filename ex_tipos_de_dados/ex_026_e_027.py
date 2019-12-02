metros = float(input('Metros quadrados: '))
hectares = metros * 0.0001
print(f'{metros}m2 -› {hectares:.1f}ha')

hectares = float(input('Hectares: '))
metros = hectares * 10000
print(f'{hectares}ha -› {metros:.1f}m2')
