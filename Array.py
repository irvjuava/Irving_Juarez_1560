class Array:

    def __init__(self, size):
        self.__size = size
        self.__data = []
        for index in range(size):
            self.__data.append(None)

    def length(self):
        return self.__size

    def getItem(self, index):
        if index >= 0 and index < self.__size:
            return self.__data[index]
        else:
            return None # Index no válido

    def setItem(self, index, valor):
        if index >= 0 and index < self.__size:
            self.__data[index] = valor
        else:
            print("Index fuera de rango")

    def clearing(self, valor):
        for i in range(self.__size):
            self.__data[i] = valor

    def to_string(self):
        print(self.__data)

def main():
    adt = Array(10)
    adt.to_string()
    print(f"El tamaño del arreglo es {adt.length()}")
    adt.setItem(4,34)
    adt.to_string()
    print(f"El elemento 4 es {adt.getItem(4)}")
    adt.clearing(0)
    adt.to_string()

main()
