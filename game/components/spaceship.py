import pygame
from game.utils.constants import SPACESHIP


class Spaceship:

    POSITION_X = 500   
    POSITION_Y = 500
    #WIDTH = 90
    #HEIGH = 90
    def __init__(self,screen):
        #self.imagen = SPACESHIP
        #cambia el tamaño de la imagen para que se vea mejor Nota toma ancho y alto
        #fuucion que hace que pueda cambiar el tamaño de la imagen
        self.imagen = pygame.transform.scale(SPACESHIP, (80, 90)) 
        self.screen = screen
        self.position_x = self.POSITION_X
        self.position_y = self.POSITION_Y
        #self.width = self.WIDTH
        #self.heigh = self.HEIGH

   

    def update(self):
        print(f"Avatar position: ({self.position_x}, {self.position_y})")



    def draw(self):
        #metodo blit para dibujar el spaceship en pantalla
        self.screen.blit(self.imagen, (self.position_x, self.position_y))

    def moving_left(self):
        self.position_x -= 5

    def moving_right(self):
        self.position_x += 5

    def stop_moving(self):
        self.position_x = 0



