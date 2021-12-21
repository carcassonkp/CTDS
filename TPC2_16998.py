import requests
import json
import os
from datetime import datetime

folder = "Covid2021"
file_name = "Covid_Braga.json"
file_path = os.path.join(folder, file_name)

sel_county='AMARES'
cases=[]
date=[]
with open(file_path) as f:
  data_1 = json.load(f)

dayOfTheYear = datetime.datetime.strptime(data['data'], '%d-%m-%Y').timetuple().tm_yday






