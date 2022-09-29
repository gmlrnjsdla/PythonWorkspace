import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

form_class = uic.loadUiType('../ui/UpbitCoinTrade.ui')[0]


class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('UPBIT COIN TRADE')
        self.setWindowIcon(QIcon('../icons/upbit.png'))
        self.statusBar().showMessage('UPBIT COIN TRADE VER 0.5')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())