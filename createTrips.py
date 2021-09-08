from index import *

trips_time = 8



cnx = con()
cur = cnx.cursor()
cur.execute(f'select * from agents a inner join grps g on a.grp = g.id where g.shift like "{trips_time if trips_time>9 else f"0{trips_time}"}%" group by zone')
agents = cur.fetchall()
print(agents)

cnx.close()