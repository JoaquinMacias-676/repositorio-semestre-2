# Estructura del Proyecto

El proyecto se divide en tres archivos de Python para mantener un código limpio y modular:

| Archivo            | Función Principal                               | Teclas Control  |
|--------------------|-------------------------------------------------|-----------------|
| rectangulo_pequeño  | Define la clase del rectángulo pequeño          | Flechas         |
| rectangulo_grande   | Define la clase del rectángulo grande           | W, A, S, D      |
| Main.py             | Bucle principal del juego y lógica de colisión  | N/A             |

## 1. Clases de Objeto (rectangulo_pequeno y rectangulo_grande)
Concepto Clavo -> pygame.rect

El objeto self.rect es la parte más importante. Pygame usa este objeto para:

1. Dibujar el rectángulo en la pantalla
2. Mover el rectángulo (cambiando sus coordenadas x e y)
3. Detectar colisiones de forma eficiente

# Funciones Principales en las Clases

| Método               | Descripción                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------|
|__init__              | Inicializa objeto y crea el Pygame.Rect                                                     |
|dibujar (ventana)     |Dibuja el objeto en la ventana del juego usando Pygame.draw.rect()                           |
|mover (teclas)        |Lee las teclas presionadas y actualiza self.rect.x y self.rect.y                             |
|obtener_posicion      |Devuelve la posición actual del Rect (una tupla (x, y). Crucial para la lógica de colisión)  |
|restablecer_posicion  |Vuelve a colocar el Rect en una posición especifica                                          |

## 2- Detalles del método mover
El método mover ( self, teclas) se encarga de traducir la acción del jugador (presionar teclas) en movimiento en la pantalla. Se ejecuta continuamente en el bucle principal (main.py)

¿Cómo funcionan las teclas?
El argumento teclas es una lista que contiene el estado de todas las teclas del teclado en ese momento si teclas[pygame.K_LEFT] es TRUE, significa que la flecha izquierda está presionada.

## Dirección
Se asigna un valor de 1 o -1 a mov_x o mov_y según la tecla presionada. Este valor representa el peso que el objeto debe dar.

## Aplicación Final de movimiento

self.rect.x += mov_x * self.velocidad (mismo para y)

## Cálculo: 
El desplazamiento final es el resultado final de multiplicar la dirección (mov_x o mov_y) por la velocidad del objeto.
Ejemplo: Si mov_x es -1 y self.velocidad es 5, el rectángulo se mueve -5, pixeles a la izquierda.

## Actualización:
El operador de asignación aumenta += suma ese desplazamiento calculado a la posición actual del objeto. (self.rect.x y self.rect.y), moviendolo efectivamente en la pantalla.