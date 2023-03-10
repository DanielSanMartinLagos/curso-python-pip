import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''
  print('OK iniciando ejecucion con pandas')

  # Con pandas creamos un data frame direcatamente con la funcion read_csv, muy parecida la que creamos con anterioridad.
  df = pd.read_csv('data.csv')
  # filtramos inmediatamente
  df = df[df['Continent'] == 'Asia']
  # Obtengo los paises
  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)
  
  print('OK en medio de la ejecución')

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
  
  print('OK terminado!')

if __name__ == '__main__':
  run()