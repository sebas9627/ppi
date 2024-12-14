import pygame
from ayudas import *

class Mapa:
    def __init__(self):
        # Matriz del mundo (30 columnas x 20 filas)
        self.mundo = [
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', '2', ' ', ' ', ' ', ' ', ' ', '1', ' ', '1', ' ', ' ', ' ', ' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
            [' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', '1', ' ', ' ', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', '1', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
            ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1'],
            [' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '3', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ]

        # Cargar el sprite de la plataforma
        self.sprite_plataforma1 = pygame.image.load("./imagenes/plataformas/plataforma1.png").convert_alpha()
        self.sprite_plataforma1 = pygame.transform.scale(self.sprite_plataforma1, (TILESIZE, TILESIZE))
        
        self.sprite_plataformaAbajo = pygame.image.load("./imagenes/plataformas/plataformaAbajo.png").convert_alpha()
        self.sprite_plataformaAbajo = pygame.transform.scale(self.sprite_plataformaAbajo, (TILESIZE, TILESIZE))
        
        self.sprite_plataformaGrande = pygame.image.load("./imagenes/plataformas/plataformaGrande.png").convert_alpha()
        self.sprite_plataformaGrande = pygame.transform.scale(self.sprite_plataformaGrande, (TILESIZE, TILESIZE))
        
        self.sprite_arbol = pygame.image.load("./imagenes/objetos/arbol1.png").convert_alpha()
        self.sprite_arbol = pygame.transform.scale(self.sprite_arbol, (TILESIZE, TILESIZE))
        

        self.plataformas = pygame.sprite.Group()
        self.arboles = pygame.sprite.Group()  # Crear un grupo separado para los árboles

        self.crear_mundo()

    def crear_mundo(self):
        """Genera las plataformas a partir de la matriz del mundo."""
        for fila_idx, fila in enumerate(self.mundo):
            for col_idx, celda in enumerate(fila):
                if celda == '1':  # Representación de una plataforma
                    plataforma = pygame.sprite.Sprite()
                    plataforma.image = self.sprite_plataforma1  # Usar el sprite cargado
                    plataforma.rect = plataforma.image.get_rect()
                    plataforma.rect.topleft = (col_idx * TILESIZE, fila_idx * TILESIZE)
                    self.plataformas.add(plataforma)
                    print(f"Plataforma añadida en posición: {plataforma.rect.topleft}")
                    
                    
                elif celda == '2':  # Representación de la plataforma 2
                    plataforma = pygame.sprite.Sprite()
                    plataforma.image = pygame.transform.scale(
                        self.sprite_plataformaGrande, 
                        (TILESIZE * 2, TILESIZE * 2)  # Tamaño doble del TILESIZE
                    )
                    plataforma.rect = plataforma.image.get_rect()
                    plataforma.rect.topleft = (col_idx * TILESIZE, fila_idx * TILESIZE)
                    self.plataformas.add(plataforma)
                    
                elif celda == '3':  # Representación de la plataforma 3
                    plataforma = pygame.sprite.Sprite()
                    plataforma.image = pygame.transform.scale(
                        self.sprite_plataformaAbajo, 
                        (TILESIZE * 2, TILESIZE * 2)  # Tamaño doble del TILESIZE
                    )
                    plataforma.rect = plataforma.image.get_rect()
                    plataforma.rect.topleft = (col_idx * TILESIZE, fila_idx * TILESIZE)
                    self.plataformas.add(plataforma)
                    
                elif celda == '4':  # Representación de la plataforma 3
                    plataforma = pygame.sprite.Sprite()
                    plataforma.image = pygame.transform.scale(
                        self.sprite_arbol, 
                        (TILESIZE * 2, TILESIZE * 2)  # Tamaño doble del TILESIZE
                    )
                    plataforma.rect = plataforma.image.get_rect()
                    plataforma.rect.topleft = (col_idx * TILESIZE, fila_idx * TILESIZE)
                    self.plataformas.add(plataforma)
                

    def dibujar(self, ventana):
        """Dibuja las plataformas ajustadas a la cámara."""
        for plataforma in self.plataformas:
            offset_pos = plataforma.rect.topleft - offset
            ventana.blit(plataforma.image, offset_pos)

        for arbol in self.arboles:
            offset_pos = arbol.rect.topleft - offset
            ventana.blit(arbol.image, offset_pos)    
    
    def plantar_arbol(self, posicion):
        """Planta un árbol en la posición especificada."""
        arbol = pygame.sprite.Sprite()
        arbol.image = self.sprite_arbol
        arbol.rect = arbol.image.get_rect(topleft=posicion)
        self.arboles.add(arbol)  # Agregar el árbol al grupo de árboles
            
            
    

class PlataformaExterna(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill((0, 255, 0))  # Color verde para distinguirla
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
