import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave."""

    def __init__(self, config, screen, ship):
        """Cria um objeto para o projétil na posição atual da espaçonave."""

        super(Bullet, self).__init__()
        self.screen = screen

        #   Cria um retângulo para o projétil em (0,0) e, em seguida, define a
        #   posição correta.
        self.bullet_rect = pygame.Rect(0, 0, config.bullet_width, 
            config.bullet_height)
        self.bullet_rect.centerx = ship.ship_rect.centerx
        self.bullet_rect.top = ship.ship_rect.top

        #   Armazena a posição do projétil como um valor decimal
        self.y = float(self.bullet_rect.y)

        self.bullet_color = config.bullet_color
        self.bullet_speed_factor = config.bullet_speed_factor

    def update(self):
        """Move o projétil para cima na tela."""

        #   Atualiza a posição decimal do projétil
        self.y -= self.bullet_speed_factor
        #   Atualiza a posição de rect
        self.bullet_rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil na tela."""

        pygame.draw.rect(self.screen, self.bullet_color, self.bullet_rect)