from time import sleep
import emoji
for c in range(10, 0, -1):
    print(c, end=' -> ')
    sleep(.25)
print(emoji.emojize(':fireworks:'))
print('KaBUUUMMM!!!')
