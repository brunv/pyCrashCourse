import sys
import pygame
from time import sleep
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


def check_events(config, screen, stats, sb, play_button, ship, aliens, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # clique no botão de fechar janela
            sys.exit()                  # fecha o programa
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, config, screen, ship, bullets)          

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(config, screen, stats, sb, play_button, ship, aliens,
                bullets, mouse_x, mouse_y)


def check_play_button(config, screen, stats, sb, play_button, ship, aliens,     
    bullets, mouse_x, mouse_y):
    """Inicia um novo jogo quando o jogador clicar em Play."""

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #   Reinicia as configurações do jogo
        config.initialize_dynamic_settings()

        #   Oculta o cursos do mouse
        pygame.mouse.set_visible(False)

        #   Reinicia os dados estatísticos do jogo:
        stats.reset_stats()
        stats.game_active = True

        #   Reinicia as imagens do painel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        #   Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        #   Cria uma nova frota e centraliza a espaçonave
        create_fleet(config, screen, ship, aliens)
        ship.center_ship()


def fire_bullet(config, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    
    #   Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < config.bullet_allowed:
        new_bullet = Bullet(config, screen, ship)
        bullets.add(new_bullet)


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
    number_rows = get_number_rows(config, ship.rect.height, alien.rect.height)

    #   Cria a primeira linha de alienígenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(config, screen, aliens, alien_number, row_number)


def update_bullets(config, screen, stats, sb, ship, aliens, bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""

    #   Atualiza posição dos projéteis
    bullets.update()

    #   Livra-se dos projéteis que desaparecerem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))

    check_bullet_alien_collisions(config, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(config, screen, stats, sb, ship, aliens,
     bullets):
    """Responde a colisões entre projéteis e alienígenas."""

    #   Verifica se algum projétil atingiu os alienígenas
    #   Em caso afirmativo, livra-se do projétil e do alienígena
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #   Os dois argumentos True dizem ao Pygame se os projéteis e os alienígenas
    #   que colidiram devem ser apagados.

    if collisions:
        for aliens in collisions.values():
            stats.score += config.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        #   Destrói todos os projéteis existentes e cria uma nova frota
        bullets.empty()
        config.increase_speed()

        #   Aumenta o nível
        stats.level += 1
        sb.prep_level()

        create_fleet(config, screen, ship, aliens)


def update_screen(config, screen, stats, sb, ship, aliens, bullets, play_button):
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

    #   Desenha informação sobre a pontuação
    sb.show_score()

    #   Desenha o botão Play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()

    #   Deixa a tela mais recente visível
    pygame.display.flip()


def check_fleet_edges(config, aliens):
    """Responde apropriadamente se algum alienígena alcançou uma borda."""

    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(config, aliens)
            break


def change_fleet_direction(config, aliens):
    """Faz toda a frota descer e mudar de direção."""

    for alien in aliens.sprites():
        alien.rect.y += config.fleet_drop_speed
    config.fleet_direction *= -1


def check_aliens_bottom(config, stats, screen, ship, aliens, bullets):
    """Verifica se algum alienígena alcançou a parte inferior da tela."""

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #   Trata esse caso do mesmo modo que é feito quando a espaçonave
            #   é atingida.
            ship_hit(config, stats, screen, ship, aliens, bullets)
            break


def update_aliens(config, stats, screen, ship, aliens, bullets):
    """
    Verifica se a frota está em uma das bordas e então atualiza as posições de
    todos os alienígenas da frota.
    """

    check_fleet_edges(config, aliens)
    aliens.update()

    #   Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(config, stats, screen, ship, aliens, bullets)
        print("Ship hit!!!")

    #   Verifica se há algum alienígenaque atingiu a parte inferior da tela
    check_aliens_bottom(config, stats, screen, ship, aliens, bullets)


def ship_hit(config, stats, screen, ship, aliens, bullets):
    """Responde ao fato de a espaçonave ter sido atingida por um alienígena."""

    if stats.ships_left > 0:
        #   Decrementa ships_left
        stats.ships_left -= 1

        #   Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        #   Cria uma nova frota e centraliza a espaçonave
        create_fleet(config, screen, ship, aliens)
        ship.center_ship()

        #   Faz uma pausa
        sleep(1)
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    
def check_high_score(stats, sb):
    """Verifica se há uma nova pontuação máxima."""

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


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