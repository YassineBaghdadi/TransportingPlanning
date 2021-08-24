import datetime
from calendar import calendar
from time import strftime, gmtime

import pymysql


def con():
    return pymysql.connect(host='10.73.100.101', user='VP', database='vansplanning', password='1234@@it.', port=3306)


def createTrips():
    today = datetime.date.today()
    day = datetime.datetime.today().strftime('%A')
    print(day)
    if day.lower() == "Friday".lower():
        tomorrow = datetime.date.today() + datetime.timedelta(days=3)
    else:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)


    print(tomorrow)
    cnx = con()
    cur = cnx.cursor()
    cur.execute('select shift from grps')
    data = []
    for r in cur.fetchall():
        for c in r:
            for cc in str(c).split('-'):
                data.append(int(cc))
    dt = [i for i in set(sorted(data))]
    data = []
    for i in dt:
        if i < 10:
            data.append(f'0{i}')
        else:
            data.append(str(i))
    print(data)
    trips = {}
    total = 0
    ids = []
    for h in data:
        query = ''
        if int(h) < 15:
            query = f'select a.id from agents a inner join grps g on a.grp = g.id where g.shift like "{h}-%"'
        else:
            query = f'select a.id from agents a inner join grps g on a.grp = g.id where g.shift like "%-{h}"'

        cur.execute(query)
        result = cur.fetchall()
        print(result)

        count = len(result)

        trips[h] = [i[0] for i in result]
        total += count

    print(trips)
    print(total)
    maxForVan = 18
    for time, agents in trips.items():
        vansNeeded = 0
        if len(agents) > maxForVan:
            vansNeeded = 2
        else:
            vansNeeded = 1

        for i in range(vansNeeded):






createTrips()