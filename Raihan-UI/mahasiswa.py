from PyQt6 import QtWidgets, uic
import sys




class app5F(QtWidgets.QMainWindow):
    def __init__(self):
        super(app5F,self).__init__()
        uic.loadUi('mahasiswa.ui',self)

        self.btnsimpan.clicked.connect(self.testingTombol);

    def testingTombol(self):
        nama = self.editnama.text()
        npm = self.editnpm.text()
        jurusan = self.editjurusan.text()
        alamat = self.editalamat.text()
        email = self.editemail.text()
        telepon = self.edittelepon.text()


        print(f'DATA MAHASISWA')
        print(f'Nama : {nama}')
        print(f'NPM : {npm}')
        print(f'Jurusan : {jurusan}')
        print(f'Alamat : {alamat}')
        print(f'Email : {email}')
        print(f'Telepon : {telepon}')

if __name__ == '__main__':
    aplikasiku = QtWidgets.QApplication(sys.argv)
    jendela = app5F()
    jendela.show()

    sys.exit(aplikasiku.exec())