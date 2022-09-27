""" Aquellos que comienzan y terminan con dos carateres subrayados. Por ejemplo: 
    -La creación del objeto (__init__) 
    -Generar una cadena que los represente (__str__). """

# Todos estos métodos tienen un primer parámetro que hace referencia al propio objeto, que
# por convenio se suele llamar self. Siendo el resto de los parámetros del método variables.

""" METODO CONSTRUCTOR -> __init__ """
# Empleado para crear cada una de las instancias de las clases.
# No tiene una cantidad fija de parámetros, ya que estos dependen de las propiedades que 
# tenga el objeto.
# Por ejemplo, se puede crear un objeto Vector:
# class Vector():
#     def __init__(self,data):
#         self.data=data

# v=Vector([1,2])
# print(v)

""" __str__ """
# Se utiliza para crear una representación del objeto con significado para las personas.
# En el ejemplo anterior, el resultado es una cadena que indica el tipo de objeto y una
# dirección. Lo que generalmente no tiene sentido para las personas.
# Este inconveniente se puede resolver con el mètodo __str__
# class Vector():
#     def __init__(self,data):
#         self.data=data

#     def __str__(self):
#         return f'Los valores son: {self.data}'

# v=Vector([1,2])
# print(v)

""" __len__ """
# Se utiliza para obtener el número de elementos que tenga el objeto.
# Si probamos con el objeto nos encontramos con un error.
# class Vector():
#     def __init__(self,data):
#         self.data=data

#     def __str__(self):
#         return f'Los valores son: {self.data}'
    
#     def __len__(self):
#         return len(self.data)

# v=Vector([1,2])
# print(len(v))

""" __getitem__ """
# Permite que se puedan LEER los elementos mediante el uso de corchetes. 
# Necesita un parámetro adicional, que es la posición del elemento a leer. La función debe
# retornar el valor leido.
# class Vector():
#     def __init__(self,data):
#         self.data=data

#     def __str__(self):
#         return f'Los valores son: {self.data}'

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self,pos):
#         return self.data[pos]

# v=Vector([1,2])
# print(v[0])

""" __setitem__ """
# Complemento del método getitem. 
# Es necesario pasar 2 parámetros adicionales, la posición y el valor a reemplazar.
# class Vector():
#     def __init__(self,data):
#         self.data=data

#     def __str__(self):
#         return f'Los valores son: {self.data}'
    
#     def __len__(self):
#         return len(self.data)
    
#     def __getitem__(self,pos):
#         return self.data[pos]
    
#     def __setitem__(self,pos,valor):
#         self.data[pos]=valor

# v=Vector([1,2])
# v[1]=20
# print(v) 

""" __iter__ """
# Hace que la clase sea iterable, lo que permite usarla por ejemplo en bucles tipo for, es 
# necesario implementar este método.
# En el sgte. ejemplo, se ve una implementación del método en el que devuelve una cadena con 
# el índice y el valor de cada elemento.
class Vector():
    def __init__(self,data):
        self.data=data

    def __str__(self):
        return f'Los valores son: {self.data}'
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self,pos):
        return self.data[pos]

    def __setitem__(self,pos,valor):
        self.data[pos]:valor

    def __iter__(self):
        for indice in range(0,len(self.data)):
            yield f'Valor[{indice}]: {self.data[indice]}'

v=Vector([2,4,1])
for vec in v:
    print(vec)

 