frase = str(input('Digite uma frase: ')).strip().upper()
a = frase.split()
frase = (''.join(a))
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[letra]
print(frase, inverso)
if frase == inverso:
    print('PALÍNDROMO!')
else:
    print('Não é palíndromo.')