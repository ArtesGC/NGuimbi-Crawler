import re
from sys import argv

from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *

theme = open('themes/gcryptermix.qss').read().strip()


class GCr:
    def __init__(self):
        self.gc = QApplication(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setWindowTitle('NGuimbi-Crawler')
        self.ferramentas.setFixedSize(QSize(1350, 630))
        self.ferramentas.setStyleSheet(theme)

        barraFerramentas = QToolBar(self.ferramentas)
        prevBtn = barraFerramentas.addAction(QIcon('img/icons/previous.png'), 'Voltar')
        barraFerramentas.addSeparator()

        homeBtn = barraFerramentas.addAction(QIcon('img/icons/homepage.png'), 'Pagina Inicial')
        barraFerramentas.addSeparator()

        atualizar = barraFerramentas.addAction(QIcon('img/icons/sync.png'), 'Atualizar')
        barraFerramentas.addSeparator()

        self.search = QLineEdit()
        self.search.setFixedWidth(950)
        self.search.setPlaceholderText('Digite aqui o  endereço do website..')
        self.search.returnPressed.connect(self.searchWeb)
        searchBox = barraFerramentas.addWidget(self.search)
        barraFerramentas.addSeparator()

        searchBtn = barraFerramentas.addAction(QIcon('img/icons/web.png'), 'Navegar')
        searchBtn.triggered.connect(self.searchWeb)
        barraFerramentas.addSeparator()

        novaba = barraFerramentas.addAction(QIcon('img/icons/newpage.png'), 'Nova Aba')
        novaba.triggered.connect(self.searchWeb)
        barraFerramentas.addSeparator()

        favoritos = barraFerramentas.addAction(QIcon('img/icons/favorite.png'), 'Favoritos')
        barraFerramentas.addSeparator()

        downloads = barraFerramentas.addAction(QIcon('img/icons/download.png'), 'Downloads')
        barraFerramentas.addSeparator()

        historico = barraFerramentas.addAction(QIcon('img/icons/history.png'), 'Historico')
        barraFerramentas.addSeparator()

        definicao = barraFerramentas.addAction(QIcon('img/icons/settings.png'), 'Definicoes')

        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 50, 1350, 600)
        self.tab.setDocumentMode(True)
        self.tab.setTabsClosable(True)
        self.tab.setTabBarAutoHide(True)

        self.pagina = QWebEnginePage()
        self.historico = QWebEngineHistory()
        self.definicao = QWebEngineSettings()

        self.novaJanela()

    def novaJanela(self, _url='https://google.com/'):
        janela1 = QWebEngineView()
        janela1.load(QUrl(_url))

        self.tab.addTab(janela1, f'Aba [{self.tab.currentIndex()}]')
        self.tab.setCurrentWidget(janela1)

    def searchWeb(self):
        url = re.compile('[a-z].[a-z]{2,3}')
        if 'https://' in self.search.text():
            request = self.search.text()
            self.novaJanela(_url=request)
        elif url.match(self.search.text()):
            request = 'https://' + self.search.text()
            self.novaJanela(_url=request)
        else:
            self.novaJanela()

    def janelaDefinicoes(self):
        pass

    def janelaHistorico(self):
        pass


if __name__ == '__main__':
    app = GCr()
    app.ferramentas.show()
    app.gc.exec_()
