def funcao(b):
    global a  # substituirá o valor global de A
    a = 8
    b = b + 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
funcao(a)
print(f'A global vale {a}')