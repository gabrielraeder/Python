import urllib
import urllib.request


try:
    web = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site inacessivel.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
