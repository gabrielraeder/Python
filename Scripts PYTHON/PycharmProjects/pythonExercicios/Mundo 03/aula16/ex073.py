tupla = ('ManCity', 'Liverpool','Chelsea','West Ham','ManUTD',
         'Arsenal','Tottenham','Wolves','Brighton','Leicester City',
         'Aston Villa','Southampton','Crystal Palace','Brentford','Leeds',
         'Everton','Newcastle','Norwich','Watford','Burnley')
print('¨'*50)
print(f'Os cinco primeiros colocados são {tupla[0:5]}.')
print('¨'*50)
print(f'Os últimos quatro são {tupla[-4:]}')
print('¨'*50)
print(f'ORDEM ALFÁBETICA: \n{sorted(tupla)}')
print('¨'*50)
print(f'O Arsenal está na {tupla.index(("Arsenal"))+1}ª posição.')
print('¨'*50)
for t in tupla:
    print(t)