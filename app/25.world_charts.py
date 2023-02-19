from utils import get_population, get_population_by_country
import read_csv
import charts

#Grafincando poblaciones

def run():
    data = read_csv.read_csv('./data.csv')
    continent = str(input('Indica el continente que deseas filtrar: '))
    data = list(filter(lambda item: item['Continent'] == continent, data))
    precentages_dict = {item['Country/Territory']: item['World Population Percentage'] for item in data}

    country = precentages_dict.keys()
    per = precentages_dict.values()

    charts.generate_pie_chart(continent,country, per)


if __name__ == "__main__":
    run()