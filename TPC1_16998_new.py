
import json
import os
from datetime import datetime
import requests
from base64 import b64encode

# API authentication header
userAndPass = b64encode(b"alunos.ipca.pt:*U,+z7:[(!-Xwku3").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}

# request to the API

folder = "Covid2021"
file_name = "Covid_Braga.json"

if not os.path.exists(folder):  # criar pasta caso não exista
    os.mkdir(folder)
file_path = os.path.join(folder, file_name)
print(file_path)

if os.path.exists(file_path):  # se já existir um ficheiro json este será removido visto que se corrermos script sem remover o ficheiro estaremos a adicionar dados repetidos
    os.remove(file_path)

date_format = "%d-%m-%Y"
start_date = "01-01-2021"
end_date = "21-12-2021"
start_date_obj = datetime.strptime(start_date, date_format)
end_date_obj = datetime.strptime(end_date, date_format)


r_all_counties_by_date = requests.get("https://covid19-api.vost.pt/Requests/get_entry_counties/{}_until_{}".format(start_date, end_date), headers=headers)

my_keys = ['data', 'concelho', 'confirmados_1']
Data_to_store=[]

for entry in r_all_counties_by_date.json():
    compare_date_obj = datetime.strptime(entry['data'], date_format)
    if entry['distrito']=='BRAGA' and start_date_obj <= compare_date_obj <= end_date_obj:
        entry_1 = {k: v for (k, v) in entry.items() if k in my_keys}
        Data_to_store.append(entry_1)

with open(os.path.join(folder,file_name), "a") as fp:
    json.dump(Data_to_store, fp)




