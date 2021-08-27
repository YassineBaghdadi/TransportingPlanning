from time import gmtime, strftime

from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os, sys, datetime, pymysql, threading

from PyQt5.QtWidgets import QHeaderView
from plyer import notification






def notif(self = None, title = '', msg = ''):
    try:
        notification.notify(
            title=title,
            message=msg,
            app_icon=os.path.join(os.getcwd(), 'src/img/it.ico'),
            timeout=60,
        )
    except:
        QtWidgets.QMessageBox.about(self, title, msg)


def con():
    return pymysql.connect(host='10.73.100.101', user='VP', database='vansplanning', password='1234@@it.', port=3306)


def preparingDB():
    cnx = con()
    cur = cnx.cursor()
    cur.execute('''Create table if not exists users (id  INT AUTO_INCREMENT, firstName Varchar(50), LastName Varchar(50), username Varchar(50), pass Varchar(50), role INT , PRIMARY KEY (id));''')
    cur.execute('''create table if not exists grps (id  INT AUTO_INCREMENT, name Varchar(50), shift Varchar(20) , PRIMARY KEY (id));''')
    cnx.commit()
    cur.execute('''create table if not exists agents (id  INT AUTO_INCREMENT, firstName Varchar(50), LastName Varchar(50), CIN varchar(50), address Varchar(100), grp int , PRIMARY KEY (id), foreign key(grp) references grps(id));''')
    cur.execute('''create table if not exists vans (id  INT AUTO_INCREMENT, matr Varchar(50), driver varchar(50), max_places int , PRIMARY KEY (id))''')
    cur.execute('''create table if not exists vans(id  INT AUTO_INCREMENT, matricule varchar(50), max_places int , PRIMARY KEY (id))''')
    cur.execute('''create table if not exists drivers(id  INT AUTO_INCREMENT, firstName Varchar(50), LastName varchar(50), PRIMARY KEY (id))''')
    cnx.commit()

    cur.execute('create table if not exists trips(id  INT AUTO_INCREMENT, van int, driver int, datetime Varchar(50), foreign key(van) references vans(id), foreign key(driver) references drivers(id) , PRIMARY KEY (id))')

    cnx.commit()
    cur.execute('''create table if not exists trips_history(id  INT AUTO_INCREMENT,trip int, agent int, pick_time varchar(50), presence int, foreign key(trip) references trips(id), foreign key(agent) references agents(id), PRIMARY KEY (id))''')
    cnx.commit()
    cnx.close()
    print('tables created ')


preparingDB()

today = datetime.datetime.today().strftime('%Y-%m-%d')

def createPlannings():
    today = datetime.date.today()
    day = datetime.datetime.today().strftime('%A')
    print(day)
    if day.lower() == "Friday".lower():
        tomorrow = datetime.date.today() + datetime.timedelta(days=3)
    else:
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    # tomorrow = today #TODO Just for test
    doneDates = []
    for date in [today, tomorrow]:
        print(f'date ==> {date}')
        print(date)
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
        # print(data)
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
            # print(result)

            count = len(result)

            trips[h] = [i[0] for i in result]
            total += count

        print(trips)
        print(total)
        maxForVan = 18
        for time, agents in trips.items():
            vansNeeded = 0
            if agents:
                if len(agents) > maxForVan:
                    vansNeeded = 2
                else:
                    vansNeeded = 1

                if vansNeeded == 1:
                    cur.execute(
                        f''' select count(id) from trips where datetime like "{date} {time}:00:00" and van = 1''')
                    if not cur.fetchone()[0]:
                        cur.execute(
                            f'''insert into trips(van, driver, datetime) values (1, 1, "{date} {time}:00:00");''')
                        cnx.commit()
                        for agent in agents:
                            cur.execute(f'''select id from trips where datetime like "{date} {time}:00:00"''')
                            cur.execute(
                                f'''insert into trips_history (trip, agent, presence) values ({int(cur.fetchone()[0])}, {agent}, 0)''')
                            cnx.commit()
                else:
                    grp1 = [i for i in agents[:len(agents) // 2]]
                    grp2 = [i for i in agents[len(agents) // 2:]]
                    cur.execute(
                        f'''select count(id) from trips where datetime like "{date} {time}:00:00" and driver = 1''')
                    if not cur.fetchone()[0]:
                        cur.execute(
                            f'''insert into trips(van, driver, datetime) values (1, 1, "{date} {time}:00:00");''')

                    cur.execute(f'''select id from trips where datetime like "{date} {time}:00:00"''')

                    trip1, trip2 = [int(i[0]) for i in cur.fetchall()]
                    for agent in grp1:
                        cur.execute(
                            f'''select count(id) from trips_history where trip = {trip1} and agent = {agent}''')
                        if not cur.fetchone()[0]:
                            cur.execute(
                                f'''insert into trips_history (trip, agent, presence) values ({trip1}, {agent}, 0)''')
                            cnx.commit()

                    cur.execute(
                        f'''select count(id) from trips where datetime like "{date} {time}:00:00" and driver = 1''')
                    if not cur.fetchone()[0]:
                        cur.execute(
                            f'''insert into trips(van, driver, datetime) values (2, 2, "{date} {time}:00:00");''')
                    cnx.commit()
                    for agent in grp2:
                        cur.execute(
                            f'''select count(id) from trips_history where trip = {trip2} and agent = {agent}''')
                        if not cur.fetchone()[0]:
                            cur.execute(
                                f'''insert into trips_history (trip, agent, presence) values ({trip2}, {agent}, 0)''')
                            cnx.commit()
        doneDates.append(f'{date}')
    cnx.close()

    notif(title="Saccom IT Departement : ", msg=f'{len(doneDates)} Plannings has been created : {doneDates} ')


class Splash(QtWidgets.QDialog):
    def __init__(self):
        super(Splash, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/splash.ui"), self)


        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowTitle('welcome back')
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        creatingPlanningThread = threading.Thread(target=createPlannings)
        creatingPlanningThread.start()
        self.prog()



    def isConnected(self):
        conn = con()
        #todo prepaire the error interface
        if not conn:
            print('can\'t connect to the database ...')
            exit()
        conn.close()
        return True




    def prog(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)

    def timerEvent(self, event):
        if self.step >= 100 :
            self.timer.stop()

            self.logi = LogIn()
            self.logi.show()
            self.close()
            return
        self.step += 4
        self.progressBar.setValue(self.step)


class LogIn(QtWidgets.QWidget):
    def __init__(self):
        super(LogIn, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/logIn.ui"), self)

        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.cnx.setEnabled(False)


        # palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QImage("img/pack.png")))
        # self.setPalette(palette)
        self.label.setPixmap(QtGui.QPixmap('src/img/login.png'))
        self.label.setScaledContents(True)
        self.setWindowTitle('Transporting Planning ')

        self.username_in.setPlaceholderText('User Name')
        self.passwrd_in.setPlaceholderText('Password')


        self.username_in.textChanged.connect(self.typing)
        self.passwrd_in.textChanged.connect(self.typing1)
        self.passwrd_in.returnPressed.connect(self.login)
        self.username_in.returnPressed.connect(self.login)
        self.cnx.clicked.connect(self.login)





    def typing(self):
        if len(self.username_in.text()) > 2:
            self.username_in.setStyleSheet('border : 2px solid white')
        else:
            self.username_in.setStyleSheet('border : 2px solid red')

        if len(self.username_in.text()) > 2 and len(self.passwrd_in.text()) > 2:
            self.cnx.setEnabled(True)
        else:
            self.cnx.setEnabled(False)



    def typing1(self):
        if len(self.passwrd_in.text()) > 2:
            self.passwrd_in.setStyleSheet('border : 2px solid white')
            self.cnx.setEnabled(True)
        else:
            self.passwrd_in.setStyleSheet('border : 2px solid red')
            self.cnx.setEnabled(False)

        if len(self.username_in.text()) > 2 and len(self.passwrd_in.text()) > 2:
            self.cnx.setEnabled(True)
        else:
            self.cnx.setEnabled(False)


    def login(self):
        username = self.username_in.text()
        passwrd = self.passwrd_in.text()

        print(f'UserName : {username}\nPassword : {passwrd}')
        conn = con()
        cur = conn.cursor()
        cur.execute(f'''SELECT role FROM users Where username like "{username}" and pass like "{passwrd}";''')
        role = cur.fetchone()
        try:
            if role is not None:
                self.main = Main(role=int(role[0]))
                self.main.show()
                self.close()
            else:
                self.passwrd_in.setStyleSheet('border : 2px solid red')
                self.username_in.setStyleSheet('border : 2px solid red')
                self.passwrd_in.clear()
                # python -m pip install plyer
                from plyer import notification
                notif(self, title='Transport Planning ', msg='The Username Or The Passsword are wrong')

        except Exception as e:
            print(e)

        conn.close()


class Main(QtWidgets.QWidget):
    def __init__(self, role):
        super(Main, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/main.ui"), self)
        self.role = role
        if self.role == 0:
            print('The Admin')

        # self.emps.clicked.connect(self.openAgentsUI)
        self.emps.installEventFilter(self)
        self.emps_icon.setPixmap(QtGui.QPixmap('src/img/emps.png'))

        self.vans_icon.installEventFilter(self)
        self.vans_icon.setPixmap(QtGui.QPixmap('src/img/vans.png'))

        self.comps_icon.installEventFilter(self)
        self.comps_icon.setPixmap(QtGui.QPixmap('src/img/comps.png'))

        self.plan_icon.installEventFilter(self)
        self.plan_icon.setPixmap(QtGui.QPixmap('src/img/planning.png'))
        # self.emps.setFixedSize()


        self.emps_icon.setScaledContents(True)
        self.planning.installEventFilter(self)
        head = ['Trip ID','Van Matricule','Driver name ','Trip time','Agents numbers']
        self.trips.setHeaderLabels(head)
        self.getCurrentPlanning()
        self.trips.itemSelectionChanged.connect(lambda : print(f'Select ==> {self.trips.selectedItems()[0].text(0)}'))
        self.trips.itemDoubleClicked.connect(self.trip_View)
        self.comps.installEventFilter(self)
        self.vans.installEventFilter(self)
        STYLESHEET = '''QAbstractItemView QHeaderView {
    show-decoration-selected: 0;
    background: transparent;
}
QAbstractItemView::section QHeaderView::section {
    show-decoration-selected: 0;
    background: transparent;
}
            '''
        self.trips.setStyleSheet(STYLESHEET)

        # self.getTrips()
        #TODO

    def eventFilter(self, s, e):
        if e.type() == QtCore.QEvent.MouseButtonPress:
            if s is self.emps:
                self.openAgentsUI()

            if s is self.vans:
                self.openVans()

            if s is self.comps:
                self.openComps()

            if s is self.planning:
                self.openTrips()
            # if s is self.emps:
            #     pass
            # if s is self.emps:
            #     pass
            # if s is self.emps:
            #     pass
            # if s is self.emps:
            #     pass
            # if s is self.emps:
            #     pass
            # if s is self.emps:
            #     pass
            # if s is self.emps:
            #     pass

        return super(Main, self).eventFilter(s, e)

    def openVans(self):
        self.vansUI = Vans(role=self.role)
        self.vansUI.show()
        self.close()

    def openComps(self):

        self.compUI = Compaigns(role=self.role)
        self.compUI.show()
        self.close()

    def trip_View(self):

        data = [i.text(0) for i in self.trips.selectedItems()]
        print(f'data ==> {data}')
        cnx = con()
        cur = cnx.cursor()
        cur.execute(f'select datetime from trips where id = {int(data[0])} ;')
        if int(strftime("%H", gmtime())) >= int(str(cur.fetchone()[0]).split(' ')[1].split(':')[0]) :

            self.TV = Trip_View(role=self.role, id=data, desibleedit=True)
            notif(self, title="Error", msg='You can\'t Modify this Trip .')
        else:
            self.TV = Trip_View(role=self.role, id=data)
        self.TV.show()
        self.close()




    def openTrips(self):
        self.tri = Trips(role=self.role)
        self.tri.show()
        self.close()

    def openAgentsUI(self):
        self.agents = Agents(self.role)
        self.agents.show()
        self.close()


    def getCurrentPlanning(self):
        self.trips.clear()
        currentHour = strftime("%H", gmtime())
        cnx = con()
        cur = cnx.cursor()

        cur.execute(f'''select t.id, v.matr, CONCAT(d.firstName, ' ', d.LastName) as driverName , t.datetime, (select count(id) from trips_history where trip = t.id) as Agent_numbers
                    from trips t inner join vans v on t.van = v.id inner join drivers d on t.driver = d.id where date(t.datetime) >= "{today} 00:00:00" order by t.datetime;''')
        data = cur.fetchall()
        ind = 0
        for i in data:

            item = QtWidgets.QTreeWidgetItem([str(u) for u in i])
            cur.execute(f'''select a.id, CONCAT(a.firstName, " ", a.LastName) as agentName, th.pick_time, th.presence, g.name  from trips t inner join trips_history th on th.trip = t.id inner join agents a on th.agent = a.id inner join grps g on a.grp = g.id where t.id = {i[0]};''')
            agentsForTrip = [i for i in cur.fetchall()]
            if agentsForTrip:
                ch1 = QtWidgets.QTreeWidgetItem([f'All The Agents  : {len(agentsForTrip)}'])
                for agent in agentsForTrip:
                    rr = QtWidgets.QTreeWidgetItem([str(i) for i in agent])
                    ch1.addChild(rr)
                item.addChild(ch1)
            # if f'{datetime.date.today()}' in  i[3] :
            #     print(self.trips.topLevelItem(ind))

            self.trips.addTopLevelItem(item)
            ind += 1
        cnx.close()

class Trip_View(QtWidgets.QWidget):
    def __init__(self, role, id, desibleedit = False):
        super(Trip_View, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/tripView.ui"), self)
        self.role = role
        if self.role == 0:
            print('The Admin')
        # print(data)
        self.id_ = id[0]
        cnx = con()
        cur = cnx.cursor()
        cur.execute(f'''select v.matr, t.datetime, concat(d.firstName, " ", d.LastName) as driverName from vans v inner join trips t on t.van = v.id inner join drivers d on t.driver = d.id where t.id = {int(self.id_)}''')

        self.trip_id.setText(self.id_)

        dt = cur.fetchone()
        self.van_matr.setText(dt[0])
        self.trip_time.setText(dt[1])
        self.driver_name.setText(dt[2])
        self.rmv.clicked.connect(self.removeAgent)

        self.tableWidget.itemSelectionChanged.connect(self.rowSelected)
        self.agnts.currentIndexChanged.connect(lambda : self.add.setEnabled(True) if self.agnts.currentIndex() != 0 else self.add.setEnabled(False))

        cnx.close()

        self.refreshTable()
        self.add.clicked.connect(self.add_agent)
        if desibleedit:
            self.agnts.setEnabled(False)
            self.tableWidget.setEnabled(False)


    def add_agent(self):
        cnx = con()
        cur = cnx.cursor()
        print(str(self.agnts.currentText()).split('-'))
        fname, lname = str(self.agnts.currentText()).split('-')
        print(f'First name ==> {fname}\nLast Name ==> {lname}')
        cur.execute(f'insert into trips_history(trip, agent, presence) values({int(self.trip_id.text())}, (select id from agents where firstName like "{fname}" and LastName like "{lname}"), 0) ')
        cnx.commit()
        cnx.close()
        self.refreshTable()

    def removeAgent(self):
        if items := [i.text() for i in self.tableWidget.selectedItems()]:
            print(items)
            reply = QtWidgets.QMessageBox.question(self, 'Alert !!', 'Are you sure you want to remove ?',
                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                print('removing')
                cnx = con()
                cur = cnx.cursor()
                cur.execute(f'delete from trips_history where trip = {int(self.trip_id.text())} and agent = {int(items[0])}')
                cnx.commit()
                cnx.close()
                self.refreshTable()



    def refreshTable(self):

        cnx = con()
        cur = cnx.cursor()
        cur.execute(f'''select a.id, concat(a.firstName, " ", a.LastName) as fullName, g.name, g.shift, a.address 
                                    from trips_history th inner join agents a on th.agent = a.id 
                                    inner join grps g on a.grp = g.id where th.trip = {int(self.id_)};''')
        data = [[c for c in r] for r in cur.fetchall()]
        cur.execute(f'select max_places from vans where matr like "{self.van_matr.text()}"')
        maxP = int(cur.fetchone()[0])

        if agents := data:
            if len(agents) >= maxP:
                self.agnts.setEnabled(False)
            [self.tableWidget.removeRow(0) for _ in range(self.tableWidget.rowCount())]

            self.tableWidget.setRowCount(len(agents))
            self.tableWidget.setColumnCount(len(agents[0]))
            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
            self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
            self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)



            head = [i for i in 'Agent ID-Full Name-Group-Shift-Address'.split('-')]
            self.tableWidget.setHorizontalHeaderLabels(head)
            print(agents)
            for r in range(len(agents)):
                for c in range(len(agents[r])):
                    self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(str(agents[r][c])))

        cur.execute(f'select agent from trips_history where trip = {self.trip_id.text()}')
        # print(f'current agents == > {list(set([i[0] for i in cur.fetchall()]))}')
        agents = []
        existsAgents = tuple(set([i[0] for i in cur.fetchall()]))
        print(f'select concat(firstName, "-", LastName) as fullName from agents where id not in {existsAgents};')
        cur.execute(
            f'select concat(firstName, "-", LastName) as fullName from agents where id not in {existsAgents};' if len(existsAgents) > 1 else f'select concat(firstName, "-", LastName) as fullName from agents where id != {existsAgents[0]};')

        # print(cur.fetchall())
        self.agnts.clear()
        self.agnts.addItems(['Choose Agent ...'])
        self.agnts.addItems([i[0] for i in cur.fetchall()])
        self.agnts.setCurrentIndex(0)

        cnx.close()
    def rowSelected(self):
        items = [i.text() for i in self.tableWidget.selectedItems()]
        print(items)
        if items:
            self.rmv.setEnabled(True)
        else:
            self.rmv.setEnabled(False)

    def closeEvent(self, event):
        self.main = Main(self.role)
        self.main.show()
        self.close()


class Trips(QtWidgets.QWidget):
    def __init__(self, role):
        super(Trips, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/trips.ui"), self)
        self.role = role
        self.getTrips()
        # self.create_btn.clicked.connect(self.createTrips)



    def closeEvent(self, event):
        self.main = Main(self.role)
        self.main.show()
        self.close()

    # def createTrips(self):
    #     today = datetime.date.today()
    #     day = datetime.datetime.today().strftime('%A')
    #     print(day)
    #     if day.lower() == "Friday".lower():
    #         tomorrow = datetime.date.today() + datetime.timedelta(days=3)
    #     else:
    #         tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    #
    #     # tomorrow = today #TODO Just for test
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
    #                 cur.execute(
    #                     f''' select count(id) from trips where datetime like "{tomorrow} {time}:00:00" and van = 1''')
    #                 if not cur.fetchone()[0]:
    #                     cur.execute(
    #                         f'''insert into trips(van, driver, datetime) values (1, 1, "{tomorrow} {time}:00:00");''')
    #                     cnx.commit()
    #                     for agent in agents:
    #                         cur.execute(f'''select id from trips where datetime like "{tomorrow} {time}:00:00"''')
    #                         cur.execute(
    #                             f'''insert into trips_history (trip, agent, presence) values ({int(cur.fetchone()[0])}, {agent}, 0)''')
    #                         cnx.commit()
    #             else:
    #                 grp1 = [i for i in agents[:len(agents) // 2]]
    #                 grp2 = [i for i in agents[len(agents) // 2:]]
    #                 cur.execute(
    #                     f'''select count(id) from trips where datetime like "{tomorrow} {time}:00:00" and driver = 1''')
    #                 if not cur.fetchone()[0]:
    #                     cur.execute(
    #                         f'''insert into trips(van, driver, datetime) values (1, 1, "{tomorrow} {time}:00:00");''')
    #
    #                 cur.execute(f'''select id from trips where datetime like "{tomorrow} {time}:00:00"''')
    #
    #                 trip1, trip2 = [int(i[0]) for i in cur.fetchall()]
    #                 for agent in grp1:
    #                     cur.execute(f'''select count(id) from trips_history where trip = {trip1} and agent = {agent}''')
    #                     if not cur.fetchone()[0]:
    #                         cur.execute(
    #                             f'''insert into trips_history (trip, agent, presence) values ({trip1}, {agent}, 0)''')
    #                         cnx.commit()
    #
    #                 cur.execute(
    #                     f'''select count(id) from trips where datetime like "{tomorrow} {time}:00:00" and driver = 1''')
    #                 if not cur.fetchone()[0]:
    #                     cur.execute(
    #                         f'''insert into trips(van, driver, datetime) values (2, 2, "{tomorrow} {time}:00:00");''')
    #                 cnx.commit()
    #                 for agent in grp2:
    #                     cur.execute(f'''select count(id) from trips_history where trip = {trip2} and agent = {agent}''')
    #                     if not cur.fetchone()[0]:
    #                         cur.execute(
    #                             f'''insert into trips_history (trip, agent, presence) values ({trip2}, {agent}, 0)''')
    #                         cnx.commit()
    #     cnx.close()
    #     self.getTrips()
    #


    def getTrips(self):
            self.tableWidget.setRowCount(0)
            cnx = con()
            cur = cnx.cursor()
            cur.execute('''select t.id, v.matr, d.firstName, d.LastName, t.datetime, (select count(id) from trips_history where trip = t.id) as Agent_numbers
                    from trips t inner join vans v on t.van = v.id inner join drivers d on t.driver = d.id ;''')
            dt = cur.fetchall()

            data = []

            for r in dt:
                data.append([r[0], r[1], f'{r[2]} {r[3]}', r[4], r[5]])
            head = ['Trip-ID ', 'van Matrecule', 'Driver Name', 'Time', 'Agents Numbers']

            print(data)
            self.tableWidget.setColumnCount(len(data[0]))
            self.tableWidget.setRowCount(len(data))
            # self.tableWidget.horizontalHeader().setSectionResizeMode(head.index(head[-1]), QHeaderView.Stretch)
            # self.tableWidget.resizeColumnsToContents()
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

            self.tableWidget.setHorizontalHeaderLabels(head)
            for r in range(len(data)):
                for c in range(len(data[0])):
                    self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(str(data[r][c])))

            cnx.close()


class Agents(QtWidgets.QWidget):
    def __init__(self, role):
        super(Agents, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/Agents.ui"), self)
        self.add_btn.clicked.connect(self.add)

        self.role = role
        if self.role == 0:
            print("The Admin")

        self.refreshTable()

        self.back = True

        self.edit_btn.clicked.connect(self.edit)

        self.groups.currentIndexChanged.connect(self.refreshTable)

        self.tableWidget.itemSelectionChanged.connect(self.tableSelectRowChanged)
        self.search.textChanged.connect(self.searching)

    def searching(self):
        self.refreshTable(key= self.search.text())

    def refreshTable(self, key = None):

        self.tableWidget.setRowCount(0)

        cnx = con()
        cur = cnx.cursor()
        if self.groups.currentIndex() == 0:
            self.search.setEnabled(True)
            self.search.setStyleSheet('border : 1px solid blue')
            if key:
                cur.execute(
                    f'select a.id, a.firstName, a.LastName, a.CIN, a.address, g.name, g.shift from agents a inner join grps g on a.grp = g.id where a.firstName like "%{key}%" or a.LastName like "%{key}%" or a.CIN like "%{key}%" or a.address like "%{key}%" or g.name like "%{key}%";')
            else:
                cur.execute(
                f'select a.id, a.firstName, a.LastName, a.CIN, a.address, g.name, g.shift from agents a inner join grps g on a.grp = g.id;')
        else:
            self.search.setEnabled(False)
            self.search.setStyleSheet('border : 2px solid red')
            cur.execute(f'select id from grps where name = "{self.groups.currentText()}"')
            cur.execute(
                f'select a.id, a.firstName, a.LastName, a.CIN, a.address, g.name, g.shift from agents a inner join grps g on a.grp = g.id  where a.grp = {cur.fetchone()[0]};')


        agents = []
        data = cur.fetchall()

        if data:


            for r in data:
                agents.append([r[0], f'{r[1]} {r[2]}', r[3], r[4], r[5], r[6]])
            head = ['Agent ID ', 'Full Name', 'CIN', 'Adress', 'Group', 'Shift']
            print(agents)
            self.tableWidget.setColumnCount(len(agents[0]))
            self.tableWidget.setRowCount(len(agents))
            # self.tableWidget.horizontalHeader().setSectionResizeMode(head.index(head[-1]), QHeaderView.Stretch)
            # self.tableWidget.resizeColumnsToContents()

            self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
            self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
            self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
            self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
            self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
            self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)

            self.tableWidget.setHorizontalHeaderLabels(head)
            for r in range(len(agents)):
                for c in range(len(agents[0])):
                    self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(str(agents[r][c])))

            cur.execute('select name from grps')
            grps_names = [i[0] for i in cur.fetchall()]
            print(grps_names)
            self.groups.addItems(grps_names)
        else:
            print('no data found ')
        cnx.close()


    def tableSelectRowChanged(self):
        items = [i.text() for i in self.tableWidget.selectedItems()]
        print(items)
        if items:
            self.edit_btn.setEnabled(True)
        else:
            self.edit_btn.setEnabled(False)


    def edit(self):

        self.back = False
        self.eA = AddAgent(self.role, do='edit', data=[i.text() for i in self.tableWidget.selectedItems()])
        self.eA.show()
        self.close()


    def closeEvent(self, event):
        if self.back:
            self.main = Main(self.role)
            self.main.show()
            self.close()

    def add(self):
        self.back = False
        self.addAgent = AddAgent(self.role)
        self.close()
        self.addAgent.show()


class Vans(QtWidgets.QWidget):
    def __init__(self, role):
        super(Vans, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/vans.ui"), self)
        self.add_btn.clicked.connect(self.add)

        self.role = role
        if self.role == 0:
            print("The Admin")

        self.refreshTable()

        self.back = True

        self.edit_btn.clicked.connect(self.edit)


        self.tableWidget.itemSelectionChanged.connect(self.tableSelectRowChanged)

    def searching(self):
        self.refreshTable(key= self.search.text())

    def refreshTable(self, key = None):

        self.tableWidget.setRowCount(0)

        cnx = con()
        cur = cnx.cursor()
        columns = 'v.id, v.matr, v.max_places, concat(d.firstName, " ", LastName) as fullName '

        cur.execute(
            f'select {columns} from vans v inner join drivers d on v.driver = d.id ;')


        data = cur.fetchall()

        if data:
            vans = [[c for c in r] for r in data]
            head = ['Vehicle ID ', 'Matricule', 'Max Places', 'Driver\'s name']
            print(vans)
            self.tableWidget.setColumnCount(len(vans[0]))
            self.tableWidget.setRowCount(len(vans))
            # self.tableWidget.horizontalHeader().setSectionResizeMode(head.index(head[-1]), QHeaderView.Stretch)
            # self.tableWidget.resizeColumnsToContents()
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

            self.tableWidget.setHorizontalHeaderLabels(head)
            for r in range(len(vans)):
                for c in range(len(vans[0])):
                    self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(str(vans[r][c])))


        else:
            print('no data found ')
        cnx.close()


    def tableSelectRowChanged(self):
        items = [i.text() for i in self.tableWidget.selectedItems()]
        print(items)
        if items:
            self.edit_btn.setEnabled(True)
        else:
            self.edit_btn.setEnabled(False)



    def closeEvent(self, event):
        if self.back:
            self.main = Main(self.role)
            self.main.show()
            self.close()

    def add(self):
        self.back = False
        self.addVans = AddVan(self.role)
        self.close()
        self.addVans.show()

    def edit(self):

        self.back = False
        self.eV = AddVan(self.role, do='edit', data=[i.text() for i in self.tableWidget.selectedItems()])
        self.eV.show()
        self.close()


class AddVan(QtWidgets.QWidget):
    def __init__(self, role, do = 'save', data = None):
        super(AddVan, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/addVan.ui"), self)
        self.save_btn.clicked.connect(self.save)
        self.role = role
        if self.role == 0:
            print('The Admin')
        self.action = do
        cnx = con()
        cur = cnx.cursor()
        cur.execute('select concat(firstName, " ", LastName) as fullName from drivers;')
        drivers_names = [i[0] for i in cur.fetchall()]
        print(drivers_names)
        self.drivers.addItems(drivers_names)
        self.data = data
        if self.data:
            self.matr.setText(str(self.data[1]))
            self.max_places.setText(str(self.data[2]))
            self.drivers.setCurrentIndex(drivers_names.index(self.data[3]))



        cnx.close()

    def closeEvent(self, event):
        self.VansPage = Vans(self.role)
        self.VansPage.show()
        self.close()



    def save(self):
        if len(self.matr.text()) > 3 and len(self.max_places.text()) > 0:
            cnx = con()
            cur = cnx.cursor()
            cur.execute(f'select id from drivers where firstName like "{str(self.drivers.currentText()).split(" ")[0]}" and LastName like "{str(self.drivers.currentText()).split(" ")[-1]}"')
            drvr = int(cur.fetchone()[0])

            if self.action == 'save':
                cur.execute(
                    f'select count(id) from vans where matr like "{self.matr.text()}";')
                if cur.fetchone()[0]:
                    print('this Van alredy exists ')
                    self.matr.setStyleSheet('border : 2px solid red')
                    notif(self, title='Transport Planning ', msg='This Vehicle already exists in the Database ')
                else:
                    cur.execute(f'insert into vans (matr, max_places, driver) value ("{self.matr.text()}", {int(self.max_places.text())}, {drvr});')
                    cnx.commit()
            elif self.action == 'edit':
                    cur.execute(f'''
                            update vans set matr = "{self.matr.text()}",
                                            max_places = {int(self.max_places.text())},
                                            
                                            driver = {drvr}
                                            where id = {int(self.data[0])}
                        ''')
                    cnx.commit()
                    # self.agents = Agents(self.role)
                    # self.agents.show()
                    # self.close()
            self.matr.clear()
            self.max_places.clear()
            self.drivers.setCurrentIndex(0)

            cnx.close()

        else:
            notif(self, title="Error ", msg='you have to write all the infos')


class Compaigns(QtWidgets.QWidget):
    def __init__(self, role):
        super(Compaigns, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/cmps.ui"), self)
        self.add_btn.clicked.connect(self.add)

        self.role = role
        if self.role == 0:
            print("The Admin")

        self.refreshTable()

        self.back = True

        self.edit_btn.clicked.connect(self.edit)

        self.tableWidget.itemSelectionChanged.connect(self.tableSelectRowChanged)


    def refreshTable(self, key=None):

        self.tableWidget.setRowCount(0)

        cnx = con()
        cur = cnx.cursor()

        cur.execute(
            f'select id, name, shift  from grps ;')



        if dt := [[c for c in r] for r in cur.fetchall()]:
            data = []
            for i, r in enumerate(dt):
                row = r
                cur.execute(f'select count(id) from agents where grp = {row[0]}')
                row.append(cur.fetchone()[0])
                data.append(row)

            head = ['Compaign ID ', 'Compaign Name', 'Shift', 'Agents Number']
            print(data)
            self.tableWidget.setColumnCount(len(data[0]))
            self.tableWidget.setRowCount(len(data))
            # self.tableWidget.horizontalHeader().setSectionResizeMode(head.index(head[-1]), QHeaderView.Stretch)
            # self.tableWidget.resizeColumnsToContents()
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

            self.tableWidget.setHorizontalHeaderLabels(head)
            for r in range(len(data)):
                for c in range(len(data[0])):
                    self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(str(data[r][c])))


        else:
            print('no data found ')
        cnx.close()

    def tableSelectRowChanged(self):
        items = [i.text() for i in self.tableWidget.selectedItems()]
        print(items)
        if items:
            self.edit_btn.setEnabled(True)
        else:
            self.edit_btn.setEnabled(False)

    def closeEvent(self, event):
        if self.back:
            self.main = Main(self.role)
            self.main.show()
            self.close()

    def add(self):
        self.back = False
        self.addComp = AddComp(self.role)
        self.close()
        self.addComp.show()

    def edit(self):

        self.back = False
        self.eV = AddComp(self.role, do='edit', data=[i.text() for i in self.tableWidget.selectedItems()])
        self.eV.show()
        self.close()


class AddComp(QtWidgets.QWidget):
    def __init__(self, role, do='save', data=None):
        super(AddComp, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/addComp.ui"), self)
        self.save_btn.clicked.connect(self.save)
        self.role = role
        if self.role == 0:
            print('The Admin')
        self.action = do
        self.shiftfrom.addItems([f'0{i}:00' if i < 10 else f'{i}:00' for i in range(8, 24)])
        self.shiftto.addItems([f'0{i}:00' if i < 10 else f'{i}:00' for i in range(8, 24)])
        self.data = data
        #['Compaign ID ', 'Compaign Name', 'Shift', 'Agents Number']
        if self.data:
            self.cname.setText(str(self.data[1]))
            self.shiftfrom.setCurrentIndex([self.shiftfrom.itemText(i) for i in range(self.shiftfrom.count())].index(f'{str(self.data[2]).split("-")[0]}:00'))
            self.shiftto.setCurrentIndex([self.shiftto.itemText(i) for i in range(self.shiftto.count())].index(f'{str(self.data[2]).split("-")[1]}:00'))



    def closeEvent(self, event):
        self.CompsPage = Compaigns(self.role)
        self.CompsPage.show()
        self.close()

    def save(self):
        print(f''' name > 2 ({len(self.cname.text())}) : {len(self.cname.text()) > 2} \n
                {int(self.shiftfrom.currentText().split(':')[0])} < {int(self.shiftto.currentText().split(':')[0])} :  {int(self.shiftfrom.currentText().split(':')[0]) < int(self.shiftto.currentText().split(':')[0])} \n
                {int(self.shiftto.currentText().split(':')[0])} - {int(self.shiftfrom.currentText().split(':')[0])} == 9 ({int(self.shiftto.currentText().split(':')[0]) - int(self.shiftfrom.currentText().split(':')[0])}) :  {int(self.shiftfrom.currentText().split(':')[0]) - int(self.shiftto.currentText().split(':')[0]) == 9}''')
        if len(self.cname.text()) > 2 \
                and int(self.shiftfrom.currentText().split(':')[0]) < int(self.shiftto.currentText().split(':')[0]) \
                and int(self.shiftto.currentText().split(':')[0]) - int(self.shiftfrom.currentText().split(':')[0]) == 9:
            cnx = con()
            cur = cnx.cursor()


            if self.action == 'save':
                cur.execute(
                    f'select count(id) from grps where name like "{self.cname.text()}";')
                if cur.fetchone()[0]:
                    print('this Compaogns alredy exists ')
                    self.matr.setStyleSheet('border : 2px solid red')
                    notif(self, title='Transport Planning ', msg='This Compaign already exists in the Database ')
                else:
                    cur.execute(
                        f'insert into grps (name, shift) value ("{self.cname.text()}", "{str(self.shiftfrom.currentText()).split(":")[0]}-{str(self.shiftto.currentText()).split(":")[0]}");')
                    cnx.commit()
            elif self.action == 'edit':
                cur.execute(f'''
                            update grps set name = "{self.cname.text()}",
                                            shift = "{str(self.shiftfrom.currentText()).split(":")[0]}-{str(self.shiftto.currentText()).split(":")[0]}"
                                            where id = {int(self.data[0])}
                        ''')
                cnx.commit()
                # self.agents = Agents(self.role)
                # self.agents.show()
                # self.close()
            self.cname.clear()
            self.shiftfrom.setCurrentIndex(0)
            self.shiftto.setCurrentIndex(0)

            cnx.close()

        else:
            notif(self, title="Error ", msg='you have to write all the infos')


class AddAgent(QtWidgets.QWidget):
    def __init__(self, role, do = 'save', data = None):
        super(AddAgent, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/addAgent.ui"), self)
        self.save_btn.clicked.connect(self.save)
        self.role = role
        if self.role == 0:
            print('The Admin')
        self.action = do
        cnx = con()
        cur = cnx.cursor()
        cur.execute('select name from grps')
        grps_names = [i[0] for i in cur.fetchall()]
        print(grps_names)
        self.grps.addItems(grps_names)
        self.data = data
        if self.data:
            self.Fname.setText(str(self.data[1]).split(' ')[0])
            self.Lname.setText(str(self.data[1]).split(' ')[1])
            self.CIN.setText(self.data[2])
            self.ad.setText(self.data[3])
            self.grps.setCurrentIndex(grps_names.index(self.data[4]))



        cnx.close()

    def closeEvent(self, event):
        self.agentPage = Agents(self.role)
        self.agentPage.show()
        self.close()



    def save(self):
        if len(self.Fname.text()) > 3 and len(self.Lname.text()) > 3 and len(self.CIN.text()) > 3 and len(self.ad.text()) > 3:
            cnx = con()
            cur = cnx.cursor()
            cur.execute(f'select id from grps where name like "{self.grps.currentText()}"')
            grp = int(cur.fetchone()[0])

            if self.action == 'save':
                cur.execute(
                    f'select count(id) from agents where FirstName like "{self.Fname.text()}" and LastName like "{self.Lname.text()}"')
                if cur.fetchone()[0]:
                    print('thsi Agent alredy exists ')
                    self.Fname.setStyleSheet('border : 2px solid red')
                    self.Lname.setStyleSheet('border : 2px solid red')
                    notif(self, title='Transport Planning ', msg='This Agent already exists in the Database ')
                else:
                    cur.execute(f'insert into agents (firstName, LastName, CIN, address, grp) value ("{self.Fname.text()}", "{self.Lname.text()}", "{self.CIN.text()}", "{self.ad.text()}", {grp});')
                    cnx.commit()
            elif self.action == 'edit':
                    cur.execute(f'''
                            update agents set firstName = "{self.Fname.text()}",
                                            LastName = "{self.Lname.text()}",
                                            CIN = "{self.CIN.text()}",
                                            address = "{self.ad.text()}",
                                            grp = {grp}
                                            where id = {int(self.data[0])}
                        ''')
                    cnx.commit()
                    # self.agents = Agents(self.role)
                    # self.agents.show()
                    # self.close()
            self.Fname.clear()
            self.Lname.clear()
            self.CIN.clear()
            self.ad.clear()
            self.grps.setCurrentIndex(0)

            cnx.close()

        else:
            notif(self, title="Error ", msg='you have to write all the infos')






if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    splash_wn = Splash()
    splash_wn.show()
    sys.exit(app.exec_())