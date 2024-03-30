##                                  Funcion primeros auxilios 
'''
------------------------------------------------------------------------------------------------------------------------

En cualquier momento puede haber una emergencia y hay que estar preparados ¿sabrías cómo reaccionar en caso de 
que alguien necesite de primeros auxilios?
Es muy probable que mucha gente no conozca cuáles son los pasos a seguir en caso de emergencia. 
Es por eso que se le solicita construir una aplicación que permita indicar los pasos a seguir ante una emergencia. 
Debido a que no se espera que usted sea un experto en el tema se le provee de un diagrama que explica 
las distintas instancias a la que se está sometido durante una emergencia.
-------------------------------------------------------------------------------------------------------------------------
'''
resp_estim = input('¿Estás respondiendo a estímulos? (s/n): ')

if resp_estim == 's':
    print('Valorar la necesidad de llevarlo al hospital más cercano')
else:
    print('Debe abrir la vía aérea')
    respira = input('¿Respira? (s/n): ')

    if respira == 's':
        print('Administrar 5 ventilaciones y llamar a la ambulancia')
        llega_ambulancia = False

        while not llega_ambulancia:
            signos_vitales = input('¿Tiene signos vitales? (s/n): ')

            if signos_vitales == 's':
                print('Reevaluar a la espera de la ambulancia')
            else:
                print('Administrar RCP hasta que llegue la ambulancia')

            llega_ambulancia = input('¿Llegó la ambulancia? (s/n): ')

            if llega_ambulancia == 's':
                llega_ambulancia = True
            else:
                llega_ambulancia = False

print('Fin primeros auxilios')