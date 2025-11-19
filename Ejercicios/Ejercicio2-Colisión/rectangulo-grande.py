import pygame as pg

class RectanguloGrande:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 1
        self.color = (63, 234, 76)
        self.rect = pg.Rect(self.x, self.y, self.ancho, self.alto)

    def dibujar(self, ventana):
        pg.draw.rect(ventana, self.color, self.rect)

    def mover(self, teclas):
        mov_x = 0
        mov_y = 0

        if teclas[pg.K_a]:
            mov_x = -1
        if teclas[pg.K_d]:
            mov_x = 1
        if teclas[pg.K_w]:
            mov_y = -1
        if teclas[pg.K_s]:
            mov_y = 1