from random import randint
cont = 0
print('Sou seu computador...\nAcabei de pensar em número de 0 a 10.\nConsegue adivinha-lo??')
pc: int = randint(0, 10) #randint não ignora o ultimo valor
acertou = False
while not acertou:
    j = int(input('Qual é o seu palpite? '))
    cont = cont + 1
    if j == pc:
        acertou = True
    else:
        if j > pc:
            print('MENOS! Tente novamente.')
        else:
            print('MAIS! Tente novamente.')
        print('='*25)
if cont == 0:
    print('WOW! Acertou de primeira! Parabéns!')
elif cont == 1:
    print('Acertou! Foram somente {} tentativas para acertar.'.format(cont))
else:
    print('Finalmente acertou! Foram {} tentativas para acertar.'.format(cont))
