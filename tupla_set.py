dias = ('lun','mar', 'mier')
#dias [2] = 'jue' NO SE PUEDE MUTAR UNA TUPLA 
dias = tuple(list(dias) + ['jue'])
print(dias)

votacion=['Trump','Putin','Biden','Biden','Putin','Trump','Biden','Pedro Pascal', 'Biden','Pikachu']

#votacion=list(set(votacion))
votacion.sort()
print(votacion) 

resultados = {}
for voto in votacion:
  if voto in resultados.keys():
    resultados[voto] += 1
  else:
    resultados[voto] = 1
    
#voto.sort()

print(resultados)  

'''
resultados = {
  'Trump' : 3,
  'Biden': 4,
  'Putin' : 1,
  'Pedro Pascal': 1,
  'Pikachu': 1
  }
'''
