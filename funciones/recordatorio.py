'''
recordatorios = [
  ['2021-01-01', "11:00", "Levantarse y ejercitar"],
  ['2021-05-01', "15:00", "No trabajar"],
  ['2021-07-15', "13:00", "No hacer nada es feriado"],
  ['2021-09-18', "16:00", "Ramadas"],
  ['2021-12-25', "00:00", "Navidad"]
  ]

#agragamos evento del 2 de febrero a las 06:00 AM, 'Empezar el año'
eventonuevo = ["2021-02-02", "06:00", "Empezar el año"]

recordatorios = [recordatorios[0], eventonuevo] + recordatorios[1:]

print(recordatorios)
'''

eventos [
  ['2022-09-18', "20:00", "bailar cueca"],
  ['2022-01-03', "21:00", "Se te aparecio marzo"],
  ['2022-01-01', "07:00", "Salir a correr"],
]
eventos.sort(CRITERIO)

