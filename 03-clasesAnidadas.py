""" RELACION ENTRE CLASES """
# Ejemplo 1: los Perros suelen ser la mascota de una Persona
# class Perro():
#     especie='Mamífero'
#     def __init__(self,nombre,raza):
#         self.nombre=nombre
#         self.raza=raza

#     def __str__(self):
#         return f'Nombre: {self.nombre}, Raza: {self.raza}, Especie: {self.especie}'

#     # METODOS
#     def ladrar(self):
#         print('Este perro ha ladrado :( \nEstá enojado')
    
#     def caminar(self,pasos):
#         print(f'Este perro ha caminado {pasos} pasos')

# class Persona():
#     def __init__(self,nombre,apellido,perro):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.perro=perro
    
#     def __str__(self):
#         return f'Mi nombre es: {self.nombre} {self.apellido}\n{self.perro}'

# perro1=Perro('Sammy','Caniche')
# persona1=Persona('Nicolas','Perez',perro1)

# print(persona1)

# Ejemplo 2: Otra forma de realizar clases internas a otras clases. No es lo más típico y 
# usado, pero puede ser útil para cuando hay una relación muy estricta entre 2 clases.
class Sueldo:
    def __init__(self,sueldo):
        self.sueldo=sueldo
    
    def __str__(self):
        return f'\nSUELDO: {self.sueldo}'

    class Empleado:
        def __init__(self,nombre,puesto):
            self.nombre=nombre
            self.puesto=puesto
            self.sueldo=Sueldo(1200)

        def __str__(self):
            return f'NOMBRE: {self.nombre}\nPUESTO: {self.puesto}\n{self.sueldo}'

s1=Sueldo(200)
emp1=Sueldo.Empleado('Nico','Profesor')
print(f'RESTULTADO 1: {s1}')
print(f'RESTULTADO 2: {emp1}')

