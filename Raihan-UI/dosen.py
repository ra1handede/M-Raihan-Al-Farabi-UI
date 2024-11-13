from PyQt6 import QtWidgets, uic
import sys




class app5F(QtWidgets.QMainWindow):
    def __init__(self):
        super(app5F,self).__init__()
        uic.loadUi('dosen.ui',self)

        self.btnsimpan.clicked.connect(self.testingTombol);

    def testingTombol(self):
        iddosen = self.editiddosen.text()
        nip = self.editnip.text()
        namadosen = self.editnamadosen.text()
        email = self.editemail.text()
        telepon = self.edittelepon.text()
        alamat = self.editalamat.text()


        print(f'DATA DOSEN')
        print(f'ID Dosen : {iddosen}')
        print(f'NIP : {nip}')
        print(f'Nama Dosen : {namadosen}')
        print(f'Email : {email}')
        print(f'Telepon : {telepon}')
        print(f'Alamat : {alamat}')

if __name__ == '__main__':
    aplikasiku = QtWidgets.QApplication(sys.argv)
    jendela = app5F()
    jendela.show()

    sys.exit(aplikasiku.exec())