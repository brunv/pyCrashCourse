class GameStats():
    """Armazena dados estatísticos de Invasão Alienígena."""

    def __init__(self, config):
        """Inicializa os dados estatísticos."""

        self.config = config
        self.reset_stats()

        #   Inicia a Invasão Alienígena em um estado ativo
        self.game_active = False

        #   A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0

    def reset_stats(self):
        """Inicializa os dados estatísticos que pode mudar durante o jogo."""

        self.ships_left = self.config.ship_limit
        self.score = 0