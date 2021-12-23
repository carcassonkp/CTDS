
import json
import os
from datetime import datetime
import requests
from base64 import b64encode

# API authentication header
userAndPass = b64encode(b"alunos.ipca.pt:*U,+z7:[(!-Xwku3").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}

# request to the API


counties_Braga = ["AMARES", "BARCELOS", "BRAGA", "CABECEIRAS DE BASTO", "CELORICO DE BASTO",
                  "ESPOSENDE", "FAFE",
                  "GUIMARÃES", "PÓVOA DE LANHOSO", "TERRAS DE BOURO", "VIEIRA DO MINHO", "VILA NOVA DE FAMALICÃO",
                  "VILA VERDE",
                  "VIZELA"]

folder = "Covid2021"
file_name = "Covid_Braga_test.json"

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

# r = requests.get(f'https://covid19-api.vost.pt/Requests/get_county_list/', headers=headers)
r_all_counties_by_date = requests.get("https://covid19-api.vost.pt/Requests/get_entry_counties/{}_until_{}".format(start_date, end_date), headers=headers)
# api_url =
# r_all_counties_by_date = requests.get(api_url),headers=headers
# print(r_all_counties_by_date.json())

cnt = 0
for entry in r_all_counties_by_date.json():
    compare_date_obj = datetime.strptime(entry['data'], date_format)
    # print(entry['data'])
    # print(compare_date_obj)
    # if entry['concelho'] in counties_Braga and entry['data'].endswith("2021"):
    if entry['concelho'] in counties_Braga and start_date_obj <= compare_date_obj <= end_date_obj:
        cnt += 1
        # print(entry['data'])
        # print(entry['concelho'])
        with open(file_path, "a") as fp:
            json.dump(entry, fp)

print(cnt)
