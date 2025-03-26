from PyQt6 import QtWidgets, QtCore
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(800, 600)
        self.widget_list = []
        self.vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbox)

        self.label = QtWidgets.QLabel("______")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.vbox.addWidget(self.label)

        self.add_new_widget(QtWidgets.QPushButton("1"), "Один")
        self.add_new_widget(QtWidgets.QPushButton("2"), "Два")
        self.add_new_widget(QtWidgets.QPushButton("3"), "Три")
        self.add_new_widget(QtWidgets.QPushButton("Закрыть"), "Закрыть")

    def on_click(self, message, widget):
        match message:
            case "Закрыть":
                print(message)
                self.close()
            case _:
                self.label.setText(message)
                print(message)
                widget.setText("Удаляем...")
                QtCore.QTimer.singleShot(1000, widget.deleteLater) 

    def add_new_widget(self, widget, message):
        self.vbox.addWidget(widget)
        self.widget_list.append(widget)
        widget.clicked.connect(lambda: self.on_click(message, widget))


app = QtWidgets.QApplication(sys.argv)
windows = MyWindow()
windows.show()
sys.exit(app.exec())
