from csv import reader

with open('Build 2.0.0.19129 - Visualizador da INDE - Infraestrutura Nacional de Dados Espaciais.csv') as file:
    csv_reader = reader(file)
    for cidade in csv_reader:
        print(cidade)
