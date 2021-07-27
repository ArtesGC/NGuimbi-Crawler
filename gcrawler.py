from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from sys import argv, exit


class GCr:
    def __init__(self):
        self.gc = QApplication(argv)
        self.ferramentas = QWidgets()

        barraFerramentas = QToolBar(self.ferramentas)
        prevBtn = barraFerramentas.addAction(QIcon('img/icons/previous.png'))
        homeBtn = barraFerramentas.addAction(QIcon('img/icons/'))

        self.tab = QTabWidget(self.ferramentas)
        self.tab.setTabBarAutoHide(True)
        self.tab.setDocumentMode(True)
        self.tab.setTabsClosable(True)

        self.janelaPrincipal()

    def janelaPrincipal(self):
        janela1 = QWidget()

