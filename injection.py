import os, openpyxl, sys, pandas as pd, pymysql, json

import bcolors as bcolors

server = json.load(open(os.path.join(os.getcwd(), "server.json")))
host = server["host"]
user = server["user"]
database = server["db"]
psswrd = server["password"]
port = server["port"]

cnx = pymysql.connect(host=host, user=user, database=database, password=psswrd, port=port)
cur = cnx.cursor()
file = pd.read_excel(sys.argv[1])
cols = [i for i in file.columns[:6]]
print(cols)
agents = []

for index, row in file.iterrows():
    agents.append([row['Matriculation'], row['Nom'], row['Prenom'], row['CIN'], row['Adress'], row['Group']])


print(agents)
for ag in agents:
    try:
        cur.execute(f'insert into agents (matrr, firstName, LastName, CIN, address, grp) values("{ag[0]}", "{ag[1]}", "{ag[2]}", "{ag[3]}", "{ag[4]}", {int(ag[5])})')
        cnx.commit()

        print(f"{ag[0]} ==> {ag[1]} {ag[2]} : ADDED successfully .")
    except Exception as e:
        print(f"{ag[0]} ==> {ag[1]} {ag[2]} : ADDED FAILLED . ====> {e}")



