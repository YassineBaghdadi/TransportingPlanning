from time import gmtime

from PyQt5 import QtWidgets, uic, QtGui, QtCore
import os, sys, datetime, pymysql

from PyQt5.QtWidgets import QHeaderView


def con():
    return pymysql.connect(host='10.73.100.101', user='VP', database='vansplanning', password='1234@@it.', port=3306)


def preparingDB():
    cnx = con()
    cur = cnx.cursor()
    cur.execute('''Create table if not exists users (id  INT AUTO_INCREMENT, firstName Varchar(50), LastName Varchar(50), username Varchar(50), pass Varchar(50), role INT , PRIMARY KEY (id));''')
    cur.execute('''create table if not exists grps (id  INT AUTO_INCREMENT, name Varchar(50), shift Varchar(20) , PRIMARY KEY (id));''')
    cnx.commit()
    cur.execute('''create table if not exists agents (id  INT AUTO_INCREMENT, firstName Varchar(50), LastName Varchar(50), CIN varchar(50), address Varchar(100), grp int , PRIMARY KEY (id), foreign key(grp) references grps(id));''')
    cnx.commit()

    cnx.close()
    print('tables created ')


# preparingDB()

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
        role = int(cur.fetchone()[0])
        if not role :#the admin
                self.main = Main()
                self.main.show()
                self.close()
                print('welcome back Admin')
        else :
                print('not Admin')
                self.main = Main()
                self.main.show()
                self.close()
        conn.close()


class Main(QtWidgets.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/main.ui"), self)

        self.emps.clicked.connect(self.openAgentsUI)



    def openAgentsUI(self):
        self.agents = Agents()
        self.agents.show()
        self.close()



class Agents(QtWidgets.QWidget):
    def __init__(self):
        super(Agents, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/Agents.ui"), self)
        self.add_btn.clicked.connect(self.add)
        cnx = con()
        cur = cnx.cursor()
        cur.execute('select a.id, a.firstName, a.LastName, a.CIN, a.address, g.name, g.shift from agents a inner join grps g on a.grp = g.id ;')
        agents = []
        data = cur.fetchall()
        for r in data:
            agents.append([r[0], f'{r[1]} {r[2]}', r[3], r[4], r[5], r[6]])

        head = ['Agent ID ', 'Full Name', 'CIN', 'Adress', 'Group', 'Shift']
        print(agents)
        self.tableWidget.setColumnCount(len(agents[0]))
        self.tableWidget.setRowCount(len(agents))
        # self.tableWidget.horizontalHeader().setSectionResizeMode(head.index(head[-1]), QHeaderView.Stretch)
        # self.tableWidget.resizeColumnsToContents()
        for i in range(self.tableWidget.columnCount()): # todo I'm here
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

        self.tableWidget.setHorizontalHeaderLabels(head)
        for r in range(len(agents)):
            for c in range(len(agents[0])):
                self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(str(agents[r][c])))


    def add(self):
        self.addAgent = AddAgent()
        self.addAgent.show()
        self.close()






class AddAgent(QtWidgets.QWidget):
    def __init__(self):
        super(AddAgent, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/addAgent.ui"), self)
        self.save_btn.clicked.connect(self.save)

    def save(self):
        self.agents = Agents()
        self.agents.show()
        self.close()



class Vans(QtWidgets.QWidget):
    def __init__(self):
        super(Vans, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/Agents.ui"), self)
        self.add_btn.clicked.connect(self.add)

    def add(self):
        self.addAgent = AddAgent()
        self.addAgent.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    splash_wn = Splash()
    splash_wn.show()
    sys.exit(app.exec_())