def fuerza(qfloat,q2:float,r:float) -> float: # Se define una función que recibe como entrada las cargas y la distancia y devuelve la fuerza
  k = (8.99)*(10**9)	# Se define el valor de la constante de Coulomb
  return (k*q1*q1)/(r**2) # El valor de retorno será la aplicación de la formula

q1 = 3*(10**(-6))	# Valor de la primera carga
q2 = -8*(10**(-6))	# Valor de la segunda carga
r = 2.0			# Distancia entre las dos cargas

print("El valor de la fuerza de atracción entre las dos cargas es: {}".format(fuerza(q1,q2,r)))
