import os
import tempfile


# with tempfile.TemporaryDirectory() as temp:
#     print(f'Criei um diretório temporário {temp}')
#     with open(os.path.join(temp, 'arquivo_teste.txt'), 'w') as file:
#         file.write('Este é um arquivo teste')

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Mhirley Lopes is studying\n')
    tmp.seek(0)
    print(tmp.read())
