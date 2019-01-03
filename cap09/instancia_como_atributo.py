#       Ao modelar algo do mundo relm no código, poderá perceber que está
#       adicionando cada vez mais detalhes em uma classe. Poderá notar que há
#       uma lista cresccente de atributos e métodos e que os arquivos estão
#       começando a ficar extensos. Nessas situações, talvez perceba que parte
#       de uma classe pode ser escrita como uma classe separada. Sua classe
#       maior poderá ser divida em partes menores que funcionem como conjunto.

#
#       Classe Car:
#

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


#
#       Classe ElectricCar filha de Car:
#

class ElectricCar(Car):
    """Representa aspectos de um carro específicos de veículos elétricos."""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


#
#       Classe Battery:
#

class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro elétrico."""

    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())


#       Quando quisermos descrever a bateria, precisaremos trabalhar com o
#       atributo 'battery' do carro elétrico:
#       Essa linha diz a Python para usar a instância my_tesla, encontrar seu
#       atributo 'battery' e chamar o método 'describe_battery()' associado à
#       instância de 'Battery' armazenada no atributo.

my_tesla.battery.describe_battery()