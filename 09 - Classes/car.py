"""Uma classe que pode ser usada para representar um carro."""

class Car():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Define o valor de leitura do hodômetro com o valor especificado.
        Rejeita a alteração se for tentativa de diminuir o valor do hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        """
        Soma a quantidade especificada ao valor de leitura do hodôemtro.
        Rejeita a soma se a quantidade especificada for negativa.
        """
        if mileage > 0:
            self.odometer_reading += mileage
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        """Exibe uma frase mostrando que o carro está abastecido."""
        print("The tank is filling up... Now it's full.")