n = 0
cont = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print(f'A soma vale {s}.')  #FSTRING /atualização do python em relação ao inicio do curso PYTHON 3.6+