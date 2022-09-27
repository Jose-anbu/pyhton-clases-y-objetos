class Perro():
    
    num_patas=4

    def __init__(self,nombre,raza,edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad

    def ladrar(self,cant):
        return 'guau '*cant

perro1=Perro('Cachito','Caniche',3)
perro2=Perro('Pepito','Dalmata',1)

print(perro1.ladrar(8))
print(perro2.ladrar(2))

