lista = []
par = []
impar = []
for c in range(0,7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
lista.append(par[:])
lista.append(impar[:])
print(lista)
print(f'Os pares são {lista[0]} e os impares {lista[1]}')