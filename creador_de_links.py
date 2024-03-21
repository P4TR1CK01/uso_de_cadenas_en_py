'''
Necesito preguntarle al usuario como se llama en la vida real y en github

''
# 1. Pido al usuario que ingrese su nombre
nombre = input('hola como te llamas: ')
# 2. Pido al usuario que ingrese su nombre de usuario de github
usuario = input('por favor, ingrese su nombre de usuario de github: ')
# 3. Fabrico la variable saludo
saludo = 'Hola ' + nombre + ', un gusto conocerte. Tu nombre de usuario en github es: ' + usuario
# 4. Imprimo el saludo en consola
print(saludo)
# 5. Crear el link a github
link = '<a class="nav-link" href="https://github.com/(github)">{nombre}</a>'
# 6. Imprimir el link en consola}
print(link)
'''

'''
Necesito preguntarle al usuario como se llama en
la vida real, y en Github

<li class="nav-item">
    <a class="nav-link" href="https://github.com/USUARIO">NOMBRE_USUARIO</a>
</li>
'''
''
nombre = input ('hola como te llamas: ')
github = input ('cual es tu nombre de usuario en github: ')
# enlace = '<li class="nav-item"><a class="nav-link" href=""https://github.com/' + github + '">' + nombre + '</a></li>'
enlace = 
<li class="nav-item">
    <a class="nav-link" href="https://github.com/{github}">{nombre}</a>
</li>
print(enlace)
