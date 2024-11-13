from PyQt6 import QtWidgets, uic
import sys

class app5F(QtWidgets.QMainWindow):
    def __init__(self):
        super(app5F,self).__init__()
        uic.loadUi('doktor.ui',self)

        self.btnsimpan.clicked.connect(self.testingTombol);

    def testingTombol(self):
        namadoktor = self.editnamadoktor.text()
        gelar = self.editgelar.text()
        nip = self.editnip.text()
        spesialis = self.editspesialis.text()


        print(f'DATA DOKTOR')
        print(f'Nama Doktor : {namadoktor}')
        print(f'Gelar : {gelar}')
        print(f'NIP : {nip}')
        print(f'Spesialis : {spesialis}')

if __name__ == '__main__':
    aplikasiku = QtWidgets.QApplication(sys.argv)
    jendela = app5F()
    jendela.show()

    sys.exit(aplikasiku.exec())