valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}º valor: ')))
    if c == 0: #define que o primeiro valor digitado seja o abaixo pois o primeiro digitado é o c=0, primeira posição
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'você digitou os valores {sorted(valores)}')
print(f'O maior valor é {maior} e está nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}', end='... ')
print(f'\nO menor valor é {menor} e está nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}', end='... ')


