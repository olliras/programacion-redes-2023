'''
nombre: Samuel reynaldo olvera lira
fecha: 5 de noviembre 2023
descripcion 
laborartorio: 3.4.1.12
'''
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        """
        Constructor de la clase Timer.

        Parámetros:
        - hours: Valor inicial de las horas (por defecto, 0).
        - minutes: Valor inicial de los minutos (por defecto, 0).
        - seconds: Valor inicial de los segundos (por defecto, 0).
        """
        # Inicializa las propiedades privadas para horas, minutos y segundos.
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        """
        Método que convierte el objeto Timer en una cadena de tiempo formateada.

        Retorna:
        Una cadena en el formato "hh:mm:ss".
        """
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"

    def next_second(self):
        """
        Método que incrementa el tiempo almacenado en un segundo.
        """
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def prev_second(self):
        """
        Método que decrementa el tiempo almacenado en un segundo.
        """
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23

# Crear una instancia de Timer
timer = Timer(23, 59, 59)
print(timer)

timer.next_second()
print(timer)

timer.prev_second()
print(timer)
