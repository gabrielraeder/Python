frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.split()
junto = ''.join(frase)
inverso = ''
inverso = junto[::-1]

'''for c in range (len(junto)-1, -1, -1):
    inverso = inverso + junto[c]'''

print(junto , '/', inverso)
if inverso == junto:
    print('\033[1;32;40m PALíNDROMO! \033[m')
else:
    print('Não é um palíndromo.')