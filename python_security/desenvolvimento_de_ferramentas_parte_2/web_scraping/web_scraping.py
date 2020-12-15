from bs4 import BeautifulSoup
import requests

# site está recebendo o conteúdo da requisição http do site fornecido
site = requests.get('https://www.climatempo.com.br/').content

# soup está baixando o html do site fornecido
soup = BeautifulSoup(site, 'html.parser')

# transforma html em string e exibi ele
print(soup.prettify())

print(soup.title.string)
