print('{:=^50}'.format(' PAGAMENTOS '))
preço = float(input('Preço das compras? R$ '))
pagamento = int(input('''FORMA DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
 Qual é a opção? '''))
if pagamento >=1 and pagamento <=4:
    if pagamento == 1:
        total = preço - preço*10/100
    elif pagamento == 2:
        total = preço - preço*5/100
    elif pagamento == 3:
        total = preço
        parc = total / 2
        print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parc))
    elif pagamento == 4:
        total = preço + preço*20/100
        parc = int(input('Quantas parcelas?'))
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parc, (total/parc)))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
else:
    print('ERRO! FORMA DE PAGAMENTO INVÁLIDA.')
