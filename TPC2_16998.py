import requests
import json
import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, r2_score

folder = "Covid2021"
file_name = "Covid_Braga.json"
file_path = os.path.join(folder, file_name)

sel_county='VIZELA'
# counties_Braga = ["AMARES", "BARCELOS", "BRAGA", "CABECEIRAS DE BASTO", "CELORICO DE BASTO",
#                   "ESPOSENDE", "FAFE",
#                   "GUIMARÃES", "PÓVOA DE LANHOSO", "TERRAS DE BOURO", "VIEIRA DO MINHO", "VILA NOVA DE FAMALICÃO",
#                   "VILA VERDE",
#                   "VIZELA"]

cases=[]
day_Year=[]
with open(file_path) as f:
  data_1 = json.load(f)

for entry in data_1:
  if entry['concelho'] == sel_county:
    # day_obj=datetime.strptime(entry['data'], '%d-%m-%Y')
    day = datetime.strptime(entry['data'], '%d-%m-%Y').timetuple().tm_yday
    # se for 6 de janeiro entao guarda o valor 6/365, se for 28 fev guarda o valor 59/365
    num_cases=entry['confirmados_1']
    cases.append(num_cases)
    day_Year.append(day)

for i in range(len(cases)):
  print("Day: ", day_Year[i])
  print("Cases: ", cases[i])

model=np.poly1d(np.polyfit(day_Year,cases,deg=8))
###########
daily_prediction=343
cases_prediction = model(daily_prediction)
print("Prediction for day {}".format(daily_prediction))
print("{} cases".format(round(cases_prediction)))
#################
curvy_line = np.linspace(1, day_Year[len(day_Year)-1], 1000)
prediction_line = np.linspace(day_Year[len(day_Year)-1], 455, 1000)
plt.axis([None, None, -20, 200])

# plt.scatter(day_Year,cases,s=4)
plt.plot(day_Year,cases,'o')
plt.xlabel('Day of Year')
plt.ylabel('Covid Cases')
plt.plot(curvy_line,model(curvy_line), color='green')
plt.plot(prediction_line,model(prediction_line), color='red')
plt.legend(['Covid cases','Polynomial Model','Next 3 months'])
plt.title("COVID CASES IN {}".format(sel_county))
plt.show()











