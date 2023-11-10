'''
nombre: Samuel reynaldo olvera lira
fecha: 5 de noviembre 2023
descripcion 
laborartorio: 3.2.1.16
'''
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        # Inicializa la cola como una lista vacía.
        self.__queue = []

    def put(self, elem):
        # Agrega un elemento al final de la cola.
        self.__queue.append(elem)

    def get(self):
        # Obtiene y elimina el elemento del principio de la cola.
        if not self.__queue:
            # Lanza una excepción si la cola está vacía.
            raise QueueError("Error de Cola")
        return self.__queue.pop(0)

    def isempty(self):
        # Devuelve True si la cola está vacía, False de lo contrario.
        return not bool(self.__queue)


class SuperQueue(Queue):
    # No se añade ningún comportamiento adicional en esta subclase.
    pass

# Crear una instancia de SuperQueue
que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
