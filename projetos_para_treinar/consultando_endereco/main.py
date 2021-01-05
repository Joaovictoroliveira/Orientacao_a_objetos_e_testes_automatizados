import requests

def main():
    print("*** CONSULTA CEP ***\n")
    cep_input = input("Digite o CEP para a consulta: ")

    if len(cep_input) != 8:
        print("Quantidade de digitos invalida")
        exit()

    request = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print("======= CEP encontrado ======")
        print(f"CEP: {address_data['cep']}")
        print(f"Logradouro: {address_data['logradouro']}")
        print(f"Bairro: {address_data['bairro']}")
        print(f"Cidade: {address_data['localidade']}")
        print(f"Estado: {address_data['uf']}")
    else:
        print("CEP invalido")

    nova_consulta = input("Deseja realizar uma nova consulta? [S/N]: ").upper()

    if nova_consulta == 'S':
        main()
    else:
        exit()

if __name__ == '__main__':
    main()
