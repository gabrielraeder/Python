frase = str(input('Digite uma frase: ')).upper().strip()  #upper para deixar tudo em maiusculas e strip para remover possiveis espaços errados
print('A letra A aparece {} na frase acima.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))  # +1 pois a contagem do python inicia em 0
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))  # RFIND pois busca iniciando a contagem apartir da direita