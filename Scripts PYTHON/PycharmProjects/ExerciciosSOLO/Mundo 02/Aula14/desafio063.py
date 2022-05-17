print('++++FIBONACCI++++')
n = int(input('Digite quantos elementos quer ver: '))
t1 = 0
t2 = 1
cont = 3
print('{} - {} - '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    if cont < n:
        print('{}'.format(t3), end=' - ')
    else:
        print('{}'.format(t3))
    t1 = t2
    t2 = t3
    cont = cont + 1