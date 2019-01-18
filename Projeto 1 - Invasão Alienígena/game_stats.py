class GameStats():
    """Armazena dados estatísticos de Invasão Alienígena."""

    def __init__(self, config):
        """Inicializa os dados estatísticos."""

        self.config = config
        self.reset_status()

        #   Inicia a Invasão Alienígena em um estado ativo
        self.game_active = True

    def reset_status(self):
        """Inicializa os dados estatísticos que pode mudar durante o jogo."""

        self.ships_left = self.config.ship_limit