import pygame
from ayudas import *

class Jugador:
    def __init__(self):
        self.sprite = pygame.sprite.Sprite()
        self.sprite_size = (40, 40)  # Tamaño uniforme para todos los sprites
        self.movimientos = {
            "walk_izquierda": [],
            "walk_derecha": [],
            "idle_izquierda": [],
            "idle_derecha": [],
            "jump_izquierda": [],
            "jump_derecha": [],
        }

        # Cargar todas las animaciones
        self.cargar_todas_las_animaciones()

        # Usar el primer sprite de idle_izquierda como imagen inicial
        self.sprite.image = self.movimientos["idle_izquierda"][0]
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.topleft = (400, ALTO_MUNDO - TILESIZE * 3)

        self.velocidad = pygame.math.Vector2(0, 0)
        self.saltando = False
        self.en_tierra = False
        self.direccion = "izquierda"
        self.indice_animacion = 0
        self.semillas_recogidas = 0  # Contador de semillas recogidas

        # Agregar el jugador al grupo de la cámara
        CAMARA.add(self.sprite)

    def cargar_todas_las_animaciones(self):
        """Carga todas las animaciones desde los sprites."""
        # Caminar
        for i in range(1, 7):
            imagen = pygame.image.load(f"./imagenes/personajes/Walk{i}.png").convert_alpha()
            imagen_escalada = pygame.transform.scale(imagen, self.sprite_size)
            self.movimientos["walk_izquierda"].append(imagen_escalada)
            self.movimientos["walk_derecha"].append(
                pygame.transform.flip(imagen_escalada, True, False)
            )

        # Idle
        for i in range(1, 5):
            imagen = pygame.image.load(f"./imagenes/personajes/Idle{i}.png").convert_alpha()
            imagen_escalada = pygame.transform.scale(imagen, self.sprite_size)
            self.movimientos["idle_izquierda"].append(imagen_escalada)
            self.movimientos["idle_derecha"].append(
                pygame.transform.flip(imagen_escalada, True, False)
            )

        # Salto
        imagen = pygame.image.load("./imagenes/personajes/Jump.png").convert_alpha()
        imagen_escalada = pygame.transform.scale(imagen, self.sprite_size)
        self.movimientos["jump_izquierda"].append(imagen_escalada)
        self.movimientos["jump_derecha"].append(
            pygame.transform.flip(imagen_escalada, True, False)
        )

    def mover(self, teclas, plataformas):
        """Controla el movimiento y las colisiones del jugador."""
        self.velocidad.x = 0

        # Movimiento lateral
        if teclas[pygame.K_LEFT]:
            self.velocidad.x = -4
            self.direccion = "izquierda"
            self.cambiar_animacion("walk_izquierda")
        elif teclas[pygame.K_RIGHT]:
            self.velocidad.x = 4
            self.direccion = "derecha"
            self.cambiar_animacion("walk_derecha")
        else:
            if self.en_tierra:
                self.cambiar_animacion(f"idle_{self.direccion}")

        # Salto
        if teclas[pygame.K_1] and self.en_tierra:
            self.velocidad.y = -18
            self.cambiar_animacion("jump_izquierda")
        elif teclas[pygame.K_2] and self.en_tierra:
            self.velocidad.y = -18
            self.cambiar_animacion("jump_derecha")

        # Gravedad
        self.velocidad.y += 1
        if self.velocidad.y > 16:
            self.velocidad.y = 16

        # Colisiones
        self.en_tierra = False
        for plataforma in plataformas:
            if plataforma.rect.colliderect(self.sprite.rect.move(self.velocidad.x, 0)):
                print(f"Colisión lateral detectada con plataforma en posición: {plataforma.rect.topleft}")
                self.velocidad.x = 0
            if plataforma.rect.colliderect(self.sprite.rect.move(0, self.velocidad.y)):
                if self.velocidad.y > 0:
                    print(f"Colisión inferior detectada con plataforma en posición: {plataforma.rect}, Jugador rect: {self.sprite.rect}")
                    self.sprite.rect.bottom = plataforma.rect.top
                    self.velocidad.y = 0
                    self.en_tierra = True
                elif self.velocidad.y < 0:
                    print(f"Colisión superior detectada con plataforma en posición: {plataforma.rect.topleft}")
                    self.sprite.rect.top = plataforma.rect.bottom
                    self.velocidad.y = 0

        self.sprite.rect.move_ip(self.velocidad)

    def cambiar_animacion(self, movimiento):
        """Cambia la animación actual según el estado."""
        animaciones = self.movimientos[movimiento]
        self.indice_animacion = (self.indice_animacion + 1) % len(animaciones)
        self.sprite.image = animaciones[self.indice_animacion]

    def dibujar(self, ventana):
        """Dibuja al jugador ajustado a la cámara."""
        ventana.blit(self.sprite.image, self.sprite.rect.topleft - offset)

    
    def plantar_arbol(self, mapa):
        """Planta un árbol en la plataforma más cercana si hay semillas disponibles."""
        if self.semillas_recogidas > 0:
            colision_detectada = False
            for plataforma in mapa.plataformas:
                #Verificar esquinas de la plataforma
                if (plataforma.rect.colliderect(self.sprite.rect) or
                    (self.sprite.rect.bottom == plataforma.rect.top and
                     self.sprite.rect.right > plataforma.rect.left and
                     self.sprite.rect.left < plataforma.rect.right)):
                    print(f"Colisión detectada con plataforma en posición: {plataforma.rect.topleft}")
                    # Ajustar la posición del árbol para que se plante justo encima de la plataforma 
                    posicion_arbol = (plataforma.rect.midtop[0] - self.sprite.rect.width // 2, plataforma.rect.top - int(1.5 * self.sprite.rect.height))
                    mapa.plantar_arbol(posicion_arbol)
                    self.semillas_recogidas -= 1
                    colision_detectada = True
                    break
            if not colision_detectada:
                print("No se detectó colisión con ninguna plataforma.")
        else:
            print("No hay suficientes semillas para plantar un árbol.")

            