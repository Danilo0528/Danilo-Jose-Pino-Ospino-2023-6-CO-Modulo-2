import pygame
from pygame.sprite import Sprite
from game.components.bullet import Bullet
from game.utils.constants import SPACESHIP

class Spaceship(Sprite):
    POSITION_X = 500
    POSITION_Y = 500

    def __init__(self, screen):
        super().__init__()
        # self.imagen = SPACESHIP
        # Cambia el tamaño de la imagen para que se vea mejor. Nota: toma ancho y alto.
        self.image = pygame.transform.scale(SPACESHIP, (80, 90))
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_Y
        self.screen = screen
        self.bullets = pygame.sprite.Group()
        self.shot_speed = 10
        self.count = 0

    def muestra_texto(self, pantalla, texto, color=(255, 255, 255)):
        tipo_letra = pygame.font.Font('freesansbold.ttf', 24)
        superficie = tipo_letra.render(texto, True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (self.rect.x, self.rect.y)
        pantalla.blit(superficie, rectangulo)

    def update(self):
        # Actualiza todos los sprites del grupo de balas
        self.bullets.update()


    def draw(self):
        # Dibuja la imagen de la nave espacial en la pantalla
        self.screen.blit(self.image, self.rect)
        # Dibuja todas las balas del grupo en la pantalla
        self.bullets.draw(self.screen)

    def shot_bullet(self):
        # Crea una instancia de Bullet y la agrega al grupo de balas
        bullet = Bullet(self.screen, self.rect.x, self.rect.y, self.shot_speed)
        self.bullets.add(bullet)


    def check_collision(self, enemy):
        return self.rect.colliderect(enemy.rect)
    

    def moving_left(self):
        # Mueve la nave espacial hacia la izquierda
        self.rect.x -= 5

    def moving_right(self):
        # Mueve la nave espacial hacia la derecha
        self.rect.x += 5

    def stop_moving(self):
        # Detiene el movimiento de la nave espacial estableciendo su posición x en 0
        self.rect.x = 0
