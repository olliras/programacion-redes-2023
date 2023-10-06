'''
nombre: Samuel reynaldo olvera lira
fecha: 26 de septiembre 2023
descripcion: laborartorios modulo 2
'''
# Ingresar la hora de inicio en horas y minutos
hora_inicio = int(input("Hora de inicio (horas): "))
minutos_inicio = int(input("Minuto de inicio (minutos): "))

# Ingresar la duración del evento en minutos
duracion_evento = int(input("Duración del evento (minutos): "))

# Calcular la hora final y los minutos finales
hora_final = (hora_inicio + (minutos_inicio + duracion_evento) // 60) % 24
minutos_finales = (minutos_inicio + duracion_evento) % 60

# Imprimir el resultado
print(f"El evento terminará a las {hora_final:02}:{minutos_finales:02}")
