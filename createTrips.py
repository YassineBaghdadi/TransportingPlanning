from index import *



def create_trip(date, type, driver, van):
    cnx = con()
    cur = cnx.cursor()

    tday, trips_time, trip_type = date.split(' ')[0], int(date.split(' ')[1].split(':')[0]), type
    cur.execute(f'''select count(id) from trips where datetime like "{date}";''')
    if not cur.fetchone()[0]:
        cur.execute(f'''select max_places from vans where id = {van}''')
        max_places = int(cur.fetchone()[0])
        beforHour = trips_time -1
        afterHour = trips_time +1
        cur.execute(f'''select count(id) from trips 
        where (datetime like "{tday} {beforHour if beforHour > 9 else f"0{beforHour }"}:00:00" 
        OR datetime like "{tday} {afterHour if afterHour > 9 else f"0{afterHour }"}:00:00") 
        and driver = {driver} and van = {van};''')
        if not cur.fetchone()[0]:

            if 6 > trips_time > 20:
                cur.execute('''select zone from agents''')
                zones = set(i[0] for i in cur.fetchall())
                zone1 = []
                zone2 = []
                for z in zones:
                    if z in ['Sidi Yahya', 'Sidi Ziane']:
                        zone1.append(z)
                    else:
                        zone2.append(z)

                cur.execute(f'''select id from agents where zone in ({[i for i in zone1]})'''.replace('[', '').replace(']', ''))

                agentZone1 = [i[0] for i in cur.fetchall()]

                cur.execute(f'''select id from agents where zone in ({[i for i in zone2]})'''.replace('[', '').replace(']', ''))

                agentZone2 = [i[0] for i in cur.fetchall()]

                for i in range(1, 3):
                    cur.execute(
                        f'''insert into trips (van, driver, datetime, ttype)values ({i}, {i}, "{tday} {trips_time if trips_time > 9 else f"0{trips_time}"}:00:00", "{trip_type}")''')
                    cnx.commit()
                    cur.execute(f'''select id from trips where datetime like "{date}" and van = {i} and diver = {i}''')
                    trip_id = cur.fetchone()[0]
                    if i == 1:
                        cur.execute(f'''insert into trips_histoy(trip, agent) values {[f"({trip_id}, {agent})" for agent in agentZone1]}'''.replace('[', '').replace(']', '').replace("'", ""))

                    if i == 2:
                        cur.execute(f'''insert into trips_histoy(trip, agent) values {[f"({trip_id}, {agent})" for agent in agentZone2]}'''.replace('[', '').replace(']', '').replace("'", ""))
                    cnx.commit()


            else:
                cur.execute(
                    f'''insert into trips (van, driver, datetime, ttype)values ({van}, {driver}, "{tday} {trips_time if trips_time > 9 else f"0{trips_time}"}:00:00", "{trip_type}")''')
                cnx.commit()
                cur.execute(f'''select id from trips where datetime like "{date}"''')
                trip_id = cur.fetchone()[0]
                cur.execute(f'''select a.id from agents a inner join grps g on a.grp = g.id inner join trips_history th on th.agent = a.id inner join trips t on th.trip = t.id
                where g.shift like "{f"{trips_time if trips_time > 9 else f'0{trips_time}'}-%" if trip_type == 'IN' else f"%-{trips_time if trips_time > 9 else f'0{trips_time}'}"}" 
                and t.datetime != "{date}" order by a.zone''')
                agents = [i[0] for i in set(cur.fetchall())]
                print(agents)
                if agents:
                    if len(agents) > max_places:

                        grp1 = [i for i in agents[:len(agents) // 2]]
                        for a in grp1:
                            # query = f'''insert into trips_history(trip, agent) values {[f"({trip_id}, {agent})" for agent in grp1]}'''.replace('[', '').replace(']', '').replace("'", "")
                            query = f'''insert into trips_history(trip, agent) values({trip_id}, {a}) ;'''
                            print(query)
                            cur.execute(query)
                            cnx.commit()
                        Trip_View(role=0, id=trip_id).show()
                        cur.execute(f'''select d.id from drivers d inner join trips t on t.driver = d.id  where d.id != (select driver from trips where id = {trip_id})''')
                        driver2 = cur.fetchone()[0]
                        cur.execute(f'''select v.id from vans v inner join trips t on t.van = v.id  where v.id != (select van from trips where id = {trip_id})''')
                        van2 = cur.fetchone()[0]
                        create_trip(date=date, driver=driver2, van=van2, type=trip_type)
                    else:
                        for a in agents:
                            # query = f'''insert into trips_history(trip, agent) values {[f"({trip_id}, {agent})" for agent in agents]}'''.replace('[', '').replace(']', '').replace("'", "")
                            query = f'''insert into trips_history(trip, agent) values({trip_id}, {a}) ;'''
                            print(query)
                            cur.execute(query)
                            cnx.commit()
                        Trip_View(role=0, id=trip_id).show()






        else:
            print('cant create this trip right now')

    else:
        print('the trip already exists ...')

    cnx.close()

create_trip(date='2021-09-17 18:00:00', type='OUT', driver=1, van=1)
