#pip install PyQt5
#pip install Qtpy
#pip inatall PyQtWebEngine

import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLineEdit, QPushButton


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Browser')
        self.setGeometry(100, 100, 800, 600)

        # Create a QWebEngineView widget and set it as the central widget
        # of the main window
        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        # Set the default url
        self.view.setUrl(QUrl('https://www.google.com'))

        # Create the "Back" action
        self.back_action = QAction('Back', self)
        self.back_action.setShortcut('Alt+Left')
        self.back_action.triggered.connect(self.view.back)

        # Create the "Forward" action
        self.forward_action = QAction('Forward', self)
        self.forward_action.setShortcut('Alt+Right')
        self.forward_action.triggered.connect(self.view.forward)

        # Create the "Reload" action
        self.reload_action = QAction('Reload', self)
        self.reload_action.setShortcut('F5')
        self.reload_action.triggered.connect(self.view.reload)

        # Add the actions to the toolbar
        self.toolbar = self.addToolBar('Navigation')
        self.toolbar.addAction(self.back_action)
        self.toolbar.addAction(self.forward_action)
        self.toolbar.addAction(self.reload_action)
        # Create the search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setGeometry(200, 2, 200, 20)
        self.search_button = QPushButton('Search', self)
        self.search_button.setGeometry(420, 2, 80, 20)
        self.search_button.clicked.connect(self.search)

    def search(self):
        query = self.search_bar.text()
        url = 'https://www.google.com/search?q=' + query
        self.view.setUrl(QUrl(url))

app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())
