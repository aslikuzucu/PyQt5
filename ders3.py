import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.giris_buton = QPushButton("Giriş", self)
        self.cikis_buton = QPushButton("Çıkış", self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.giris_buton)
        vbox.addWidget(self.cikis_buton)

        self.setLayout(vbox)

        self.giris_buton.clicked.connect(self.giris)
        self.cikis_buton.clicked.connect(self.cikis)

        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Basit bir PyQt5 Arayüzü")
        self.show()

    def giris(self):
        print("Giriş yapıldı")

    def cikis(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    arayuz = Arayuz()
    sys.exit(app.exec_())
