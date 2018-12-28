#       Podemos usar argumentos posicionais, que devem estar na mesma ordem em que os
#       parâmetros foram escritos, argumentos nomeados (keyword arguments), em que cada
#       argumentoé constituído de um nome de variável e de um valor, ou por meio de
#       listas e de dicionários de valores.


#       Argumentos Posicionais:

def describre_pet(animal_type, pet_name, pet_age):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("\nHis name is " + pet_name.title() + " and he is " + str(pet_age) + " yrs old.")

describre_pet('cat', 'cristal', 6)


#       Argumento Nomeados:

describre_pet(pet_age=8, animal_type='dog', pet_name='joe')


#       Valores default:

def exponencial(num, exp=2):
    """Eleva um numero dado à uma potência dada."""
    result = num ** exp
    print(result)

exponencial(2,3)    # 8
exponencial(2)      # 4


#       Retornando resultados:

def get_exponencial(num, exp):
    """Retorna um numero dado elevado à uma potência dada."""
    return num ** exp

result = get_exponencial(2,4)
print(result)       # 16


#       Retornando um Dicionário:

def build_person(first_name, last_name, age=''):
    """Retorna um dicionário com informações de uma pessoa."""
    person = {
        'first': first_name.title(),
        'last': last_name.title()
    }

    if age:
        person['age'] = age
    
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)