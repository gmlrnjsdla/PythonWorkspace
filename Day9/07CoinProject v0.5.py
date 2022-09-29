import time

import requests
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *

form_class = uic.loadUiType('../ui/UpbitCoinTrade.ui')[0]

# 시그널 클래스(쓰레드)
class CoinViewThread(QThread):
    coinDataSent = pyqtSignal(float, float, float, float, float, float, float, float)

    def __init__(self):
        super().__init__()
        self.ticker = 'BTC'
        self.alive = True

    def run(self):
        while self.alive:
            url = "https://api.upbit.com/v1/ticker"
            ticker = 'KRW-BTC'
            param = {'markets': ticker}
            response = requests.get(url, params=param)
            ubbitResult = response.json()
            trade_price = ubbitResult[0]['trade_price']  # 코인의 현재가격
            acc_trade_volume_24h = ubbitResult[0]['acc_trade_volume_24h']  # 24시간 누적 거래량
            acc_trade_price_24h = ubbitResult[0]['acc_trade_price_24h']  # 24시간 누적 거래 대금
            trade_volume = ubbitResult[0]['trade_volume']  # 최근 거래량
            high_price = ubbitResult[0]['high_price']  # 고가
            low_price = ubbitResult[0]['low_price']  # 저가
            prev_closing_price = ubbitResult[0]['prev_closing_price']     # 전일 종가
            signed_change_rate = ubbitResult[0]['signed_change_rate']     # 변화율

            self.coinDataSent.emit(float(trade_price),
                                   float(acc_trade_volume_24h),
                                   float(acc_trade_price_24h),
                                   float(trade_volume),
                                   float(high_price),
                                   float(low_price),
                                   float(prev_closing_price),
                                   float(signed_change_rate))

            time.sleep(0.5)     # 서버에 요청하는 delay Time


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