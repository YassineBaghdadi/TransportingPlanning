
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pymysql
from index import *

# Fetch the service account key JSON file contents
cred = credentials.Certificate("src/key.json")

# Initialize the app with a service account, granting admin privileges


firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://saccom-tm-default-rtdb.firebaseio.com',

})


users = db.reference('users')
# users = ref.child('users')
print(users.child('YassineBaghdadi').get())
cnx = con()
cur = cnx.cursor()
cur.execute('select concat(firstName, LastName) as fullName , username, pass from users;')
dt = cur.fetchall()
for d in dt:
    if not users.child(f'{d[0]}').get():

        users.child(f'{d[0]}').set({
                'username' : d[1],
                'pass' : d[2],
            }
        )

drvrs = db.reference('drivers')
cur.execute('select concat(firstName, LastName) as fullName , username, pass from drivers;')
users = cur.fetchall()
for d in users:
    if not drvrs.child(f'{d[0]}').get():

        drvrs.child(f'{d[0]}').set({
                'username' : d[1],
                'pass' : d[2],
            }
        )

drivers_firebase = db.reference('drivers')

cur.execute(f'''select t.id, v.matr, CONCAT(d.firstName, d.LastName) as driverName , t.datetime, (select count(id) from trips_history where trip = t.id) as Agent_numbers, t.ttype
                    from trips t inner join vans v on t.van = v.id inner join drivers d on t.driver = d.id where date(t.datetime) < "{today} 00:00:00" order by t.datetime;''')

toDelete = cur.fetchall()

for i in toDelete:
    drivers_firebase.child(f'{i[2]}').child('trips').child(f'{i[3]}').delete()


cur.execute(f'''select t.id, v.matr, CONCAT(d.firstName, d.LastName) as driverName , t.datetime, (select count(id) from trips_history where trip = t.id) as Agent_numbers, t.ttype
                    from trips t inner join vans v on t.van = v.id inner join drivers d on t.driver = d.id where date(t.datetime) >= "{today} 00:00:00" order by t.datetime;''')

trips = cur.fetchall()

for trip in trips:
    trp = drivers_firebase.child(f'{trip[2]}').child('trips').child(f'{trip[3]}')
    cur.execute(f'''select concat(a.firstName, " ", a.LastName) as fullName
                                    from trips_history th inner join agents a on th.agent = a.id 
                                    where th.trip = {int(trip[0])};''')

    agents = [i[0] for i in cur.fetchall()]
    print(f'Agents : {agents}')
    if not trp.get():
        trp.set({
            'id' : trip[0],
            'agents' : agents,

        })

print(trips)
cnx.close()
