import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pymysql
# from index import *
def con():
    return pymysql.connect(host='10.73.100.101', user='VP', database='vansplanning', password='1234@@it.', port=3306)
# Fetch the service account key JSON file contents
cred = credentials.Certificate("src/key.json")

# Initialize the app with a service account, granting admin privileges

today = datetime.datetime.today().strftime('%Y-%m-%d')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://saccom-tm-default-rtdb.firebaseio.com',

})

#
# users = db.reference('users')
# # users = ref.child('users')
# print(users.child('YassineBaghdadi').get())
cnx = con()
cur = cnx.cursor()
# cur.execute('select concat(firstName, LastName) as fullName , username, pass from users;')
# dt = cur.fetchall()
# for d in dt:
#     if not users.child(f'{d[0]}').get():
#
#         users.child(f'{d[0]}').set({
#                 'username' : d[1],
#                 'pass' : d[2],
#             }
#         )

drvrs = db.reference('drivers')
cur.execute('select username, pass from drivers;')
# drivers = cur.fetchall()
# for d in drivers:
#     if not drvrs.child(f'{d[0]}').get():
#
#         drvrs.child(f'{d[0]}').set({'pass' : d[1],})
#
# drivers_firebase = db.reference('drivers')

cur.execute(f'''select t.id, v.matr, d.username as driverName , t.datetime, (select count(id) from trips_history where trip = t.id) as Agent_numbers, t.ttype
                    from trips t inner join vans v on t.van = v.id inner join drivers d on t.driver = d.id where date(t.datetime) < "{today} 00:00:00" order by t.datetime;''')

toDelete = cur.fetchall()
# # TODO the old Trips
for i in toDelete:
    tt = drvrs.child(f'{i[2]}').child('trips').child(f'{i[3]}')
    if tt.get():
        tripID  = tt.child("id").get()
        print(f"tripID = {tripID}")
        print(tt.child("agents").get())
        agents = tt.child("agents").get()
        print(type(agents))
        if agents:
            for ag in agents:
                try:
                    print(ag)
                    print(type(ag))
                    cur.execute(f'''update trips_history set picktime = "{ag['picktime']}", pickloc = "{ag["pickloc"]}", droptime = "{ag["droptime"]}", droploc = "{ag["droploc"]}", presence = "{ag["presence"]}"
                    where trip = {tripID} and agent = {str(ag["name"]).split(" ")[0]}''')
                    cnx.commit()
                except Exception as e:
                    # cur.execute(f"insert into logs(user, query, status, desc)value("", "", "", "")")
                    # cnx.commit()
                    print(e)
    tt.delete()



# #
# cur.execute(f'''select t.id, v.matr, d.firstName as driverName , t.datetime, (select count(id) from trips_history where trip = t.id) as Agent_numbers, t.ttype
#                     from trips t inner join vans v on t.van = v.id inner join drivers d on t.driver = d.id where date(t.datetime) >= "{today} 00:00:00" order by t.datetime;''')
#
# cur.execute(f'''select t.id, v.matr, d.username as driverName , t.datetime, (select count(id) from trips_history where trip = t.id) as Agent_numbers, t.ttype
#                     from trips t inner join vans v on t.van = v.id inner join drivers d on t.driver = d.id  order by t.datetime;''')
# #
# trips = cur.fetchall()
# #
# for trip in trips:
#     trp = drvrs.child(f'{trip[2]}').child('trips').child(f'{trip[3]}')
#     cur.execute(f'''select a.id, concat(a.firstName, " ", a.LastName) as fullName,
#                                     g.name, a.pic from trips_history th inner join agents a on th.agent = a.id inner join grps g on a.grp = g.id
#                                     where th.trip = {int(trip[0])};''')
#
#
#
#     # pics = ["https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg", "https://images.pexels.com/photos/2078265/pexels-photo-2078265.jpeg",
#     #         "https://images.pexels.com/photos/6962024/pexels-photo-6962024.jpeg",
#     #         "https://images.pexels.com/photos/7148620/pexels-photo-7148620.jpeg",
#     #         "https://images.pexels.com/photos/6214874/pexels-photo-6214874.jpeg",
#     #         "https://images.pexels.com/photos/7013617/pexels-photo-7013617.jpeg",
#     #         "https://images.pexels.com/photos/4924538/pexels-photo-4924538.jpeg",
#     #         "https://images.pexels.com/photos/6962008/pexels-photo-6962008.jpeg",
#     #         "https://images.pexels.com/photos/5032023/pexels-photo-5032023.jpeg",
#     #         "https://images.pexels.com/photos/7654096/pexels-photo-7654096.jpeg",
#     #         "https://images.pexels.com/photos/6195663/pexels-photo-6195663.jpeg",]
#     # agents = [i[0] for i in cur.fetchall()]
#     # agents = {}
#     # for agent in cur.fetchall():
#     #     agents[agent[0]] = agent[1]
#     import random
#     agents = [{"name" : f"{i[0]} - {i[1]}", "phone" : "0630504606", "pic" : i[3], "grp" : i[2], "droptime":"", "droploc":"", "picktime":"", "pickloc":"", "presence":""} for i in cur.fetchall()]
#
#     print(f'Agents : {agents}')
#     if not trp.get():
#
#         trp.set({
#             'id' : trip[0],
#             'agents' : agents,
#
#         })
#
# print(trips)
cnx.close()
