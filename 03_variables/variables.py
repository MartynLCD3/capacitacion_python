# Trabajando con variables
numeroObtenido = 7
print(numeroObtenido) # 7
print(numeroObtenido // 3) # 2

# Reasignando valor
variableAreasignar = 23
print(variableAreasignar) # 23
variableAreasignar = 'Ahora es un string'
print(variableAreasignar) # Ahora es un string

# Tomar datos de entrada
valorEntrante = input()
print(valorEntrante) # lo que ingreses, se pinta
mensajeAimprimir = 'nombre: '
nombre = input(mensajeAimprimir) #  nombre: ...
print('Hola ' + nombre) # Hola ...

# @Input toma entero e imprime string
edad = int(input('Edad: ')) # ... @toma enteros nada más
print(edad) # ... 

edad = 26
print('La edad de Martín es ' + str(edad) + ' años') # La edad de Martín es 26 años

# Operadores in-place (forma de concatenación)
valorAconcatenar = "Hola"
valorAconcatenar += "Mundo"
print(valorAconcatenar) # HolaMundo

valorAconcatenar = "Holis"
valorAconcatenar *= 4
print(valorAconcatenar) # HolisHolisHolisHolis
