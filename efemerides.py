
'''
# Diccionario
efemerides = {'1 de enero': 'Año Nuevo',
    '27 de febrero': 'Terremoto en Chile',
    '8 de marzo': 'Día de la Mujer',
    '21 de mayo': 'Glorias Navales',
    '18 de septiembre': 'Fiestas Patrias',
    '19 de septiembre': 'Glorias del Ejercito',
    '25 de diciembre': 'Navidad'}

fecha = input("Ingrese una fecha: ").lower()

print(f'Efemérides: {efemerides.get(fecha, "No hay eventos para esta fecha")}')'''


def transformar_fecha(f_original):
  meses = {
    '1': 'enero', '2': 'febrero', '3': 'marzo', '4': 'abril', 
    '5': 'mayo', '6': 'junio', '7': 'julio', '8': 'agosto', 
    '9': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'
	}
  
  if '/' in f_original:
    f_array = f_original.split('/')
    f_ nueva = f_array[0] + '  de ' + meses[f_array[1]]
		return  f_nueva
  if '-' in  f_original:
    f_array = f_original.split('-')
    f_nueva = f_array[0] + ' de ' + meses[f_array[1]]
    return f_nueva
  if '.' in f_original.split('.')
		f_array = f_original.split('.')
    f_nueva =  f_array[0] + ' de ' + meses[f_array[1]]
    return f_nueva
    
  signo_raro 
	}