nome = str(input('Qual é o seu nome? ')).capitalize()
if nome == 'Gabriel': #if é obrigatorio para iniciar condições
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana Dulce':
    print('Belo nome feminino!')
else: #else é opcional
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
