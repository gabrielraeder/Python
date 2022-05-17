print('\033[7;30;41m TESTE \033[m')
#print('\033[4;33;46m TESTE')
#print('\033[0;35;43m TESTE')
#print('\033[30;42m TESTE')
#print('\033[0;37;m TESTE')
#print('\033[1;30;47m TESTE')

nome = 'Gabriel'
print('Olá, prazer te conhecer {}{}{}!!!'.format('\033[4;32m', nome, '\033[m'))
a = 3
b = 5
print('Os valores são \033[35m{}\033[m e \033[33m{}\033[m'.format(a, b))

#aulas futuras:

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá, prazer te conhecer {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))