# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 100, 501, 231))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setGeometry(QtCore.QRect(410, 70, 75, 25))
        self.toolButton.setObjectName("toolButton")
        self.saveTextEdit = QtWidgets.QLineEdit(self.tab)
        self.saveTextEdit.setGeometry(QtCore.QRect(100, 70, 300, 25))
        self.saveTextEdit.setObjectName("saveTextEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 160, 491, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.downloadButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout.addWidget(self.downloadButton)
        
        self.urlTextEdit = QtWidgets.QLineEdit(self.tab)
        self.urlTextEdit.setGeometry(QtCore.QRect(100, 40, 300, 25))
        self.urlTextEdit.setObjectName("urlTextEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 101, 21))
        self.label_2.setObjectName("label_2")
        
        self.resolutionComboBox = QtWidgets.QComboBox(self.tab)
        self.resolutionComboBox.setGeometry(QtCore.QRect(150, 100, 81, 21))
        self.resolutionComboBox.setObjectName("resolutioncomboBox")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 10, 271, 20))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        
        
      
       
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(0, 100, 131, 20))
        self.label_10.setObjectName("label_10")
        
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 0, 2620, 100))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "Browse"))
        self.downloadButton.setText(_translate("MainWindow", "Tải xuống"))
        
        self.label_2.setText(_translate("MainWindow", " Video URL : "))
        self.label_3.setText(_translate("MainWindow", " Lưu vào : "))
        self.label.setText(_translate("MainWindow", "Nhập URL và đường dẫn tải xuống"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tải xuống"))
        
   
        self.label_10.setText(_translate("MainWindow", " Độ phân giải : "))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
