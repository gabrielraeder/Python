from time import sleep
num = int(input('Digite um número inteiro: '))
base = int(input('Escolha uma das bases para conversão:\n [1] Converter para BINÁRIO\n [2] Converter para OCTAL\n ['
                 '3]Converter para HEXADECIMAL\nSua opção: '))
if base == 1 or base == 2 or base == 3:
    print('CALCULANDO...')
    sleep(1)
    print('...')
    sleep(1)
if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:])) #[2:] FATIAMENTO
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')
print('')
print('\033[4;30;107m---ENCERRADO---\033[m')