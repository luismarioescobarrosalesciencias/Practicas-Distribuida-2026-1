import simpy
from Nodo import *
from Canales.CanalBroadcast import *
#from NodoGenerador import NodoGenerador


TICK = 1
class NodoConvergcast(Nodo):
    '''Implementa la interfaz de Nodo para el algoritmo de convergcast.'''
    def __init__(self, id_nodo,vecinos, canal_entrada, canal_salida, mensaje=None):
            self.id_nodo = id_nodo
            self.padre = None
            self.vecinos = vecinos
            self.canal_entrada = canal_entrada
            self.canal_salida = canal_salida
            self.mensaje = mensaje
            self.value =  self.id_nodo #Como ejemplo diremos que los valores recolectados seran los ids , no usamos un conjunto pues no sabemos que se vaya ahacer (la funcion f)
            self.valor_final = None

    def convergecast(self,env):
	    '''Implementar'''



                 
                 

                 




