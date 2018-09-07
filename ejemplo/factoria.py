from ejemplo.femenino import Femenino
from ejemplo.masculino import Masculino

class Factoria(object):
    """
    Esta clase es nuestra factoria, como ya sabes Python define un constructor  sin argumentos por default para cada clase,
    por eso no hace falta escribir uno.
    """

    def get_persona(self, nombre, edad, genero):
        """
        Metodo que retorna objetos segun el genero
        :param nombre:
        :param genero: es el parametro usado por la factoria para elegir el objeto a crear
        :param edad:
        :return:
        """

        if genero is 'F':
            return Femenino(nombre, edad, genero)
        elif genero is 'M':
            return Masculino(nombre, edad, genero)