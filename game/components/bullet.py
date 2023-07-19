import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET
class Bullet(Sprite):
    def __init__(self, screen, x, y, speed):
        super().__init__()
        self.image = pygame.transform.scale(BULLET, (60, 50))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
