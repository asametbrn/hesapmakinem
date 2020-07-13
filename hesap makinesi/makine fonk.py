from hesapmakinesi import *

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

#------------- UYGULAMA OLUŞTUR----------------
uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

sys.exit(uygulama.exec_())
#------------- FONKSİYONLAR --------------

class butonlar (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn1.clicked.connect(self.btn1_clicked_slot)

        def btn1_clicked_slot(self):

            print("basıldı")

















