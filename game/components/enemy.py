import math
import random
import pygame

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy:

    POSITION_ENEMY_X = 500
    POSITION_ENEMY_Y = 20

    def __init__(self,screen):
        #self.imagen = SPACESHIP
        #cambia el tamaño de la imagen para que se vea mejor Nota toma ancho y alto
        #fuucion que hace que pueda cambiar el tamaño de la imagen
        self.imagen = pygame.transform.scale(ENEMY_1, (80, 90))
        self.screen = screen
        self.position_x = self.POSITION_ENEMY_X
        self.position_y = self.POSITION_ENEMY_Y
        self.angle = 0
        self.radius = random.uniform(80, 120)
        self.speed = random.uniform(0.03, 0.07)



    def muestra_texto(self, pantalla,texto,color=(255,255,255)):
        tipo_letra = pygame.font.Font('freesansbold.ttf',24)
        superficie = tipo_letra.render(texto,True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (self.position_x, self.position_y)
        pantalla.blit(superficie,rectangulo)

    def update(self):
        self.angle += self.speed
        # Calculate the new position using trigonometry
        self.position_x = self.POSITION_ENEMY_X + self.radius * math.cos(self.angle)
        self.position_y = self.POSITION_ENEMY_Y + self.radius * math.sin(self.angle)
        # Check boundaries and reverse direction
        if self.position_x < 0 or self.position_x + self.imagen.get_width() > SCREEN_WIDTH:
            self.speed *= -1
        print(f"Enemy: ({self.position_x}, {self.position_y})")

    def draw(self):
        #metodo blit para dibujar el spaceship en pantalla
        self.screen.blit(self.imagen, (self.position_x, self.position_y))