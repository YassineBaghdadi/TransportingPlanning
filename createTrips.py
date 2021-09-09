from index import *
tday = '2021-09-09'
trips_time = 8
trip_type = 'IN'
driver = 1
van = 1


cnx = con()
cur = cnx.cursor()

cur.execute(f'''select count(id) from trips where datetime like "{tday} {trips_time if trips_time > 9 else f"0{trips_time}"}:00:00";''')
if not cur.fetchone()[0]:
    beforHour = trips_time -1
    cur.execute(f'''select count(id) from trips where datetime like "{tday} {beforHour if beforHour > 9 else f"0{beforHour }"}:00:00" and driver = {driver} and van = {van};''')
    if not cur.fetchone()[0]:
        cur.execute(f'''insert into trips (van, driver, datetime, ttype)values ({van}, {driver}, "{tday} {trips_time if trips_time > 9 else f"0{trips_time}"}:00:00", "{trip_type}")''')
        cnx.commit()
        cur.execute(f'''select id from trips where datetime like "{tday} {trips_time if trips_time > 9 else f"0{trips_time}"}:00:00"''')
        trip_id = cur.fetchone()[0]
        if 7 > trips_time > 20:

        else:
            cur.execute(f'''select a.id from agents a inner join grps g on a.grp = g.id where g.shift like "{f"{trips_time if trips_time > 9 else f'0{trips_time}'}-%" if trip_type == 'IN' else f"%-{trips_time if trips_time > 9 else f'0{trips_time}'}"}"''')
            agents = [i[0] for i in cur.fetchall()]
            if agents:
                query = f'''insert into trips_history(trip, agent) values {[f"({trip_id}, {agent})" for agent in agents]}'''.replace('[', '').replace(']', '').replace("'", "")
                print(query)
                cur.execute(query)
                cnx.commit()





    else:
        print('cant create this trip right now')

else:
    print('the trip already exists ...')


cnx.close()