import random
import pygame
from game.components.bullet import Bullet
from game.components.enemy import Enemy
from game.components.spaceship import Spaceship
from pygame.sprite import Sprite

# game.utils.constants -> es un modulo donde tengo "objetos" en memoria como el BG (background)...etc
#   tambien tenemos valores constantes como el title, etc
from game.utils.constants import BG, ENEMY_1, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP, TITLE, FPS

# Game es la definicion de la clase (plantilla o molde para sacar objetos)
# self es una referencia que indica que el metodo o el atributo es de cada "objeto" de la clase Game
class Game:
    def __init__(self, num_enemies = 20):
        pygame.init() # este es el enlace con la libreria pygame para poder mostrar la pantalla del juego
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        #primero llamo a la clase Spaceship y accedo a la bariable screen del hijo
        #metodo inicialzador de spaceship
        self.avatar = Spaceship(self.screen) 
        self.enemy = Enemy(self.screen)
        self.bullets = pygame.sprite.Group()
        #self.enemies = pygame.sprite.Group()
        self.pantalla = self.screen
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship_death_count = 0
        self.game_over = True
        self.enemies = []
        self.enemies_count = num_enemies

    # este es el "game loop"
    # # Game loop: events - update - draw
    def run(self):
        self.playing = True
        while self.playing:
            print(f"I am still in the game loop")
            self.handle_events()
            self.update()
            self.draw()
            
        else:
            print(f"game is over because self.playing is", self.playing)
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        # esta expression es la llamada a un metodo pygame.event.get() que devuelve un "iterable"
        for event in pygame.event.get(): # con el for sacamos cada evento del "iterable"
            if event.type == pygame.QUIT: # pygame.QUIT representa la X de la ventana
                self.playing = False
            if event.type == pygame.KEYDOWN: #Detecta si presiono la tecla
                if event.key == pygame.K_LEFT: #mueve ala  izquierda al presionar
                    self.avatar.moving_left()
                elif event.key == pygame.K_RIGHT: #mueve ala  derecha al presionar
                    self.avatar.moving_right()
                elif event.key == pygame.K_SPACE:
                    self.avatar.shot_bullet()
            elif event.type == pygame.KEYUP: #Detecta si solte la tecla
                #verifica que si solte la tecla
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    print("solte la tecla")
                    #self.avatar.stop_moving()

    # aca escribo ALGO de la logica "necesaria" -> repartimos responsabilidades entre clases
    # o sea aqui deberia llamar a los updates de mis otros objetos
    # si tienes un spaceship; el spaceship deberia tener un "update" method que llamamos desde aqui
    def update(self):
        #le paso la lista de naves enemigas a avatar
         self.avatar.update()
         self.enemy.update()
         self.bullets.update()
         #self.avatar.check_collisions(self.enemies)

        #  for enemy in self.enemies:
        #      enemy.update()

        #  if len(self.enemies) < self.enemies_count:
        #     enemy_name = f"Enemy{len(self.enemies) + 1}"
        #     new_enemy = Enemy(self.screen, enemy_name)
        #     self.enemies.append(new_enemy)


    # este metodo "dibuja o renderiza o refresca mis cambios en la pantalla del juego"
    # aca escribo ALGO de la logica "necesaria" -> repartimos responsabilidades entre clases
    # o sea aqui deberia llamar a los metodos "draw" de mis otros objetos
    # si tienes un spaceship; el spaceship deberia tener un "draw" method que llamamos desde aqui
    
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        for enemy in self.enemies:
            enemy.draw(self.screen)
        if not self.game_over:
            self.avatar.draw()
            self.enemy.draw()
            self.avatar.muestra_texto(self.pantalla, "xswin")
            self.enemy.muestra_texto(self.pantalla, "DV1")
            self.bullets.draw(self.screen)
        else:
            self.show_game_over_screen()
        pygame.display.update()
        pygame.display.flip()


    def draw_background(self):
        # le indicamos a pygame que transforme el objeto BG (que es una imagen en memoria, no es un archivo)
        # y le pedimos que ajuste el ancho y alto de esa imagen
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # obtenemos el alto de la imagen
        image_height = image.get_height()
        ## DIBUJAMOS dos veces para dar la impresion de que nos movemos en el spacio
        # blit DIBUJA la imagen en memoria en una posicion (x, y)
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        # blit DIBUJA la imagen en memoria en una posicion (x, y)
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        # Controlamos que en el eje Y (vertical) si me sali del screen height (alto de pantalla)
        if self.y_pos_bg >= SCREEN_HEIGHT:
            # dibujo la imagen
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            # reseteo la posicion en y
            self.y_pos_bg = 0
        # No hay una velocidad de juego como tal, el "game_speed" simplemente me indica
        # cuanto me voy a mover (cuantos pixeles hacia arriba o abajo) cen el eje Y
        self.y_pos_bg += self.game_speed

    def show_game_over_screen(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text1 = font.render("Game Over", True, (255, 255, 255))
        text2 = font.render("Press F5 to restart", True, (255, 255, 255))
        text3 = font.render("Press X to quit", True, (255, 255, 255))
        imagen = pygame.transform.scale(SPACESHIP,(350, 400))
        image_rect = imagen.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        text1_rect = text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        text2_rect = text2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        text3_rect = text3.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(imagen, image_rect)
        self.screen.blit(text1, text1_rect)
        self.screen.blit(text2, text2_rect)
        self.screen.blit(text3, text3_rect)
        pygame.display.update()