import matplotlib.pyplot as plt #Puedo colocarle un sinonimo a el modulo a traves de "as"

#Graficos

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots() #"fig" hara referencia a la figura y "ax" a las coordenadas. es una forma de extraerlas funcionalidades de matplot
    ax.bar(labels, values) #creare un barchar y voy a pasarle los labels (eje x), y los valores (eje y).
    plt.savefig(f'./paises/{name}.png') #con esto se mostrarael grafico
    plt.close

def generate_pie_chart(country, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels) #En el pie chart hay que especificar los argumentos de esta manera.
    ax.axis('equal') #con esto organizo el grafico en el centro y en forma de circulo
    plt.savefig(f'./continentes/{country}.png') #con esto lo muestro y renderizo.
    plt.close()

if __name__ == "__main__":
    labels = ['a', 'b', 'c']
    values = [10, 320, 110]
    #generate_bar_chart(labels, values)
    #generate_pie_chart(labels, values)