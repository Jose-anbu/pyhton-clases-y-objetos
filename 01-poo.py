""" POO: es un modo o paradigma de programación, que permite organizar el código pensando 
    el problema como una relación entre 'cosas', denominadas OBJETOS. """

""" Los OBJETOS trabajan utilizando las clases. """

""" CLASES: cosas de los más cotidianas como una computadora o un coche. Permiten agrupar un 
    conjunto de variables y funciones """

""" ATRIBUTOS """
# Son las diferentes características, que en el caso de una computadora podrían ser la marca
# o modelo

""" METODOS """
# Las clases tienen un conjunto de funcionalidades, en el caso de una computadora podría ser
# imprimir o reproducir. Llamaremos a estas funcionalidades métodos.

""" OBJETOS """
# Pueden existir diferentes tipos de computadoras. Llamaremos a estos diferentes tipos 
# OBJETOS. Es decir, el concepto abstracto de computadora es la clase, pero cualquier tipo de
# computadora particular será el objeto.

""" CLASES """
# CREAR UNA CLASE -> class nombre_de_clase:
# Por ejemplo perro. La mínima clase que podemos crear es una clase vacía y sin mucha 
# utilidad práctica.

# class Perro:
#     pass # No tiene utilidad pero daría un error si luego de ':' no tiene contenido

# INSTANCIAR UNA CLASE -> nombre_de_la_variable = nombre_de_clase()
# Una vez creada la clase se pueden crear uno o más objetos de la misma, como si de una 
# variable normal se tratase.

# perro1=Perro()
# perro2=Perro()
# () dentro de estos irían los parámetros de entrada si los hubiera.

""" ATRIBUTOS """
# ATRIBUTOS DE INSTANCIA
# Pertenecen a la instancia de la clase o al objeto. Son atributos particulares de cada 
# instancia, en nuestro caso de cada perro.

# ASIGNANDO ATRIBUTOS DE INSTANCIA
# Empezamos creando el nombre y la raza del perro. Esto se suele hacer por medio de un 
# método __init__ que será llamado automáticamente cuando se cree un objeto. No se le puede 
# cambiar el nombre y tiene su definición propia.

# class Perro:

#     # Constructor de la clase
#     def __init__(self,nombre,raza):

#         # Atributos de la instancia
#         self.nombre = nombre
#         self.raza = raza

# SELF
# Es una variable que representa la instancia de la clase, y deberá estar siempre ahí.
# El uso de __init__ y el doble __ no es una coincidencia. Cuando el método tiene esta forma, 
# significa que está reservado para su uso especial del lenguaje. En este caso sería lo que 
# se conoce como CONSTRUCTOR.

# ATRIBUTOS DE CLASE
# Se trata de atributos que pertenecen a la clase, por lo tanto serán comunes para todos los
# objetos.

# ASIGNANDO ATRIBUTOS DE CLASE
# Son atributos que serán comunes para todos los perros. Por ejemplo, la especie de los 
# perros es algo común para todos los objetos Perro.

# class Perro:
#     # Atributos de clase
#     especie = 'Mamífero'

#     # Constructor de la clase
#     def __init__(self,nombre,raza):

#         # Atributos de la instancia
#         self.nombre = nombre
#         self.raza = raza

# Dado que es un atributo de clase, no es necesario crear un objeto para acceder al atributo.
# print(Perro.especie)

# Se puede acceder también al atributo de clase desde el objeto.
# mi_perro = Perro('Pussi','Caniche')
# print(mi_perro.especie)
# De esta manera, todos los objetos que se creen de la clase perro compartirán ese atributo
# de clase.

# print(f'Su nombre es: {mi_perro.nombre}')
# print(f'Su raza es: {mi_perro.raza}')
# print(f'Es un: {mi_perro.especie}')


""" METODOS """
# __init__ es un método especial.

# DEFINIENDO METODOS -> por ejemplo: ladrar y caminar
# Ladrar no recibirá ningún parámetro pero caminar recibirá el número de pasos que queremos 
# andar.
# Se puede definir un método con def y el nombre, y entre los () colocar los parámetros de 
# entrada que recibe, donde siempre tendrá que estar self primero.
class Perro:
    # Atributos de clase
    especie = 'Mamífero'

    # Constructor de la clase
    def __init__(self,nombre,raza):

        # Atributos de la instancia
        self.nombre = nombre
        self.raza = raza
    
    # Definición de otros métodos
    def ladra(self):
        # print('Guau')
        print('Este perro ha ladrado :( \nEstá enojado')

    def camina(self,pasos):
        print(f'Este perro ha caminado {pasos} pasos')

# Si creamos un objeto mi_perro, se podrá hacer uso de sus métodos llamándolos con '.' y el
# nombre del método. Como si de una función se tratase, pueden recibir y devolver argumentos.
mi_perro = Perro('Pussi','Caniche')
print(f'Su nombre es: {mi_perro.nombre}')
print(f'Su raza es: {mi_perro.raza}')
print(f'Es un: {mi_perro.especie}')
mi_perro.ladra()
mi_perro.camina(10)

