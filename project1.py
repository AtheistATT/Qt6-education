from PyQt6 import QtWidgets, QtCore
import sys, time

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(800, 600)
        self.button_exit = QtWidgets.QPushButton("&Закрыть")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.button_exit)
        self.setLayout(self.vbox)

        self.button_exit.clicked.connect(lambda: self.quit("Закрыть"))

    def quit(self, message):
        match message:
            case "Закрыть":
                print(message)
                QtWidgets.QApplication.instance().quit()

app = QtWidgets.QApplication(sys.argv)
windows = MyWindow()
windows.show()
sys.exit(app.exec())
