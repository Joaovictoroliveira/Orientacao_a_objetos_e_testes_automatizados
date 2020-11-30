from modulo_funcoes.identificacao_de_funcoes import *

minha_lista = []

print("Preenchendo")
preencherInventario(minha_lista)

print("Exibindo")
exibirInventario(minha_lista)

print("Pesquisando")
localizarPorNome(minha_lista)

print("Alterando")
depreciarPorNome(minha_lista, 20)

print("Excluindo")
print(excluirPorSerial(minha_lista))
exibirInventario(minha_lista)

print("Resumindo")
resumirValores(minha_lista)

