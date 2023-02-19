from utils import get_population, get_population_by_country
import read_csv
import charts

#Grafincando poblaciones

def run():
    data = read_csv.read_csv('./data.csv')
    country = str(input('Especifica el pais: '))
    result = get_population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == "__main__":
    run()