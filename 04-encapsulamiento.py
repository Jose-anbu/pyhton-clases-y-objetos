""" Hace referencia al ocultamiento de los estados internos de una clase al exterior. 
    Dicho de otra forma, encapsular consiste en hacer que los atributos o métodos internos a 
    una clase no se puedan acceder ni modificar desde afuera, sino que tan solo el propio 
    objeto pueda acceder a ellos. """

""" PYTHON POR DEFECTO NO OCULTA LOS ATRIBUTOS Y METODOS DE UNA CLASE AL EXTERIOR """

""" VISIBILIDAD DE LOS DATOS """
# Todo lo que deba estar privado debe ser precedido por __, por ende, será imposible de 
# acceder desde el exterior de la clase.

# La encapsulación es el ocultamiento de datos del estado interno para proteger la 
# integridad del objeto. Ejemplo: 
class Cliente: # clase
    def __init__(self):
        self.__nroDeCuenta=1234 # variable nroDeCuenta -> encasulada
    
    def getNroDeCuenta(self):
        return self.__nroDeCuenta

















