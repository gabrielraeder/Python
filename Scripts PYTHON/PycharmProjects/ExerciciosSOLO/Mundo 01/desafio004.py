n = input('Digite algo:')
print(type(n))
print('palavra', n.isalpha())
print('alphanumeric', n.isalnum())
print('numero', n.isnumeric())
print('digito', n.isdigit())
print('identif', n.isidentifier())