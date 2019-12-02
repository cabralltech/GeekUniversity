import datetime

data_compra = datetime.date.today()
regra_boleto = datetime.timedelta(days=3)
data_venc = data_compra + regra_boleto
print(data_compra)
print(data_venc)