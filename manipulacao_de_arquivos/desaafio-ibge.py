import csv
from urllib import request

with open('desafio-ibge.csv') as entrada:
    leitura = csv.reader(entrada, delimiter=',')
    
    for registro in leitura:
        print('{}, {}'.format(registro[3], registro[8]))

#Solução do professor
#!/usr/local/bin/python3
# def read(url):
#     with request.urlopen(url) as entrada:
#         print('Baixando o CSV...')
#         dados = entrada.read().decode('latin1')
#         print('Download completo!')

#         for cidade in csv.reader(dados.splitlines()):
#             print(f'{cidade[8]}: {cidade[3]}')

# if __name__ == '__main__':
#     read('http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
