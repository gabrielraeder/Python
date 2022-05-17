valor = int(input('Quanto deseja sacar? R$ '))
cinq = valor // 50
sobra = valor % 50
if cinq == 1:
    print(f'Total de {cinq} cédula de R$50')
elif cinq > 1:
    print(f'Total de {cinq} cédulas de R$50')
else:
    print('')
vinte = sobra // 20
sobra = sobra % 20
if vinte == 1:
    print(f'Total de {vinte} cédula de R$20')
elif vinte > 1:
    print(f'Total de {vinte} cédulas de R$20')
else:
    print('')
dez = sobra // 10
sobra = sobra % 10
if dez == 1:
    print(f'Total de {dez} cédula de R$10')
elif dez > 1:
    print(f'Total de {dez} cédulas de R$10')
else:
    print('')
um = sobra // 1
if um == 1:
    print(f'Total de {um} cédula de R$1')
elif um > 1:
    print(f'Total de {um} cédulas de R$1')
else:
    print('')