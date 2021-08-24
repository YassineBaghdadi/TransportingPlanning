from time import gmtime, strftime

from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os, sys, datetime, pymysql

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

class Splash(QtWidgets.QDialog):
    def __init__(self):
        super(Splash, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/splash.ui"), self)


        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowTitle('welcome back')
        self.timer = QtCore.QBasicTimer()
        self.step = 0

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

        self.emps.clicked.connect(self.openAgentsUI)
        self.planning.clicked.connect(self.openTrips)


    def openTrips(self):
        self.tri = Trips(role=self.role)
        self.tri.show()
        self.close()

    def openAgentsUI(self):
        self.agents = Agents(self.role)
        self.agents.show()
        self.close()

    def openVans(self):

        self.vans = Vans(self.role)
        self.vans.show()
        self.close()

    def getCurrentPlanning(self):
        currentHour = strftime("%H", gmtime())
        cnx = con()
        cur = cnx.cursor()
        cur.execute('''select name, shift from grps''')
        data = cur.fetchall()

        # for


class Trips(QtWidgets.QWidget):
    def __init__(self, role):
        super(Trips, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/trips.ui"), self)
        self.role = role
        self.getTrips()


    def closeEvent(self, event):
        self.main = Main(self.role)
        self.main.show()
        self.close()

    def createTrips(self):
        cnx = con()
        cur = cnx.cursor()
        curses


    def getTrips(self):
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
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

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



class Vans(QtWidgets.QWidget):
    def __init__(self, role):
        super(Vans, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/Agents.ui"), self)
        self.add_btn.clicked.connect(self.add)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    splash_wn = Splash()
    splash_wn.show()
    sys.exit(app.exec_())