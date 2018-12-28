def make_pizza(*toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def make_sandwich(size, *toppings):
    """Apresenta o sanduíche que estamos prestes a preparar."""
    print("\nMaking a " + str(size) + "-inch sandwich with the folling toppings:")
    for topping in toppings:
        print("- " + topping)