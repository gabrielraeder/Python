def parimpar(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
print(parimpar(num))
print('~'*35)
if parimpar(num):
    print('É par!')
else:
    print('Não é par.')
