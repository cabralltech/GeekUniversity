from collections import Counter
from random import randint
lista = []
for i in range(10):
    num = randint(1, 5)
    lista.append(num)
print(lista)
print(Counter(lista).most_common(3))

string = 'paralelepipado'
resp = Counter(string)
print(resp)

texto = """A Wikipédia é um projeto de enciclopédia colaborativa, 
universal e multilíngue estabelecido na internet sob o princípio wiki. 
Tem como propósito fornecer um conteúdo livre, objetivo e verificável​​, 
que todos possam editar e melhorar. O projeto é definido pelos princípios 
fundadores. O conteúdo é disponibilizado sob a licença Creative Commons 
BY-SA e pode ser copiado e reutilizado sob a mesma licença — mesmo para fins 
comerciais — desde que respeitando os termos e condições de uso."""

texto = texto.split()
words = Counter(texto)
print(words.most_common(5))
