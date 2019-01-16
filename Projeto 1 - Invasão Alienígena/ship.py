import pygame

class Ship():
    """Uma classe para armazenar as informações da espaçonave."""

    def __init__(self, screen):
        """Inicializa a espaçonave e define sua posição inicial."""

        self.screen = screen

        #   Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.ship_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #   Inicia cada nova espaçonave na parte inferior central da tela
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""

        self.screen.blit(self.image, self.ship_rect)


#       O método init() de Ship aceita dois parâmetros: a referência self e screen,
#       que é a tela em que desenharemos a espaçonave.
#
#       Para carregar a imamge, chamamos image.load(). Essa função devolve uma
#       superfície que representa a espaçonave; essa infomação é armazenada em
#       self.imagem.
#
#       Depois que a imagem é caregada, usamos get_rect() para acessar o atributo
#       'rect' da superfície. Um motiv para o Pygame ser tão eficiente é que ele
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
#       valor de 'self.ship_rect.centerx' (a coordenada x do centro da espaçonave)
#       concicidir com o atributo 'centerx' do retângulo da tela. Faça com que o
#       valor de 'self.ship_rect.bottom' (a coordenada y da parte inferior da
#       espaçonave) seja igual ao valor do atriuto bottom do retângulo da tela.
#
#       Definimos o método 'blitme()' que desenhará a imagem na tela na posição
#       especificada por 'self.ship_rect'.