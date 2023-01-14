import matplotlib.pyplot as pyplot

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,34,120]

    fig, ax = pyplot.subplots()
    ax.pie(values, labels=labels)
    
    # En esta oportunidad no usaremos show para que no se detenga el programa.
    # En su lugar vamos a generar una imagen y que la guarde como png.
    #pyplot.show()

    pyplot.savefig('pie.png')
    pyplot.close()