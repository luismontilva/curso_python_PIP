import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200,34,150]

    fig, ax = plt.subplots() #obtenemos la figura (fig) y las coordenadas (ax) desde plt.subplots
    ax.pie(values, labels=labels) #De esta manera especifico que quieor un grafico de pie y defino que argumentos iran.

    #plt.show() #Permite mostrar en una ventana el grafico
    plt.savefig('pie.png') #De esta manera guardara el grafico en un archivo como tal en la carpetas
    plt.close() #Esto dejara de ejecutar la generacion del grafico una vez finalice de guardar.

    
