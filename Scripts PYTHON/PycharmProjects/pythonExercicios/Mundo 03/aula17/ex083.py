exp = str(input('Digite a expressão: '))  #toda string já é uma lista
pilha = []
for simb in exp: #para cada item(simb) na lista (exp)
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão é CORRETA!')
else:
    print('A expressão está errada.')