import pygame as pg

# Importando rectangulos
from rectangulo_grande import RectanguloGrande
from rectangulo_pequeño import RectanguloPequeño

pg.init()

background = (30, 30, 30)
color_colision = (234, 63, 63) #rojo

ventana = pg.display.set_mode((800, 600))
pg.display.set_caption("Movimiento de rectángulos y colisión")

# Creando Objetos
rectangulo_pequeno = RectanguloPequeño(200, 200, 100, 50)
rectangulo_grande = RectanguloGrande(400, 300, 150, 100)

running = True # La ventana estará abierta todo el rato
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: # Al apretar la x de la ventana
            running = False
    ventana.fill(background) # fill añade el fondo

    teclas = pg.key.get_pressed()

    # Almacena la posición inicial de los rectángulos

    posición_anterior_pequeno = rectangulo_pequeno.obtener_posicion()
    posición_anterior_grande = rectangulo_grande.obtener_posicion()

    # Mover Rectángulos
    rectangulo_pequeno.mover(teclas)
    rectangulo_grande.mover(teclas)

    if rectangulo_pequeno.rect.colliderect(rectangulo_grande.rect):
        # Si existe colosión, se reestablece la posición anterior
        rectangulo_pequeno.restablecer_posicion(*posición_anterior_pequeno)
        rectangulo_grande.restablecer_posicion(*posición_anterior_grande)
        rectangulo_pequeno.cambiar_color(color_colision)
        rectangulo_grande.cambiar_color(color_colision)
    else:
        #Restablecer color
        rectangulo_pequeno.cambiar_color((63, 232, 234))
        rectangulo_grande.cambiar_color((63, 234, 76))

    ventana.fill(background)    
    rectangulo_pequeno.dibujar(ventana)
    rectangulo_grande.dibujar(ventana)


    pg.display.update() # Para actualizar la ventana, y asi que aparezca el circulo

pg.quit