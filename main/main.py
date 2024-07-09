import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self) 
        self._ui.okButton.clicked.connect(self.say_hello)

    @Slot()
    def say_hello(self):
        text = self._ui.promptText.toPlainText()
        print(text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

