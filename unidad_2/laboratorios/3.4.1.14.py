'''
nombre: Samuel reynaldo olvera lira
fecha: 5 de noviembre 2023
descripcion 
laborartorio: 3.4.1.14
'''
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        """
        Constructor de la clase Point.

        Parámetros:
        - x: Coordenada x del punto (por defecto, 0.0).
        - y: Coordenada y del punto (por defecto, 0.0).
        """
        # Propiedades privadas para almacenar las coordenadas del punto.
        self.__x = x
        self.__y = y

    def getx(self):
        """
        Método que devuelve la coordenada x del punto.
        """
        return self.__x

    def gety(self):
        """
        Método que devuelve la coordenada y del punto.
        """
        return self.__y

    def distance_from_xy(self, x, y):
        """
        Método que calcula y devuelve la distancia entre el punto y las coordenadas dadas.

        Parámetros:
        - x: Coordenada x del otro punto.
        - y: Coordenada y del otro punto.
        """
        return math.sqrt((self.__x - x)**2 + (self.__y - y)**2)

    def distance_from_point(self, point):
        """
        Método que calcula y devuelve la distancia entre el punto y otro punto dado como objeto Point.

        Parámetros:
        - point: Objeto Point representando las coordenadas del otro punto.
        """
        return self.distance_from_xy(point.getx(), point.gety())


# Ejemplo de uso
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
