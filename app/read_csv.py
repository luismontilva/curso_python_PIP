import csv #Este modulo ayuda a leer CSV's

def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file,delimiter=',') #El delimitador es la forma en que vienen separados los datos (muchas veces es por una coma)
        header = next(reader) #De esta manera saco el header o primera linea, con el iterador pasar a las lineas de data.
        data = [] #En esta lista se ira guardando cada diccionario de cada pais.
        for row in reader: #recorrere cada linea y ire asociando cada valor a las llaves
            iterable = list(zip(header, row)) #Esto va a crear una lista de tuplas, donde colocara el header con el valor en cada caso.
            country_dict = {header: row for header, row in iterable} #de esta manera asigno la llave y valor para crear el diccionario
            data.append(country_dict) #En cada iteracion ira a gregando a la lista los diccionarios.
        return data

if __name__ == "__main__":
    data = read_csv('./data.csv')
    print(data[0]) #De esta manera puedo mostrar todos los paises, o ir al indice que desee.

#Esto me traeria la informacion como un array (columna por columna), pero sin especificar a que columna pertenece. Lo ideal seria pasarlo a diccionario.

#Convertir lista a lista de diccionarios

#Reader sera el que iterara
    