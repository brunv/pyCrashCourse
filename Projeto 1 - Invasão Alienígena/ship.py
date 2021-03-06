import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Uma classe para armazenar as informações da espaçonave."""

    def __init__(self, config, screen):
        """Inicializa a espaçonave e define sua posição inicial."""

        super(Ship, self).__init__()
        
        self.screen = screen
        self.config = config

        #   Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #   Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #   Armazena um valor decimal para o centro da espaçonave
        self.ship_center = float(self.rect.centerx)

        #   Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Centraliza a espaçonave na tela."""

        self.center = self.screen_rect.centerx

    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            #   Move a espaçonave para a direita
            self.ship_center += self.config.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            #   Move a espaçonave para a esquerda
            self.ship_center -= self.config.ship_speed_factor

        #   Atualiza o objeto ship_react de acordo com self.ship_center
        self.rect.centerx = self.ship_center

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""

        self.screen.blit(self.image, self.rect)


#       O método init() de Ship aceita três parâmetros: a referência self; screen,
#       que é a tela em que desenharemos a espaçonave; e config, para ter acesso
#       às configurações da espaçonave.
#
#       Para carregar a imamge, chamamos image.load(). Essa função devolve uma
#       superfície que representa a espaçonave; essa infomação é armazenada em
#       self.imagem.
#
#       Depois que a imagem é caregada, usamos get_rect() para acessar o atributo
#       'rect' da superfície. Um motivo para o Pygame ser tão eficiente é que ele
#       permite tratar elementos do jogo como retângulo (rects), mesmo que eles não
#       tenham exatamente o formato de um retângulo. Tratar um elemento como um
#       retângulo é eficaz, pois os retângulos são formas geometricas simples. Essa
#       abordagem geralmente funciona bem, a ponto de ninguém que esteja jogando
#       perceba que não estamos trabalhando com a forma exata de cada elemento do
#       jogo.
#
#       Quando um elemento do jogo for centralizado, trabalhe com os atributos
#       'center', 'centerx' e 'centery' de um retângulo. Quando trabalhar com uma
#       borda da tela, use os atributos 'top', 'bottom', 'left' ou 'right'. Quando
#       ajustar a posição horizontal ou vertical do retângulo, você pode
#       simplesmente usar os atributos x e y, que correspondem às coordenadas x e y
#       de seu canto superior esquerdo. No Pygame, a origem (0,0) está no canto
#       superior esquerdo da tela.
#
#       Para posicionar a espaço na parte inferior central da tela, iniciamente
#       armazene o retângulo da tela em 'self.screen_rect' e, em seguida, faça o
#       valor de 'self.rect.centerx' (a coordenada x do centro da espaçonave)
#       concicidir com o atributo 'centerx' do retângulo da tela. Faça com que o
#       valor de 'self.rect.bottom' (a coordenada y da parte inferior da
#       espaçonave) seja igual ao valor do atriuto bottom do retângulo da tela.
#
#       Em update() usamos dois blocos if separados em vez de utilizar um elif para
#       permitir que o valor de rect.centerx da espaçonave seja incrementado
#       e então decrementado se as duas teclas de direção forem mantidas
#       pressionadas. Isso resulta na espaçonave parada.
#
#       Definimos o método 'blitme()' que desenhará a imagem na tela na posição
#       especificada por 'self.rect'.