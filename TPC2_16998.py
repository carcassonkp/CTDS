import requests
import json
import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


folder = "Covid2021"
file_name = "Covid_Braga.json"
file_path = os.path.join(folder, file_name)

counties_Braga = ["AMARES", "BARCELOS", "BRAGA", "CABECEIRAS DE BASTO", "CELORICO DE BASTO",
                  "ESPOSENDE", "FAFE","GUIMARÃES", "PÓVOA DE LANHOSO", "TERRAS DE BOURO", "VIEIRA DO MINHO",
                   "VILA NOVA DE FAMALICÃO","VILA VERDE","VIZELA"]
counties_poly =[7,8,9,10,6,8,8,8,8,7,7,8,9,8]

dict_counties = {}
for key in counties_Braga:
    for value in counties_poly:
        dict_counties[key] = value
        counties_poly.remove(value)
        break

print(dict_counties)


with open(file_path) as f:
  data_1 = json.load(f)

for key,value in dict_counties.items():
  sel_county=key
  deg_county=value
  cases = []
  day_Year = []
  for entry in data_1:
    if entry['concelho'] == sel_county:
      # day_obj=datetime.strptime(entry['data'], '%d-%m-%Y')
      day = datetime.strptime(entry['data'], '%d-%m-%Y').timetuple().tm_yday
      # se for 6 de janeiro entao guarda o valor 6/365, se for 28 fev guarda o valor 59/365
      num_cases=entry['confirmados_1']
      cases.append(num_cases)
      day_Year.append(day)


  model=np.poly1d(np.polyfit(day_Year,cases,deg_county))

  curvy_line = np.linspace(1, day_Year[len(day_Year)-1], 1000)
  prediction_line = np.linspace(day_Year[len(day_Year)-1], 455, 1000)
  plt.axis([None, None, -20, 200])
  plt.plot(day_Year,cases,'o')
  plt.xlabel('Day of Year')
  plt.ylabel('Covid Cases')
  plt.plot(curvy_line,model(curvy_line), color='green')
  plt.plot(prediction_line,model(prediction_line), color='red')
  plt.legend(['Covid cases','Polynomial Model Degree ({})'.format(deg_county),'Next 3 months'])
  plt.title("COVID CASES IN {}".format(sel_county))
  plt.show()












