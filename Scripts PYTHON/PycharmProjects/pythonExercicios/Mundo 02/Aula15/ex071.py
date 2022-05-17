valor = int(input('Quanto deseja sacar? R$ '))
cinq = valor // 50
sobra = valor % 50
if cinq > 1:
    print(f'{cinq} cédulas de R$50.00')
elif cinq == 1:
    print(f'{cinq} cédula de R$50.00')
vinte = sobra // 20
sobra = sobra % 20
if vinte > 1:
    print(f'{vinte} cédulas de R$20.00')
elif vinte == 1:
    print(f'{vinte} cédula de R$20.00')
dez = sobra // 10
sobra = sobra % 10
if dez > 1:
    print(f'{dez} cédulas de R$10.00')
elif dez == 1:
    print(f'{dez} cédula de R$10.00')
um = sobra // 1
if um > 1:
    print(f'{um} cédulas de R$1.00')
elif um == 1:
    print(f'{um} cédula de R$1.00')