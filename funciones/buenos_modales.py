def buenos_modales(nombre = 'anonimo'):         #Función para llamar los modales
#saludo, adios =  buenos_modales(nombre) #esto es un atajo a lo de abajo


  hola = 'buenos dias ' + nombre    #Concatena el mensaje de bienvenida
  chao = 'nos vemos ' +  nombre     #Concatena el mensaje de despedida
  return hola, chao    


#desempaquetar
saludo, adios =  buenos_modales() #esto es un atajo a lo de abajo
#saludo, adios =  buenos_modales('Camila') 
'''
palabras =  buenos_modales('Matias')
saludo, adios = buenos_modales('Camila')  
adios = palabras[1]
'''
print (saludo)
print (adios)

