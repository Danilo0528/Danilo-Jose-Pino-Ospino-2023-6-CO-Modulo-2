import pygame

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy_2:

    POSITION_ENEMY_X = 500
    POSITION_ENEMY_Y = 40

    def __init__(self,screen):
        #self.imagen = SPACESHIP
        #cambia el tamaño de la imagen para que se vea mejor Nota toma ancho y alto
        #fuucion que hace que pueda cambiar el tamaño de la imagen
        self.imagen = pygame.transform.scale(ENEMY_2, (80, 90)) 
        self.screen = screen
        self.position_x = self.POSITION_ENEMY_X
        self.position_y = self.POSITION_ENEMY_Y
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.direction = 1
        self.speed = 5
        self.velocidad_x = 5
        self.velocidad_y = 5

    def muestra_texto(self, pantalla,texto,color=(255,255,255)):
        tipo_letra = pygame.font.Font('freesansbold.ttf',24)
        superficie = tipo_letra.render(texto,True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (self.position_x, self.position_y)
        pantalla.blit(superficie,rectangulo)  

    def update(self):
        # Actualiza la posición en el eje X y el y
        self.position_x += self.velocidad_x
        self.position_y += self.velocidad_y

        # Limita la posición en el eje X a los límites de la pantalla
        if self.position_x < 0:
            self.position_x = 0
        elif self.position_x + self.imagen.get_width() > SCREEN_WIDTH:
            self.position_x = SCREEN_WIDTH - self.imagen.get_width()
        # Limita la posición en el eje Y a los límites de la pantalla
        if self.position_y < 0:
            self.position_y = 0
        elif self.position_y + self.imagen.get_height() > SCREEN_HEIGHT:
            self.position_y = SCREEN_HEIGHT - self.imagen.get_height()
        print(f"Enemy: ({self.position_x},  {self.position_y})")

    def draw(self):
        #metodo blit para dibujar el spaceship en pantalla
        self.screen.blit(self.imagen, (self.position_x, self.position_y))