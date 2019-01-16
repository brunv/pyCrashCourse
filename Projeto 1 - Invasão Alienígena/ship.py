import pygame

class Ship():
    """Uma classe para armazenar as informações da espaçonave."""

    def __init__(self, screen):
        """Inicializa a espaçonave e define sua posição inicial."""

        self.screen = screen

        #   Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images,ship.bmp')
        self.ship_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #   Inicia cada nova espaçonave na parte inferior central da tela
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""

        self.screen.blit(self.image, self.ship_rect)