n = input('Digite algo: ')
print('O tipo primitivo deste valor é:', type(n))
print('{} só tem espaços?'.format(n), n.isspace())
print('{} é um número?'.format(n), n.isnumeric())
print('{} é alfabético?'.format(n), n.isalpha())
print('{} é alfanumérico?'.format(n), n.isalnum())
print('{} está em maiúsculas?'.format(n), n.isupper())
print('{} está em minúsculas?'.format(n), n.islower())
print('{} está capitalizada?'.format(n), n.istitle())
