
n = int(input('informe o 1º termo: '))
r = int(input('Informe a razão da P.A.: '))
decimo = n + (10-1) * r                 #formula para calcular o enesimo termo da PA = primeiro + (n-1) * razão
for c in range(n, decimo + r, r):
    print(c, end=' - ')
print('FIM!')