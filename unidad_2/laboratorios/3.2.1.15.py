'''
nombre: Samuel reynaldo olvera lira
fecha: 5 de noviembre 2023
descripcion 
laborartorio: 3.2.1.15
'''
class QueueError(Exception):  # Elige la clase base para la nueva excepción.
    pass

class Queue:
    def __init__(self):
        self.__queue = []  # Inicializa la cola como una lista vacía

    def put(self, elem):
        # Agrega elementos al final de la lista (cola)
        self.__queue.append(elem)

    def get(self):
        # Toma el elemento del principio de la lista (cola) y lo devuelve
        if not self.__queue:  # Si la cola está vacía, genera una excepción QueueError
            raise QueueError("Error de Cola")
        return self.__queue.pop(0)

# Crear una instancia de la clase Queue
que = Queue()

# Realizar operaciones put y get en un bucle, manejar la excepción QueueError
try:
    que.put(1)
    que.put("perro")
    que.put(False)
    
    print(que.get())
    print(que.get())
    print(que.get())
    
    # Intentar obtener un elemento de una cola vacía para generar la excepción
    print(que.get())

except QueueError as e:
    print(f"Error de Cola: {e}")
