import utils #de esta manera importo el archivo "mod" creado en la misma carpeta

population = [
        {
        'country': 'colombia',
        'population': 150
        },
        {
        'country': 'bolivia',
        'population': 300
        }
    ] #sacar esta variable de la funcion run() permitiria que yo peudo acceder a esta varaible desde otro archivo sin tener que ejecutar todo el modulo

def run():
    keys, values = utils.get_population() #de esta manera puedo acceder a la funcion creada en el archivo "mod"

    print(keys, values) #Se imprimiran los valores dque defini en la funcion en el otro modulo.

    print(utils.a) #puedo acceder tambien a variables que esten en el otro modulo, y no solamente funciones.

    #Funcion get_population_by_country

    country = str(input('que pais deseas buscar: '))

    colombia = utils.get_population_by_country(population, country) #la funcion va a filtrarme el pais que que estoy buscando en la lista de poblacion.
    print(colombia) #solo me traera la data de colombia en una lista.

if __name__ == '__main__':
    run()

#Este if es valiosisimo, ya que especifica que si este archivo es ejecutado desde la terminal corra run(). Pero si es ejecutado como modulo, no lo haga.