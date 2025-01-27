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


#Añadir una clase Pedido que tiene como atributos:
#   - lista de productos
#   - lista de cantidades
#Añade las siguiente funcionalidad:
#   - total_pedido: muestra el precio final del pedido
#   - mostrar_productos: muestra los productos del pedido

class Pedido:
    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido (self):
        total=0
        for(p,c) in zip(self.__productos, self.__cantidades):
            total= total + p.calcular_total(c)
        return total

    def mostrar_pedido (self):
        for(p,c) in zip(self.__productos, self.__cantidades):
            print ("Producto: ", p.nombre , " cantidad: " +str(c) )

Peras = Producto(1, "Peras", 2)
Manzanas = Producto(5, "Manzanas", 4)
print (Peras)
print (Manzanas)
print (Peras.calcular_total(5))
print(Manzanas.calcular_total(5))

productos = [Peras, Manzanas]
cantidades = [15, 15]

pedido= Pedido(productos, cantidades)

print("Total pedido: " + str(pedido.total_pedido()))
pedido.mostrar_pedido()
