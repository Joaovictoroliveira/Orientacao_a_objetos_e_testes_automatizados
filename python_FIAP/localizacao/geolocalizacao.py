import geocoder

localizacao_atual = geocoder.ip('me')
print(localizacao_atual.address)

