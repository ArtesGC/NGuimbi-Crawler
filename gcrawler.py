import re

from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from sys import argv, exit


class GCr:
    def __init__(self):
        self.gc = QApplication(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setFixedSize(QSize(1500, 600))

        barraFerramentas = QToolBar(self.ferramentas)
        prevBtn = barraFerramentas.addAction(QIcon('img/icons/previous.png'), 'Voltar')
        homeBtn = barraFerramentas.addAction(QIcon('img/icons/homepage.png'), 'Pagina Inicial')

        self.search = QLineEdit()
        self.search.setMinimumWidth(50)
        self.search.setPlaceholderText('Digite aqui o que procurar ou endereço do website..')
        self.search.returnPressed.connect(self.searchWeb)
        searchBox = barraFerramentas.addWidget(self.search)

        _searchBtn = QPushButton(QIcon('img/icons/web.png'), 'Navegar')
        _searchBtn.clicked.connect(self.searchWeb)
        searchBtn = barraFerramentas.addWidget(_searchBtn)

        self.tab = QTabWidget(self.ferramentas)
        self.tab.setGeometry(0, 50, 1500, 570)
        self.tab.setDocumentMode(True)
        self.tab.setTabsClosable(True)

        self.janela1 = None

        self.janelaPrincipal()

    def janelaPrincipal(self):
        self.janela1 = QWebEngineView()
        self.janela1.setUrl(QUrl('https://google.com/'))
        self.tab.addTab(self.janela1, f'{self.janela1.title()}')
        self.tab.setCurrentIndex(self.tab.currentIndex())

    def searchWeb(self):
        url = re.compile('[a-z_0-9a-z].[a-z]{2,3}')
        if 'https://' in self.search.text():
            request = self.search.text()
            self.janela1.setUrl(QUrl(request))
        else:
            pesquisar = self.search.text().replace(' ', '+')
            request = f'https://google.com/search/?q={pesquisar}&oq={pesquisar}'
            self.janela1.setUrl(QUrl(request))


if __name__ == '__main__':
    app = GCr()
    app.ferramentas.show()
    app.gc.exec_()
