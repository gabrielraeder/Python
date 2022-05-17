from time import sleep
print('#'*24)
print('      \033[1;32mPAR\033[m ou \033[1;31mÍMPAR\033[m')
print('#'*24)
n = int(input('Me diga um número qualquer: '))
if (n % 2) == 0:
    print('O número {} é...'.format(n), end='')
    sleep(1)
    print('\033[1;32mPAR\033[m')
else:
    print('O número {} é...'.format(n), end='')
    sleep(1)
    print('\033[1;31mÍMPAR\033[m')