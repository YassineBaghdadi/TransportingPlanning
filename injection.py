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
# print(file)
# print(cols)
agents = []



def preparingDB():

    cur.execute(f'create database if not exists {database};')
    cur.execute('''Create table if not exists users (id  INT AUTO_INCREMENT, firstName Varchar(50), LastName Varchar(50), username Varchar(50), pass Varchar(50), role INT , PRIMARY KEY (id));''')
    cur.execute('''create table if not exists grps (id  INT AUTO_INCREMENT, name Varchar(50), shift Varchar(20) , PRIMARY KEY (id));''')
    cnx.commit()
    cur.execute('''create table if not exists agents (id  INT AUTO_INCREMENT, matrr varchar(50) not null, firstName Varchar(50), LastName Varchar(50), CIN varchar(50), address Varchar(100), grp int, rpr  Varchar(100), rpr_map varchar(100), pic text, PRIMARY KEY (id), foreign key(grp) references grps(id));''')
    cur.execute('''create table if not exists vans (id  INT AUTO_INCREMENT, matr Varchar(50), driver varchar(50), max_places int , PRIMARY KEY (id))''')
    cur.execute('''create table if not exists vans(id  INT AUTO_INCREMENT, matricule varchar(50), max_places int , PRIMARY KEY (id))''')
    cur.execute('''create table if not exists drivers(id  INT AUTO_INCREMENT, firstName Varchar(50), LastName varchar(50), username Varchar(45), pass Varchar(45), PRIMARY KEY (id))''')
    cnx.commit()

    cur.execute('create table if not exists trips(id  INT AUTO_INCREMENT, van int, driver int, datetime Varchar(50), ttype Varchar(5), starttime varchar(45), startloc varchar(45), stoptime varchar(45), stoploc varchar(45), counterkm varchar(45), tracking LONGTEXT, foreign key(van) references vans(id), foreign key(driver) references drivers(id) , PRIMARY KEY (id))')

    cnx.commit()
    cur.execute('''create table if not exists trips_history(id  INT AUTO_INCREMENT,trip int, agent int, presence varchar(50), picktime varchar(50), pickloc varchar(50), droptime varchar(50), droploc varchar(50), foreign key(trip) references trips(id), foreign key(agent) references agents(id), PRIMARY KEY (id))''')
    cnx.commit()
    cur.execute("CREATE TABLE if not exists logsfile (id INT AUTO_INCREMENT,user VARCHAR(45) ,query VARCHAR(500) ,status VARCHAR(50), descr VARCHAR(500) ,PRIMARY KEY (id))")
    cnx.commit()
    # cur.execute()
    cur.execute("select id from trips")
    for i in cur.fetchall():
        cur.execute(f"""select count(id) from trips_history where trip = {i[0]}""")

        if int(cur.fetchone()[0]) == 0:
            cur.execute(f"delete from trips where id = {i[0]}")
            cnx.commit()



    cnx.close()
    #print('tables created ')


preparingDB()

for index, row in file.iterrows():
    r = []
    for c in row:
        r.append(str(c).replace("'", ''))
    agents.append(r)



# print(agents[0])
# for i in agents[0]:
#     print(f'type({i}) ==> {type(i)} == nan : {str(i) == "nan"}')

cnx.ping(reconnect=True)
pic = 'https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'
for ag in agents:
        print(ag)
        cur.execute(f'''insert into agents (matrr, firstName, LastName, CIN, address, grp, rpr, rpr_map, pic) values('{ag[0]}', '{ag[2]}', '{ag[1]}', '{ag[3]}', '{ag[4]}', {int(ag[5])}, '{ag[6]}', '{ag[7]}', '{pic}')''')
        cnx.commit()
    # try:
    #
    #     cur.execute(f'insert into agents (matrr, firstName, LastName, CIN, address, grp, rpr, rpr_map) values("{ag[0] if ag[0] else 0}", "{ag[2] if ag[2] else 0}", "{ag[1] if ag[1] else 0}", "{ag[3] if ag[3] else 0}", "{ag[4] if ag[4] else 0}", {int(ag[5]) if ag[5] else 0}, "{ag[6] if ag[6] else 0}", "{ag[7] if ag[7] else 0}")')
    #     cnx.commit()
    #
    #     print(f"{ag[0]} ==> {ag[1]} {ag[2]} : ADDED successfully .")
    # except Exception as e:
    #     print(f"{ag[0]} ==> {ag[1]} {ag[2]} : ADDED FAILLED . ====> {e}")

    # print(ag)



cnx.close()