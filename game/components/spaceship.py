from pickle import NONE
import pygame
from game.utils.constants import SPACESHIP


class Spaceship:

    POSITION_X = 500   
    POSITION_Y = 500

    def __init__(self,screen):
        #self.imagen = SPACESHIP
        #cambia el tamaño de la imagen para que se vea mejor Nota toma ancho y alto
        #fuucion que hace que pueda cambiar el tamaño de la imagen
        self.imagen = pygame.transform.scale(SPACESHIP, (80, 90)) 
        self.screen = screen
        self.position_x = self.POSITION_X
        self.position_y = self.POSITION_Y

    def muestra_texto(self, pantalla,texto,color=(255,255,255)):
        tipo_letra = pygame.font.Font('freesansbold.ttf',24)
        superficie = tipo_letra.render(texto,True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (self.position_x, self.position_y)
        pantalla.blit(superficie,rectangulo)

    def update(self):
        print(f"Avatar position: ({self.position_x}, {self.position_y})")



    def draw(self):
        #metodo blit para dibujar el spaceship en pantalla
        self.screen.blit(self.imagen, (self.position_x, self.position_y))
#        self.screen.blit(self.render_text, self.position_x,self.position_y)





    def moving_left(self):
        self.position_x -= 5

    def moving_right(self):
        self.position_x += 5

    def stop_moving(self):
        self.position_x = 0



