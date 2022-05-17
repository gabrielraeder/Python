from time import sleep
print('\033[1;97;41mº'*10, '\033[1;97;41mRADAR DE VELOCIDADE', '\033[1;97;41mº\033[m'*10)
print()
v = int(input('Informe a velocidade do veículo: '))
if v > 80:
    print('\033[1;31mLimite de velocidade de 80km/h EXCEDIDO!\nVelocidade registrada: {}km/h\nMULTA A PAGAR NO VALOR '
          'DE:\033[m'.format(v))
    sleep(1)
    print('          \033[1;97;41mR${:.2f}\033[m'.format((v-80)*7))
print('\033[1;32mTenha um bom dia! Dirija com segurança!\033[m')