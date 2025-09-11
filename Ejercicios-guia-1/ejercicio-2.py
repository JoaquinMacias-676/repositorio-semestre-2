import numpy as np
import matplotlib.pyplot as plt
import math

class FuncionTrigonometrica():
    def __init__(self, tipo, amplitud= -1, periodo=2*math.pi):
        self.tipo_funcion = tipo
        self.amplitud = amplitud
        self.periodo = periodo