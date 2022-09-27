""" Crear una clase para trabajar con una Persona. Agregale 3 atributos de instancia, por lo 
    menos 2 de clase, el constructor y dos métodos (uno con parámetros y otro sin parámetro). 
    Luego instanciar a dos personas. """

class Persona:

    # ATRIBUTOS DE CLASE
    pais='Argentina'
    provincia='Tucumán'

    # CONSTRUCTOR DE LA CLASE
    def __init__(self,nombre,apellido,dni):

        # ATRIBUTOS DE INSTANCIA
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni

    # METODOS
    def despierta(self):
        print(f'Buen día {self.nombre} {self.apellido}')
    
    def corre(self,distancia):
        print(f'{self.nombre} te toca correr {distancia} km')

persona1=Persona('José Antonio','Burgos',33333333)
persona2=Persona('Juan Ignacio','Burgos',44444444)

print(f'Nombre: {persona1.nombre}')
print(f'Apellido: {persona1.apellido}')
print(f'País: {Persona.pais}')
print(f'Provincia: {Persona.provincia}')
persona1.despierta()
persona1.corre(1)


