#
#       Utilizando os países e códigos do Pygal
#

from pygal.maps.world import COUNTRIES

# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
    """Devolve o código de duas letras do Pygal para um país, dado o seu nome."""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    
    #   Se o país não foi encontrad, devolve None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))