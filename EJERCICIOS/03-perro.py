# class Perro():
    
#     num_patas=4

#     def __init__(self,nombre,raza,edad):
#         self.nombre=nombre
#         self.raza=raza
#         self.edad=edad

#     def ladrar(self,cant):
#         return 'guau '*cant

# perro1=Perro('Cachito','Caniche',3)
# perro2=Perro('Pepito','Dalmata',1)

# print(perro1.ladrar(8))
# print(perro2.ladrar(2))
# print(Perro.num_patas)

class Persona():

    especie='Humano'
    cant_cerebro=1

    def __init__(self,nombre,apellido,edad,meta):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.meta=meta
    
    def saluda(self):
        return f'Hola me llamo {self.nombre} {self.apellido} y tengo {self.edad} años'
    
    def camina(self,pasos):
        if(pasos > self.meta):
            return 'Felicidades! cumpliste tu meta'
        else:
            return 'No lograste tu meta, ponete las pilas'

persona1=Persona('Lionel','Messi',34,1000)
persona2=Persona('Mauricio','Cuello',31,5000)

print(persona1.camina(2000))
print(persona2.camina(2000))