import pygame
from ayudas import *

class Letrero:
    def __init__(self, posicion, mensaje):
        self.rect = pygame.Rect(posicion[0], posicion[1], 100, 50)  # Tamaño fijo
        self.mensaje = mensaje
        self.mostrado = False
        self.font = pygame.font.Font(None, 24)

    def dibujar(self, ventana, jugador):
        if self.rect.colliderect(jugador.sprite.rect):
            self.mostrado = True

        if self.mostrado:
            texto = self.font.render(self.mensaje, True, BLANCO)
            ventana.blit(texto, (self.rect.x, self.rect.y - 30))  # Encima del letrero
        pygame.draw.rect(ventana, ROJO, self.rect, 2)  # Dibujar el letrero
