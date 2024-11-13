from PyQt6 import QtWidgets, uic
import sys




class app5F(QtWidgets.QMainWindow):
    def __init__(self):
        super(app5F,self).__init__()
        uic.loadUi('kelas.ui',self)

        self.btnsimpan.clicked.connect(self.testingTombol);

    def testingTombol(self):
        idkelas = self.editidkelas.text()
        kodekelas = self.editkodekelas.text()
        idmatkul = self.editmatakuliah.text()
        iddosen = self.editiddosen.text()
        ruangan = self.editruangan.text()


        print(f'KELAS')
        print(f'ID Kelas : {idkelas}')
        print(f'Kode Kelas : {kodekelas}')
        print(f'ID Mata Kuliah : {idmatkul}')
        print(f'ID Dosen : {iddosen}')
        print(f'Ruangan : {ruangan}')

if __name__ == '__main__':
    aplikasiku = QtWidgets.QApplication(sys.argv)
    jendela = app5F()
    jendela.show()

    sys.exit(aplikasiku.exec())