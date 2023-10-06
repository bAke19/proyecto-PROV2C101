import random

response = 'y'

while response == 'y':
    numero = random.randint(1,6)

    if numero == 1:
        print(' -----')
        print('|     |')
        print('|  0  |')
        print('|     |')
        print(' -----')

    if numero == 2:
        print(' -----')
        print('|     |')
        print('|0   0|')
        print('|     |')
        print(' -----')
    if numero == 3:
        print(' -----')
        print('|0    |')
        print('|  0  |')
        print('|    0|')
        print(' -----')

    if numero == 4:
        print(' -----')
        print('|0   0|')
        print('|     |')
        print('|0   0|')
        print(' -----')

    if numero == 5:
        print(' -----')
        print('|0   0|')
        print('|  0  |')
        print('|0   0|')
        print(' -----')

    if numero == 6:
        print(' -----')
        print('|0   0|')
        print('|0   0|')
        print('|0   0|')
        print(' -----')

    respuesta =input("presiona 'y' para girar otra vez y 'n' para salir:") 
    response = respuesta