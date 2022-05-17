print('#'*5, '\033[7;41mMÉDIA ESCOLAR\033[m', '#'*5)
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
print('')
if m < 5.0:
    print('REPROVADO')
elif 5.0 <= m <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
print('')
print('#'*10, '\033[7;41mFIM\033[m', '#'*10)
