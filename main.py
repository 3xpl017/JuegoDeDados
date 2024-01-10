import random, os, time
from colorama import Fore, Back

numeros = [1, 2, 3, 4, 5, 6]

aleatorio = random.choice(numeros)

generados = random.randint(1, 6)

os.system('clear')

while True:
    if aleatorio == generados:
        print(Fore.GREEN + f'[!] Los números {generados} y {aleatorio} coinciden.\n')
        break
        os.system('clear')

    else:
        print(Fore.RED + f'[!] Los números {generados} y {aleatorio} no coinciden.')
        generados = random.randint(1, 6)
        aleatorio = random.choice(numeros)
