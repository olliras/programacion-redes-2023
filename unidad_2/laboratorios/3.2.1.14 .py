'''
nombre: Samuel reynaldo olvera lira
fecha: 5 de noviembre 2023
descripcion 
laborartorio: 3.2.1.14
'''
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        # Inicializa la clase base (Stack) y agrega una propiedad para contar las operaciones pop
        super().__init__()
        self.__counter = 0  # Inicializa el contador a cero en el constructor

    def get_counter(self):
        # Devuelve el valor actual del contador
        return self.__counter

    def pop(self):
        # Realiza un pop y actualiza el contador
        val = super().pop()  # Llama al método pop de la clase base
        self.__counter += 1  # Incrementa el contador
        return val

# Crea una instancia de CountingStack
stk = CountingStack()

# Realiza operaciones push y pop en un bucle
for i in range(100):
    stk.push(i)
    stk.pop()

# Imprime el valor actual del contador
print(stk.get_counter())
