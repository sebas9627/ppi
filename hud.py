import pygame
from ayudas import *

class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)  # Fuente por defecto

    def dibujar(self, ventana, semillas):
        texto = self.font.render(f"Semillas: {semillas}", True, BLANCO)
        ventana.blit(texto, (10, 10))  # Esquina superior izquierda
