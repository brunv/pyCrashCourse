"""Uma classe que pode ser usada para representar um carro elétrico simples"""

import battery, car

class ElectricCar(car.Car):
    """Representa aspectos de um carro específicos de veículos elétricos."""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico.
        """
        super().__init__(make, model, year)
        self.battery = battery.Battery()

#       Atenção para a notação de ponto nas linhas 5 e 14.