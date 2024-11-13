from PyQt6 import QtWidgets, uic
import sys




class app5F(QtWidgets.QMainWindow):
    def __init__(self):
        super(app5F,self).__init__()
        uic.loadUi('matakuliah.ui',self)

        self.btnsimpan.clicked.connect(self.testingTombol);

    def testingTombol(self):
        idmatkul = self.editid.text()
        kodematkul = self.editkode.text()
        namamatkul = self.editnamamatakuliah.text()
        semester = self.editsemester.text()
        sks = self.editsks.text()


        print(f'DATA MATA KULIAH')
        print(f'ID Mata Kuliah : {idmatkul}')
        print(f'Kode Mata Kuliah : {kodematkul}')
        print(f'Nama Mata Kuliah : {namamatkul}')
        print(f'Semester : {semester}')
        print(f'SKS : {sks}')

if __name__ == '__main__':
    aplikasiku = QtWidgets.QApplication(sys.argv)
    jendela = app5F()
    jendela.show()

    sys.exit(aplikasiku.exec())