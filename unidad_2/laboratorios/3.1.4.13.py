'''
nombre: Samuel reynaldo olvera lira
fecha: 5 de noviembre 2023
descripcion 
laborartorio: 3.4.1.13
'''
class WeekDayError(Exception):
    """
    Excepción personalizada para manejar errores en el día de la semana.
    """
    pass


class Weeker:
    def __init__(self, day):
        """
        Constructor de la clase Weeker.

        Parámetros:
        - day: Nombre del día de la semana (Lun, Mar, Mie, Jue, Vie, Sab, Dom).
        """
        # Verifica si el día proporcionado es válido
        if day not in {'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom'}:
            raise WeekDayError("Día de la semana no válido")
        
        # Inicializa la propiedad privada para almacenar el día de la semana.
        self.__day = day

    def __str__(self):
        """
        Método que convierte el objeto Weeker en una cadena.
        """
        return self.__day

    def add_days(self, n):
        """
        Método que actualiza el día de la semana hacia adelante por n días.

        Parámetros:
        - n: Número de días a sumar.
        """
        days_of_week = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']
        current_index = days_of_week.index(self.__day)
        new_index = (current_index + n) % 7
        self.__day = days_of_week[new_index]

    def subtract_days(self, n):
        """
        Método que actualiza el día de la semana hacia atrás por n días.

        Parámetros:
        - n: Número de días a restar.
        """
        days_of_week = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']
        current_index = days_of_week.index(self.__day)
        new_index = (current_index - n) % 7
        self.__day = days_of_week[new_index]


try:
    # Ejemplo de uso
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lun')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
