import pygame
from juego import Juego

# Inicializa el juego y corre el bucle principal
if __name__ == "__main__":
    pygame.init()
    juego = Juego()
    juego.ejecutar()
    pygame.quit()
