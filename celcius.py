
ingreso = int(input ('ingrese la temperatura en grados Celsius: '))
farenheit = ingreso * 1.8 + 32
kelvin = ingreso + 273.15

print('la temperatura en grados Kelvin es: ', kelvin)
print('la temperatura en grados Farenheit es: ', farenheit)



'''Transforma de °Celcius a °Farenheit y a °Kelvin'''
# 1. Pedimos al usuario la temperatura en Celcius
celcius = input('ingrese la temperatura en Celcius: ')
# 2. Transformamos a FLOAT (numeros decimales)
celcius = float(celcius)
# 3 Calculo la temperatura en Farenheit
fahr = 32 + (1.8 * celcius)
# 4. Calculo la temperatura en Kelvin
kelvin = celcius + 273.1
# 5. Volvemos a transformar todo a string
celcius = str(celcius)
fahr = str(fahr)
kelvin = str(kelvin)
# 6. Crear el mensaje concatenando los strings
mensaje = 'Los  ' + celcius + '°C son equivalentes a ' + fahr + '°F y a ' + kelvin + '°K'
# 7. Imprimimos el mensaje en consola
print(mensaje)