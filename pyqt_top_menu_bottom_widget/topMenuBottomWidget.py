from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QMainWindow, QGridLayout, QGraphicsView


class TopMenuBottomWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        btn1 = QPushButton('A')
        btn2 = QPushButton('B')

        btn1.setStyleSheet('QPushButton { border: 0; background: #DDD; padding: 5px; }')
        btn2.setStyleSheet('QPushButton { border: 0; background: #DDD; padding: 5px; }')

        lay = QHBoxLayout()
        lay.addWidget(btn1)
        lay.addWidget(btn2)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)

        menuWidget = QWidget()
        menuWidget.setLayout(lay)

        view = QGraphicsView()
        view.setStyleSheet('QGraphicsView { border: 0; }')

        lay = QVBoxLayout()
        lay.addWidget(menuWidget)
        lay.addWidget(view)
        lay.setContentsMargins(1, 1, 1, 1)
        lay.setSpacing(0)

        mainInnerWidget = QWidget()
        mainInnerWidget.setLayout(lay)

        lay = QGridLayout()
        lay.addWidget(mainInnerWidget)

        mainWidget = QWidget()
        mainInnerWidget.setObjectName('mainWidget')
        mainWidget.setLayout(lay)

        self.setStyleSheet('QWidget#mainWidget { border: 1px solid gray; }')

        self.setCentralWidget(mainWidget)
