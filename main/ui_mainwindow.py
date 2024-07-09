# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(771, 621)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.okButton = QPushButton(self.centralwidget)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setGeometry(QRect(360, 470, 75, 24))
        self.promptText = QTextEdit(self.centralwidget)
        self.promptText.setObjectName(u"promptText")
        self.promptText.setGeometry(QRect(250, 360, 311, 61))
        self.labelPrompt = QLabel(self.centralwidget)
        self.labelPrompt.setObjectName(u"labelPrompt")
        self.labelPrompt.setGeometry(QRect(370, 340, 49, 16))
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(250, 100, 301, 201))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.labelHeight = QLabel(self.formLayoutWidget)
        self.labelHeight.setObjectName(u"labelHeight")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelHeight)

        self.heightBox = QComboBox(self.formLayoutWidget)
        self.heightBox.addItem("")
        self.heightBox.addItem("")
        self.heightBox.addItem("")
        self.heightBox.addItem("")
        self.heightBox.setObjectName(u"heightBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.heightBox)

        self.labelWidth = QLabel(self.formLayoutWidget)
        self.labelWidth.setObjectName(u"labelWidth")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelWidth)

        self.widthBox = QComboBox(self.formLayoutWidget)
        self.widthBox.addItem("")
        self.widthBox.addItem("")
        self.widthBox.addItem("")
        self.widthBox.addItem("")
        self.widthBox.setObjectName(u"widthBox")
        self.widthBox.setEditable(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.widthBox)

        self.labelInference = QLabel(self.formLayoutWidget)
        self.labelInference.setObjectName(u"labelInference")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelInference)

        self.editInference = QLineEdit(self.formLayoutWidget)
        self.editInference.setObjectName(u"editInference")
        self.editInference.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editInference)

        self.labelGuidance = QLabel(self.formLayoutWidget)
        self.labelGuidance.setObjectName(u"labelGuidance")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelGuidance)

        self.editGuidance = QLineEdit(self.formLayoutWidget)
        self.editGuidance.setObjectName(u"editGuidance")
        self.editGuidance.setMaxLength(3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.editGuidance)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 771, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.widthBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GenQT", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.okButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.promptText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prompt here!", None))
        self.labelPrompt.setText(QCoreApplication.translate("MainWindow", u"Prompt", None))
        self.labelHeight.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.heightBox.setItemText(0, QCoreApplication.translate("MainWindow", u"256", None))
        self.heightBox.setItemText(1, QCoreApplication.translate("MainWindow", u"512", None))
        self.heightBox.setItemText(2, QCoreApplication.translate("MainWindow", u"768", None))
        self.heightBox.setItemText(3, QCoreApplication.translate("MainWindow", u"1024", None))

        self.labelWidth.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.widthBox.setItemText(0, QCoreApplication.translate("MainWindow", u"256", None))
        self.widthBox.setItemText(1, QCoreApplication.translate("MainWindow", u"512", None))
        self.widthBox.setItemText(2, QCoreApplication.translate("MainWindow", u"768", None))
        self.widthBox.setItemText(3, QCoreApplication.translate("MainWindow", u"1024", None))

        self.widthBox.setCurrentText(QCoreApplication.translate("MainWindow", u"256", None))
        self.labelInference.setText(QCoreApplication.translate("MainWindow", u"Inference steps", None))
        self.editInference.setInputMask(QCoreApplication.translate("MainWindow", u"D9", None))
        self.editInference.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.labelGuidance.setText(QCoreApplication.translate("MainWindow", u"Guidance scale", None))
        self.editGuidance.setInputMask(QCoreApplication.translate("MainWindow", u"D.9", None))
        self.editGuidance.setText(QCoreApplication.translate("MainWindow", u"7.0", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

