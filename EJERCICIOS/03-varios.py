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

# class Persona():

#     especie='Humano'
#     cant_cerebro=1

#     def __init__(self,nombre,apellido,edad,meta):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.edad=edad
#         self.meta=meta
    
#     def saluda(self):
#         return f'Hola me llamo {self.nombre} {self.apellido} y tengo {self.edad} años'
    
#     def camina(self,pasos):
#         if(pasos > self.meta):
#             return 'Felicidades! cumpliste tu meta'
#         else:
#             return 'No lograste tu meta, ponete las pilas'

#     def __str__(self):
#         return f'Soy {self.nombre}, un gusto!'


# persona1=Persona('Lionel','Messi',34,1000)
# persona2=Persona('Mauricio','Cuello',31,5000)

# print(persona1.camina(2000))
# print(persona2.camina(2000))
# print(persona1)

# class Vector():
#     def __init__(self,data):
#         self._data=data

#     def __str__(self):
#         return f'Los valores son: {self._data}'

#     def __len__(self):
#         return len(self._data)
    
#     def __getitem__(self,pos): # Para obtener el elemento de una determinada posición
#         return self._data[pos]

#     def __setitem__(self,pos,valor): # Para modificar el valor en una posición
#         self._data[pos]=valor

#     def __iter__(self): # Para recorrer un objeto
#         for posicion in range(0,len(self._data)):
#             yield f'Valor[{posicion}]: {self._data[posicion]}' # yield: generador

# v=Vector([1,2,3,4,5])
# print(v)
# print(len(v))
# print(v[0])
# v[1]=20
# print(v)
# for vec in v:
#     print(vec)

""" CLASES ANIDADAS """
class Perro():

    num_patas=4

    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad

    def ladrar(self,cant):
        return 'guau '*cant

    def __str__(self):
        return f'{self.raza} de {self.edad} años'
class Persona():

    especie='Humano'
    cant_cerebro=1

    def __init__(self,nombre,apellido,edad,meta,perro):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.meta=meta
        self.perro=perro
    
    def saluda(self):
        return f'Hola me llamo {self.nombre} {self.apellido} y tengo {self.edad} años'
    
    def camina(self,pasos):
        if(pasos > self.meta):
            return 'Felicidades! cumpliste tu meta'
        else:
            return 'No lograste tu meta, ponete las pilas'

    def __str__(self):
        return f'Soy {self.nombre}, y tengo un {self.perro}'

perro1=Perro('Cachito','Caniche',3)
perro2=Perro('Pepito','Dalmata',1)

persona1=Persona('Lionel','Messi',34,1000,perro1)
persona2=Persona('Mauricio','Cuello',31,5000,perro2)

# print(persona1.camina(2000))
# print(persona2.camina(2000))
print(persona1)