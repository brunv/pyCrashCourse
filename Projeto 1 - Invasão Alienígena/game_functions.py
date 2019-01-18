import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, config, screen, ship, bullets):
    """Responde a pressionamentos de tecla."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(config, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Responde a solturas de tecla."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(config, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # clique no botão de fechar janela
            sys.exit()                  # fecha o programa
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, config, screen, ship, bullets)          

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(config, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    
    #   Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < config.bullet_allowed:
        new_bullet = Bullet(config, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""

    #   Atualiza posição dos projéteis
    bullets.update()

    #   Livra-se dos projéteis que desaparecerem
    for bullet in bullets.copy():
        if bullet.bullet_rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))


def get_number_aliens_x(config, alien_width):
    """Determina o número de alienígenas que cabem em uma linha."""

    available_space_x = config.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(config, ship_height, alien_height):
    """Determina o número de linhas com alienígenas que cabem na tela."""

    available_space_y = (config.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows


def create_alien(config, screen, aliens, alien_number, row_number):
    """Cria um alienígena e o posiciona na linha."""
    
    alien = Alien(config, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    aliens.add(alien)


def create_fleet(config, screen, ship, aliens):
    """Cria uma frota completa de alienígenas."""

    #   Cria um alienígena e calcula o número de alienígenas em uma linha
    alien = Alien(config, screen)
    number_aliens_x = get_number_aliens_x(config, alien.rect.width)
    number_rows = get_number_rows(config, ship.ship_rect.height, alien.rect.height)

    #   Cria a primeira linha de alienígenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(config, screen, aliens, alien_number, row_number)


def update_screen(config, screen, ship, aliens, bullets):
    """Atualiza as imagens na tela e altera para a nova tela."""

    #   Redesenha a tela a cada passagem do laço
    screen.fill(config.bg_color)
    
    #   Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Redesenha a espaçonave a cada passagem do laço
    ship.blitme()
    aliens.draw(screen)

    #   Redesenha o alienígena a cada passagem do laço
    #alien.blitme()

    #   Deixa a tela mais recente visível
    pygame.display.flip()



# 	    Para fazer nosso programa responder aos eventos, escreveremos um laço
#	    de eventos apara ouvir um evento e executar uma tarefa apropriada de
#	    acordo com o tipo de evento ocorrido utilizando event.get().
#
#       Fornecemos um parâmetro 'ship' à função check_events(). Nela, acrescentamos
#       um bloco 'elif' no laço para responder quando Pygame detectar um evento
#       KEYDOWN. Em seguida verificamos se a tecla pressionada é a seta para a
#       direita (K_RIGHT) lendo o atributo 'event.key'.
#
#       Quando o jogador manter a seta para dirieta pressionada, queremos que a
#       espaçonave continue a se mover para a direita até que o jogador soltar a
#       tecla. Assim, faremos nosso jogo detectar um evento pygame.KEYUP para que
#       possamos saber quando a seta para a direita foi solta; então usaremos os 
#       eventos KEYDOWN e KEYUP juntamente com uma flag, chamava 'moving_right'
#       para implementar o movimento contínuo.
#
#	    Desenhamos a espaçonave na tela chamando 'ship.blitme()' depois de
#	    preencher a cor de fundo; assim a espaçonave aparecerá sobre essa cor.