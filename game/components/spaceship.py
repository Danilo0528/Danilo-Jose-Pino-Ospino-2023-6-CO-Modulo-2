import pygame
from pygame.sprite import Sprite
from game.components.bullet import Bullet
from game.utils.constants import SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):
    POSITION_X = 500
    POSITION_Y = 500

    def __init__(self, screen):
        super().__init__()
        # self.imagen = SPACESHIP
        # Cambia el tamaño de la imagen para que se vea mejor. Nota: toma ancho y alto.
        self.image = pygame.transform.scale(SPACESHIP, (80, 90))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) -40
        self.rect.y = 450
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
        #self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2

    def draw(self, screen):
        # Dibuja la imagen de la nave espacial en la pantalla
        self.screen.blit(self.image, self.rect)
        # Dibuja todas las balas del grupo en la pantalla
    #    self.bullets.draw(self.screen)
    #    font = pygame.font.Font(None, 20)
    #    label = font.render(self.name, True,(255,255,255))
    #    screen.blit(label, (self.rect.x,self.rect.y - 20))

    def shot_bullet(self):
        # Crea una instancia de Bullet y la agrega al grupo de balas
        bullet = Bullet(self.screen, self.rect.x, self.rect.y, self.shot_speed)
        self.bullets.add(bullet)

    def check_collision(self, enemy):
        return self.rect.colliderect(enemy.rect)
    
    def moving_left(self):
        # Mueve la nave espacial hacia la izquierda
        if self.rect.x > 0:
            self.rect.x -= 5
        else:
            self.rect.x = 0

    def moving_right(self):
        # Mueve la nave espacial hacia la derecha
        if self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += 5
        else:
            self.rect.x = SCREEN_WIDTH - self.rect.width

    def stop_moving(self):
        # Detiene el movimiento de la nave espacial y la centra
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2