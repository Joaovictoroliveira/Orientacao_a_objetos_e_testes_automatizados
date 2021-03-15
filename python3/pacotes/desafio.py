from app.utils.gerador import novo_nome
from app.negocio import nome_existe
from app.negocio.backend import adc_nome

def main():
    while True:
        nome = novo_nome()
        if not nome_existe(nome):
            adc_nome(nome)
            break

    print(f'Criado novo nome de testes: {nome}')

main()
