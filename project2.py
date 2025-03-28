from PyQt6 import QtWidgets, uic
import pdb
import sys

app = QtWidgets.QApplication(sys.argv)

win = uic.loadUi("testWindow.ui")

win.show()
pdb.set_trace()
sys.exit(app.exec())


