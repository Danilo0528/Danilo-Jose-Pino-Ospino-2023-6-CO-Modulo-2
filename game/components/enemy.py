import math
import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    POSITION_ENEMY_X = 500
    POSITION_ENEMY_Y = 20

    def __init__(self, screen):
        super().__init__()
        # self.imagen = SPACESHIP
        # Cambia el tamaño de la imagen para que se vea mejor. Nota: toma ancho y alto.
        # Función que hace que pueda cambiar el tamaño de la imagen.
        self.image_1 = pygame.transform.scale(ENEMY_1, (80, 90))
        self.image_2 = pygame.transform.scale(ENEMY_2, (80, 90))
        self.screen = screen
        self.rect = self.image_1.get_rect()
        self.position_x = self.POSITION_ENEMY_X
        self.position_y = self.POSITION_ENEMY_Y
        self.angle = 0
        self.radius = random.uniform(80, 120)
        self.speed = random.uniform(0.03, 0.07)
        self.image_index = 1

    def muestra_texto(self, pantalla,texto,color=(255,255,255)):
        tipo_letra = pygame.font.Font('freesansbold.ttf',24)
        superficie = tipo_letra.render(texto,True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (self.position_x, self.position_y)
        pantalla.blit(superficie,rectangulo)

    def update(self):
        self.angle += self.speed  # Incrementa el ángulo del enemigo
        # Calcula una nueva posición.
        self.position_x = self.POSITION_ENEMY_X + self.radius * math.cos(self.angle)  # Calcula la posición en el eje x
        self.position_y = self.POSITION_ENEMY_Y + self.radius * math.sin(self.angle)  # Calcula la posición en el eje y
        # Comprueba si la posición del enemigo está fuera de la pantalla.
        if self.position_x < 0 or self.position_x + self.rect.width > SCREEN_WIDTH:
            # Invierte la dirección de movimiento multiplicando la velocidad por -1.
            self.speed *= -1
        #print(f"Enemy: ({self.position_x}, {self.position_y})")

    def draw(self):
        # Método blit para dibujar el spaceship en pantalla.
        #if self.image_index == 1:
        self.screen.blit(self.image_1, (self.position_x, self.position_y))
        self.screen.blit(self.image_2, (self.position_x, self.position_y))

        #self.image_index = (self.image_index + 1) % 2
