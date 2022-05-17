import urllib.request

try:
    page = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Impossivel acessar a página.')
else:
    print('Página Pudim acessada com sucesso.')
    print(page.read())
