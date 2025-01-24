#Crear una Clase Producto con los siguientes atributos:
# - código
# - nombre
# - precio 
#Crea su constructor, getter y setter y una función llamada calcular_total, donde le pasaremos unas unidades y nos debe calcular el precio final.

class Producto: 

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property                   #nos devuelve el codigo
    def codigo(self):
        return self.__codigo
    
    @codigo.setter              #para cambiar el valor del codigo
    def codigo (self, valor):
        self.__codigo = valor

    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, valor):
        self.__nombre = valor

    @property
    def precio (self):
        return self.__precio
    
    @precio.setter
    def precio (self, valor):
        self.__precio = valor
    
    def __str__(self):
        return ("Codigo: " + str(self.__codigo) + ", nombre: " + self.__nombre + ", precio: "+str(self.__precio))
    
    def calcular_total(self, unidades):
      return self.precio * unidades

Peras = Producto(1, "Peras", 2)
print (Peras)
x=Peras.calcular_total(5)
print(x)