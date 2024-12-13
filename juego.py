import pygame
from jugador import *
from semilla import *
from mapa import *
from ayudas import *
class Juego:
    def __init__(self):
        pygame.init()
        self.ventana = ventana
        self.reloj = pygame.time.Clock()
        self.corriendo = True
        
        #Musica en el juego
        pygame.mixer.music.load("./musica/musica_juego.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    

        # Elementos del juego
        self.jugador = Jugador()
        self.mapa = Mapa()
        self.fondo = FONDO()
        self.texto_intermitente = TextoIntermitente("Presiona ESPACIO para comenzar", MEDIO_ANCHO, MEDIO_ALTO)

        # Semillas
        self.semillas = pygame.sprite.Group()
        self.tiempo_proxima_semilla = pygame.time.get_ticks() + 10000

        # Generar semillas iniciales
        for _ in range(10):
            semilla = Semilla()
            self.semillas.add(semilla)

        # Plataforma externa
        self.plataforma_externa = PlataformaExterna(300, 500, 100, 20)
        self.mapa.plataformas.add(self.plataforma_externa)

        # Título temporal
        self.titulo = True

    def manejar_eventos(self):
        """Gestiona los eventos del teclado y la ventana."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.corriendo = False
                if evento.key == pygame.K_SPACE:
                    self.texto_intermitente.activo = False
                    self.titulo = False
                if evento.key == pygame.K_3:  
                    self.jugador.plantar_arbol(self.mapa)

    def actualizar(self):
        """Actualiza los elementos del juego."""
        teclas = pygame.key.get_pressed()
        self.jugador.mover(teclas, self.mapa.plataformas)

        # Actualizar semillas
        for semilla in self.semillas:
            semilla.actualizar(self.mapa.plataformas, self.jugador)

        # Generar nuevas semillas cada 10 segundos
        if pygame.time.get_ticks() > self.tiempo_proxima_semilla:
            nueva_semilla = Semilla()
            self.semillas.add(nueva_semilla)
            self.tiempo_proxima_semilla = pygame.time.get_ticks() + 5000

    def dibujar(self):
        """Dibuja todos los elementos en pantalla en el orden correcto."""
        desplazarFondo(self.fondo)  # Fondo desplazable
        camara(self.jugador)  # Ajuste de cámara
        self.mapa.dibujar(self.ventana)  # Dibujar el mapa

        # Dibujar semillas encima del mapa
        for semilla in self.semillas:
            semilla.dibujar(self.ventana)

        # Dibujar jugador encima de las semillas
        self.jugador.dibujar(self.ventana)

        # Mostrar texto intermitente
        if self.texto_intermitente.activo:
            self.texto_intermitente.dibujar(self.ventana)

        # Mostrar título temporal
        if self.titulo:
            mostrar_texto(self.ventana, "ECO-GUARDIAN", MEDIO_ANCHO-200, MEDIO_ALTO - 200, 48, VERDEMENTA)

        # Dibujar HUD (contador de semillas)
        mostrar_texto(
            self.ventana,
            f"Semillas: {self.jugador.semillas_recogidas}",
            10,
            10,
            24,
            BLANCO,
        )

        pygame.display.flip()

    def ejecutar(self):
        """Bucle principal del juego."""
        while self.corriendo:
            self.manejar_eventos()
            if not self.texto_intermitente.activo:
                self.actualizar()
            self.dibujar()
            self.reloj.tick(FPS)
