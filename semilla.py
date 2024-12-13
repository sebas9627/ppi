import pygame
import random
from ayudas import *

class Semilla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./imagenes/objetos/semilla.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (
            random.randint(0, ANCHO - TILESIZE),  # Dentro del ancho visible
            random.randint(0, ALTO - TILESIZE)   # Dentro del alto visible
)
        self.velocidad = 3

    def actualizar(self, plataformas, jugador):
        """Actualiza la posición y verifica colisiones."""
        self.rect.y += self.velocidad

        # Verificar colisión con plataformas
        for plataforma in plataformas:
            if plataforma.rect.colliderect(self.rect):
                self.velocidad = 0
                break

        # Verificar colisión con el jugador
        if self.rect.colliderect(jugador.sprite.rect):
            jugador.semillas_recogidas += 1
            self.kill()  # Eliminar semilla del grupo

    def dibujar(self, ventana):
        """Dibuja la semilla ajustada al desplazamiento de la cámara."""
        ventana.blit(self.image, self.rect.topleft - offset)
