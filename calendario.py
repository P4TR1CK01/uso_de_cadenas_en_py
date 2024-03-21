'''
calendario = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

for mes in calendario:
  print(mes)

  semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

  for dia in semana: 
    print(dia)
    año = 2024 
    print('el dia de la semana es:', dia, 'el mes del año es:', mes, 'el año es:', año)
    '''

def calendario():
  dias = int(input('ingrese la cantidad de dias: '))
  año = dias // 365 
  dias = dias % 365
  semana = dias // 7
  dias = dias % 7
  print('el año es:', año, 'la semana es:', semana, 'los dias son:', dias)
  return año, semana, dias

calendario()
