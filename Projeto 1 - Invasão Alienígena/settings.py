class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena."""

    def __init__(self):
        """Inicializa as configurações do jogo."""

        #   Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #   Configurações da espaçonave
        self.ship_limit = 3

        #   Configurações dos projéteis
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        #   Configurações dos alienígenas
        self.fleet_drop_speed = 10

        #   A tava com que a velocidade do jogo aumenta
        self.speedup_scale = 1.3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as condigurações que mudam no decorrer do jogo."""

        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #   fleet_direction = 1 (direita) -1 (esquerda)
        self.fleet_direction = 1

    def increase_speed(self):
        """Aumenta as configurações de velocidade."""

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale