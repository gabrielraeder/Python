n = int(input(' >>> Digite um número: '))
cont = 0
soma = 0
while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input('[999] ENCERRAR >>> Digite um número: '))
print('~'*50)
if cont == 2:
    print('Foi digitado somente um número e a soma é {}.'.format(soma))
else:
    print('Foram digitados {} números e a somas destes é {}.'.format(cont, soma))
print('~'*50)
print('ENCERRADO')