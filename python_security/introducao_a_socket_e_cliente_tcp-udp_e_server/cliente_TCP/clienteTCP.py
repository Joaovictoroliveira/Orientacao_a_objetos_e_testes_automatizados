import socket # fornece acesso á interface de rede de baixo nível
import sys # módulo para manipular diferentes partes do ambiente em tempo de execução

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("A conexão falhou")
        print("Erro: {}".format(error))
        sys.exit()

    print("Socket criado com sucesso!")

    hostAlvo = input("Digite o Host ou IP a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso no host: " + hostAlvo + " e na porta: " + portaAlvo)
        s.shutdown(2)
    except socket.error as error:
        print("Não foi possível conectar no host: " + hostAlvo + " na porta: " + portaAlvo)
        print("Erro: {}".format(error))
        sys.exit()

if __name__ == "__main__":
    main()
