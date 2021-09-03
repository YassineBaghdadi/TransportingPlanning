# import datetime
# from calendar import calendar
# from time import strftime, gmtime
#
# import pymysql
#
#
# def con():
#     return pymysql.connect(host='10.73.100.101', user='VP', database='vansplanning', password='1234@@it.', port=3306)
#
#
# def createTrips():
#     today = datetime.date.today()
#     day = datetime.datetime.today().strftime('%A')
#     print(day)
#     if day.lower() == "Friday".lower():
#         tomorrow = datetime.date.today() + datetime.timedelta(days=3)
#     else:
#         tomorrow = datetime.date.today() + datetime.timedelta(days=1)
#
#     tomorrow = today #TODO Just for test
#     print(tomorrow)
#     cnx = con()
#     cur = cnx.cursor()
#     cur.execute('select shift from grps')
#     data = []
#     for r in cur.fetchall():
#         for c in r:
#             for cc in str(c).split('-'):
#                 data.append(int(cc))
#     dt = [i for i in set(sorted(data))]
#     data = []
#     for i in dt:
#         if i < 10:
#             data.append(f'0{i}')
#         else:
#             data.append(str(i))
#     # print(data)
#     trips = {}
#     total = 0
#     ids = []
#     for h in data:
#         query = ''
#         if int(h) < 15:
#             query = f'select a.id from agents a inner join grps g on a.grp = g.id where g.shift like "{h}-%"'
#         else:
#             query = f'select a.id from agents a inner join grps g on a.grp = g.id where g.shift like "%-{h}"'
#
#         cur.execute(query)
#         result = cur.fetchall()
#         # print(result)
#
#         count = len(result)
#
#         trips[h] = [i[0] for i in result]
#         total += count
#
#     print(trips)
#     print(total)
#     maxForVan = 18
#     for time, agents in trips.items():
#         vansNeeded = 0
#         if agents:
#             if len(agents) > maxForVan:
#                 vansNeeded = 2
#             else:
#                 vansNeeded = 1
#
#             if vansNeeded == 1:
#                 cur.execute(f''' select count(id) from trips where datetime like "{tomorrow} {time}:00:00" and van = 1''')
#                 if not cur.fetchone()[0]:
#                     cur.execute(f'''insert into trips(van, driver, datetime) values (1, 1, "{tomorrow} {time}:00:00");''')
#                     cnx.commit()
#                     for agent in agents:
#                         cur.execute(f'''select id from trips where datetime like "{tomorrow} {time}:00:00"''')
#                         cur.execute(f'''insert into trips_history (trip, agent, presence) values ({int(cur.fetchone()[0])}, {agent}, 0)''')
#                         cnx.commit()
#             else:
#                 grp1 = [i for i in agents[:len(agents)//2]]
#                 grp2 = [i for i in agents[len(agents)//2:]]
#                 cur.execute(f'''select count(id) from trips where datetime like "{tomorrow} {time}:00:00" and driver = 1''')
#                 if not cur.fetchone()[0]:
#                     cur.execute(f'''insert into trips(van, driver, datetime) values (1, 1, "{tomorrow} {time}:00:00");''')
#
#                 cur.execute(f'''select id from trips where datetime like "{tomorrow} {time}:00:00"''')
#
#                 trip1, trip2 = [int(i[0]) for i in cur.fetchall()]
#                 for agent in grp1:
#                     cur.execute(f'''select count(id) from trips_history where trip = {trip1} and agent = {agent}''')
#                     if not cur.fetchone()[0]:
#                         cur.execute(f'''insert into trips_history (trip, agent, presence) values ({trip1}, {agent}, 0)''')
#                         cnx.commit()
#
#
#                 cur.execute(f'''select count(id) from trips where datetime like "{tomorrow} {time}:00:00" and driver = 1''')
#                 if not cur.fetchone()[0]:
#                     cur.execute(f'''insert into trips(van, driver, datetime) values (2, 2, "{tomorrow} {time}:00:00");''')
#                 cnx.commit()
#                 for agent in grp2:
#                     cur.execute(f'''select count(id) from trips_history where trip = {trip2} and agent = {agent}''')
#                     if not cur.fetchone()[0]:
#                         cur.execute(f'''insert into trips_history (trip, agent, presence) values ({trip2}, {agent}, 0)''')
#                         cnx.commit()
#     cnx.close()
#
#
#
#
#
#
#
#
#
#
#
#
# createTrips()


#########################################################################################################################
#
# from index import *
# import os, pymysql
# from openpyxl import load_workbook
# import PyQt5
#
# workbook = load_workbook(filename = os.path.join(os.getcwd(), 'src', 'template.xlsx'))
# sheet = workbook.active
#
# cnx = con()
# cur = cnx.cursor()
# cur.execute('select a.firstName, a.LastName, g.name from trips_history th inner join agents a on th.agent = a.id inner join trips t on th.trip = t.id inner join grps g on a.grp = g.id  where t.id = 43 ')
# data = cur.fetchall()
#
# sheet['C1'] = 'Trip Id / Driver Name'
# sheet['C2'] = 'Date Time '
#
# print(data)
# cc = [i for i in 'A B C '.split()]
# print(cc)
# for i in range(4, len(data)):
#     for c in range(len(cc)):
#         sheet[f"{cc[c]}{i}"] = data[i][c]
#         print(f"{cc[c]}{i}")
#
# fileName = 'test.xlsx'
# workbook.save(filename = fileName)
# os.startfile(fileName)


############################################################################################################################################


import pymysql, index

cnx = index.con()
cur = cnx.cursor()
cur.execute('select id from trips ')
# for i in cur.fetchall():
#     cur.execute(f'''update trips set ttype = '{"IN" if int(str(i[1]).split(" ")[1].split(":")[0]) < 15 else "OUT"}' where id = {i[0]}''')
#     cnx.commit()

print(cur.fetchall())

cnx.close()