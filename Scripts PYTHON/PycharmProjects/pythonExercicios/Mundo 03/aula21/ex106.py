from time import sleep
c = ('\033[m',
     '\033[0;97;41m',   # vermelho
     '\033[0;97;42m',   # verde
     '\033[0;97;43m',   # amarelo
     '\033[0;97;44m',   # azul
     '\033[0;97;45m',   # roxo
     '\033[0;97;46m',   # ciano
     '\033[0;97;47m',   # cinza
     '\033[0;30;107m',  # branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando\'{com}\'', 5)
    print(c[8],end='')
    help(com)
    print(c[0],end='')
    sleep(1)

def titulo(msg, cor=0):         #função para formatação do programa (cores etc)
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
