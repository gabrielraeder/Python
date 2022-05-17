print('\033[7;97;40m---MÉDIA---\033[m')
print('')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if n1 <= 10.0 and n2 <= 10.0:
    print('A média final do aluno é {:.1f} e ele está:'.format(media))
    if media < 5.0:
        print('\033[1;97;41m REPROVADO \033[m')
    elif 5.0 <= media <= 6.9:
        print('\033[1;30;43m RECUPERAÇÃO \033[m')
    elif 7.0 <= media <= 10.0:
        print('\033[1;97;42m APROVADO \033[m')
else:
    print('ERRO NA LEITURA DA NOTA')