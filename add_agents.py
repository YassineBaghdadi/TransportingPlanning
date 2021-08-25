import pymysql
from PyQt5 import QtWidgets, uic
import os, sys

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


class AddAgent(QtWidgets.QWidget):
    def __init__(self):
        super(AddAgent, self).__init__()
        QtWidgets.QWidget.__init__(self)
        uic.loadUi(os.path.join(os.path.dirname(__file__), "ui/addAgent.ui"), self)
        self.save_btn.clicked.connect(self.save)

        cnx = con()
        cur = cnx.cursor()
        cur.execute('select name from grps')
        grps_names = [i[0] for i in cur.fetchall()]
        print(grps_names)
        self.grps.addItems(grps_names)

        cnx.close()



    def save(self):
        if len(self.Fname.text()) > 3 and len(self.Lname.text()) > 3 and len(self.CIN.text()) > 3 and len(self.ad.text()) > 3:
            cnx = con()
            cur = cnx.cursor()
            cur.execute(f'select id from grps where name like "{self.grps.currentText()}"')
            grp = int(cur.fetchone()[0])

            cur.execute(
                f'select count(id) from agents where FirstName like "{self.Fname.text()}" and LastName like "{self.Lname.text()}"')
            if cur.fetchone()[0]:
                print('thsi Agent alredy exists ')
                self.Fname.setStyleSheet('border : 2px solid red')
                self.Lname.setStyleSheet('border : 2px solid red')
                notif(self, title='Transport Planning ', msg='This Agent already exists in the Database ')
            else:
                cur.execute(
                    f'insert into agents (firstName, LastName, CIN, address, grp) value ("{self.Fname.text()}", "{self.Lname.text()}", "{self.CIN.text()}", "{self.ad.text()}", {grp});')
                cnx.commit()

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
    splash_wn = AddAgent()
    splash_wn.show()
    sys.exit(app.exec_())