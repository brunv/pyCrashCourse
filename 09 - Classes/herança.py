#       Se a classe que você estiver escrevendo for uma versão especializada de
#       outra classe já criada, a herança poderá ser usada. Quando uma classe
#       herda outra, ela assumirá automaticamente todos os atributos e métodos
#       da primeira classe. A classe original se chama classe-pai e a nova é a
#       classe-filha. Portanto, a classe-filha herda todos os atributos e
#       métodos da classe-pai, mas também é livre para definir novos atributos
#       e métodos próprios.

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


#
#       Classe ElectricCar herdando da classe Car:
#

#       O nome da classe-pai deve ser incluído entre parênteses na definição
#       da classe-filha, indicando a herança.

#       A primeira tarefa de Python ao criar uma instância de uma classe-filha
#       é atribuir valores a todos os atributos da classe-pai. Para isso, o
#       método 'init' de uma classe-filha precisa da ajuda de sua classe-pai.

#       A função 'super()' é uma função especial que ajuda Python a criar
#       conexões entre a classe-pai e a classe-filha. Em seguida (76), ela diz a
#       Python para chamar o método 'init' da classe-pai de ElectricCar, que
#       confere todos os atributos da classe-pai a ElectricCar. O nome super é
#       derivado de uma convenção segundo a qual a classe-pai chama superclasse
#       e a classe-filha é a subclasse.


class ElectricCar(Car):
    """Representa aspectos de um carro específicos de veículos elétricos."""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

#       Qualquer método da classe-pai que não se enquade no que estiver tentando
#       modelar com a classe-filha pode ser sobrescrito. Para isso, defina um
#       método na classe-filha com o mesmo nome do método da classe-pai. Assim,
#       Python desprezará o método da classe-pai e só prestará atenção no método
#       definido na classe-filha. Exemplo:

    def fill_gas_tank(self):
        """Carros elétricos não têm tanques de gasolina."""
        print("This car doesn't have a gas tank!")


my_tesla = ElectricCar('tesla','model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


#       Depois que tiver um classe-filha que herde de uma classe-pai, podemos
#       adicionar qualquer atributo ou método novo necessários para diferenciar
#       a classe-filha da classe-pai.
