hora = float(input('Valor hora trabalhada: '))
n_hora = float(input('Número de horas: '))
bruto = hora * n_hora
total = bruto + (bruto * (10 / 100))
print(f'O valor total por {n_hora} horas trabalhadas a R$ {hora:.2f} por hora é R$ {total:.2f}')
