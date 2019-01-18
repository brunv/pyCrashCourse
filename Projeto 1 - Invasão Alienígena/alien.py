import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""

    def __init__(self, config, screen):
        """Inicializa o alienígena e define sua posição inicial."""

        super(Alien, self).__init__()
        self.screen = screen
        self.config = config

        #   Carrega a imagem do alienígena e define seu atributo rect
        self.alien_image = pygame.image.load('images/alien.bmp')
        self.alien_rect = self.image.get_rect()

        #   Inicia cada novo alienígena próxima à parte superior esquerda da tela
        self.alien_rect.x = self.alien_rect.width
        self.alien_rect.y = self.alien_rect.height

        #   Armazena a posição exata do alienígena
        self.x = float(self.alien_rect.x)

    def blitme(self):
        """Desenha o alienígena em sua posição atual."""

        self.screen.blit(self.alien_image, self.alien_rect)