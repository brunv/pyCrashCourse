#       Trabalhando com classes e instâncias: Umas das primeras tarefas que
#       podemos fazer é modificar os atributos associados a uma instância
#       em particular. Há 3 formas de fazermos isso:

class Car():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

#       Definindo um valor default para um atributo:
#       Todo atributo de uma classe precisa de um valor inicial, mesmo que
#       esse valor seja 0 ou uma string vazia. Em alguns casos, por exemplo,
#       faz sentido especificar esse valor inicial no corpo do método 'init';
#       se isso for feito para um atributo, não será necessário incluir um
#       parâmetro para ele.

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


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


#
#       Modificando o valor de um atributo diretamente:
#

my_new_car.odometer_reading = 2000
my_new_car.read_odometer()


#
#       Modificando o valor de um atributo com um método:
#

my_new_car.update_odometer(100)
my_new_car.read_odometer()


#
#       Incrementando o valor de um atributo com um método:
#

my_new_car.increment_odometer(-200)
my_new_car.read_odometer()