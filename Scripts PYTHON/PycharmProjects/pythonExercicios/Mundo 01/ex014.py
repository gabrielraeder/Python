celsius = float(input('Qual é a temperatura em ºC: '))
farenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15
print('A temperatura de {}ºC equivale a {}ºF!'.format(celsius, farenheit))
print('A temperatura de {}ºC equivale a {} K!'.format(celsius, kelvin))
