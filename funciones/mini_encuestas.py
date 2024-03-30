preguntas = [
  '¿Que opina de Tangananica?',
  '¿Votaría por Mario para Core?, y para hardCORE',
  '¿Somos el curso favorito del profe?'
]

respuestas = []
dicc_respuestas = {
  '1': 'Muy en desacuerdo',
  '2': 'En desacuerdo',
  '3': 'Ni de acuerdo ni en desacuerdo',
  '4': 'De acuerdo',
  '5': 'Muy de acuerdo'  
}

def preguntar (pregunta):
  print(pregunta)
  opciones = '''
    Seleccione una de las siguientes:
    1. Muy en desacuerdo
    2.En desacuerdo
    3.Ni de acuerdo ni en desacuerdo
    4. De acuerdo
    5. Muy de acuerdo
  '''
  eleccion =  input(opciones)
  respuestas = dicc_respuestas.get(eleccion, 'N.S.N.R')
  
  respuestas.appenend({
    'pregunta': pregunta,
    'respuesta': respuesta
    })

def main():
  for pregunta in preguntas:
    preguntar(pregunta)
  print(respuestas)
  
main()