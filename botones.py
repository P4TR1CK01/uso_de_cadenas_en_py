'''
EJERCICIO: Una app en python que, usando colorama, me pida un texto y una clase (primary, success, danger, warning), y me retorne ese boton de bootstrap con ese texto, y de ese color.
[21:32]
Ej. python botones.py ENVIAR primary
<button type="button" class="btn btn-primary">ENVIAR</button>

Enviar mensaje a #deberes-ayuda
'''
from colorama import Fore, Back, Style


texto = input("¿Qué texto quieres que tenga el botón?: \n")

clase = input("¿Qué clase quieres que tenga el botón?: \n")

boton = f'<button type="button" class="btn btn-{clase}">{texto}</button>'

print(Fore.MAGENTA + Back.WHITE + boton)

