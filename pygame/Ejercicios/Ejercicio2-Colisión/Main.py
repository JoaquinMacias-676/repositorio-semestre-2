import pygame as pg

# Importando rectangulos
from rectangulo_grande import RectanguloGrande
from rectangulo_pequeño import RectanguloPequeño

pg.init()

background = (0, 10, 0)

ventana = pg.display.set_mode((800, 600))
pg.display.set_caption("Movimiento de rectángulos")

running = True # La ventana estará abierta todo el rato
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: # Al apretar la x de la ventana
            running = False
    ventana.fill(background) # fill añade el fondo

    RectanguloGrande.dibujar(ventana)

    pg.display.update() # Para actualizar la ventana, y asi que aparezca el circulo

pg.quit