import os # Importa o módulo (ou biblioteca) os - Integra os programas e recursos do sistema operacional

print("#" * 60)
ip_ou_host = input("Digite o IP ou host a ser verificado: ") # Criando uma variável que vai receber do usuário um IP

print("-" * 60)
os.system('ping -n 4 {}'.format(ip_ou_host)) # Chamando system da biblioteca os e chamando o comando ping
print("-" * 60)
