salario = float(input('Salário-base: '))
grat = salario * 0.05
imp_ren = salario * 0.07
total = salario + grat - imp_ren
print(f'Para um salário-base de R${salario:.2f}, recebe-se R${total:.2f}')
