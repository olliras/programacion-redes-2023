'''
nombre: Samuel reynaldo olvera lira
fecha: 5 de noviembre 2023
descripcion 
laborartorio: 3.4.1.15
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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        """
        Constructor de la clase Triangle.

        Parámetros:
        - vertice1: Objeto Point representando el primer vértice.
        - vertice2: Objeto Point representando el segundo vértice.
        - vertice3: Objeto Point representando el tercer vértice.
        """
        # Almacena los vértices en una lista privada.
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        """
        Método que calcula y devuelve el perímetro del triángulo.

        El perímetro es la suma de las longitudes de los lados del triángulo.
        """
        side1 = self.__vertices[0].distance_from_point(self.__vertices[1])
        side2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        side3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        return side1 + side2 + side3


# Ejemplo de uso
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
