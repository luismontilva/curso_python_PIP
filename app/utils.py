def get_population(country_dict):
    population_dict = {
        '1970': int(country_dict['1970 Population']),
        '1980': int(country_dict['1980 Population']),
        '1990': int(country_dict['1990 Population']),
        '2000': int(country_dict['2000 Population']),
        '2010': int(country_dict['2010 Population']),
        '2015': int(country_dict['2015 Population']),
        '2020': int(country_dict['2020 Population']),
        '2022': int(country_dict['2022 Population']), #Hay que convertir estos valores a enteros, ya que al venir de un csv los toma ne cuenta como string
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

a = 'hola'

def get_population_by_country(data, country):
    result = list(filter(lambda item : item['Country/Territory'] == country, data))
    return result

#Esta ultima funcion recibe una lista (de diccionarios) "data", la cual a partir de un filter vamos a filtrar el pais que estemos buscando, especificandolo en "country".