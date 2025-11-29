class Papa:
    def __init__(self, altura):
        self.altura = altura

class Mama:
    def __init__(self, ojos):
        self.ojos = ojos

class Yo(Papa, Mama):
    def __init__(self, altura, ojos, pelo):
        self.pelo = pelo

yo1 = Yo(170, "negro", "marron")


