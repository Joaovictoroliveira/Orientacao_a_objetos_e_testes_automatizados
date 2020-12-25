# def palindromo(numero):
#     numero_invertido = numero[::-1]
    
#     if numero == numero_invertido:
#         return "{} eh um numero palindromo".format(numero)
#     else:
#         return "{} nao eh um numero palindromo".format(numero)

# numero = input()
# print(palindromo(numero))

numero = input()
aux = numero
reversao = ''

while len(aux) != 0:
    reversao = reversao + aux[-1]
    aux = aux[:-1]
    
if reversao == numero:
    print("{} eh um numero palindromo".format(numero))
else:
    print("{} nao eh um numero palindromo".format(numero))
