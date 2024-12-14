import pygame

# Configuración general
FPS = 60
TILESIZE = 64
ANCHO_MUNDO = TILESIZE * 30
ALTO_MUNDO = TILESIZE * 20
ANCHO, ALTO = TILESIZE * 15, TILESIZE * 8
MEDIO_ANCHO, MEDIO_ALTO = ANCHO // 2, ALTO // 2

# FONTS:
 
FONT1 = 'Acme-Regular.ttf'
FONT2 = 'Action_Man_Bold_Italic.ttf'    
FONT3 = 'Action_Man_Bold.ttf'
FONT4 = 'Action_Man.ttf'
FONT5 = 'Airstream.ttf'
FONT6 = 'Planes_ValMore.ttf'


# Colores
NEGRO = (0,0,0)        
BLANCO = (255,255,255)    
AZULMARINO = (99,184,255)
TURQUESA = (0,245,255)
VERDEMENTA = (0,238,118)
VERDE = (0,139.69)
VIOLETA = (154,50,205)
AMARILLO = (255,255,0)
ROJO = (255,0,0)
CAFE = (51,0,30) 

# Crear la ventana principal
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Eco Guardian")

# Grupo para sprites visibles en la cámara
CAMARA = pygame.sprite.Group()
offset = pygame.math.Vector2(0, 0)

# Fondo desplazable
class FONDO:
    def __init__(self):
        fondo = pygame.image.load("./imagenes/fondos/arcade_platformer.png").convert_alpha()
        self.imagen = pygame.transform.scale(fondo, (ANCHO, ALTO))
        self.ancho = self.imagen.get_rect().size[0]
        self.posicion = 0

def desplazarFondo(fondo):
    ventana.blit(fondo.imagen, (fondo.posicion, 0))
    ventana.blit(fondo.imagen, (fondo.ancho + fondo.posicion, 0))
    fondo.posicion -= 3
    if abs(fondo.posicion) > fondo.ancho:
        fondo.posicion = 0

# Función de cámara
def camara(jugador):
    global offset
    offset.x = jugador.sprite.rect.centerx - MEDIO_ANCHO
    offset.y = jugador.sprite.rect.centery - MEDIO_ALTO

    for sprite in CAMARA:
        offset_pos = sprite.rect.topleft - offset
        ventana.blit(sprite.image, offset_pos)

# Mostrar texto en pantalla
def mostrar_texto(ventana, texto, x, y, tamano=70, color=BLANCO,fuente_personalizada="./fonts/Planes_ValMore.ttf"):
    x = x
    y = y
    try:
        fuente = pygame.font.Font(fuente_personalizada, tamano) if fuente_personalizada else pygame.font.Font(None, tamano)
    except FileNotFoundError:
        print(f"No se encontró la fuente personalizada: {fuente_personalizada}. Usando fuente predeterminada.")
        fuente = pygame.font.Font(None, tamano)

    render = fuente.render(texto, True, color)
    ventana.blit(render, (x, y))
    #fuente = pygame.font.Font(None, tamano)
    #render = fuente.render(texto, True, color)
    #ventana.blit(render, (x, y))

# Clase para texto intermitente
class TextoIntermitente:
    def __init__(self, texto, x, y, fuente_personalizada = "./fonts/Action_Man_Bold.ttf", tamano_fuente=30):
        self.texto = texto
        self.x = 250
        self.y = 460
        self.blink_on = True
        self.tiempo = pygame.time.get_ticks()
        self.activo = True
        #self.font = pygame.font.Font(None, 36)
        self.font = pygame.font.Font(fuente_personalizada, tamano_fuente)
        
        

    def dibujar(self, ventana):
        if not self.activo:
            return
        if pygame.time.get_ticks() - self.tiempo > 500:
            self.blink_on = not self.blink_on
            self.tiempo = pygame.time.get_ticks()
        if self.blink_on:
            texto_renderizado = self.font.render(self.texto, True, ROJO)
            ventana.blit(texto_renderizado, (self.x, self.y))
