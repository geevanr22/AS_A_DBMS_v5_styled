from PyQt5.QtWidgets import (QTabWidget, QApplication,
                             QVBoxLayout, QDialog)

from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

import sys
import os
import pandas as pd # this is necessary if you want to export the pandas df to excel
import openpyxl # this is necessary if you want to export the pandas df to excel

from mvp31_tab1CompanyBrief import Tab1
from mvp31_tab2_Outputs import Tab2

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        # self.show()
        self.setWindowTitle('AS & Associates Ark Systems File Manager 1.0')
        self.setGeometry(200, 0, 800, 600)
        flag = Qt.WindowMinMaxButtonsHint
        self.setWindowFlag(flag)


        # Add Tabs
        self.vbox = QVBoxLayout()
        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(Tab1(), 'Company Brief')
        self.tabWidget.addTab(Tab2(), 'Saved Records')


        self.vbox.addWidget(self.tabWidget)
        self.setLayout(self.vbox)

        # Generate Scanned Folder at start of the programme
        cwd = os.getcwd()  # Get current working directory to be used below

        scanDocs = 'ScannedDocs'
        if not os.path.isdir(f'{cwd}\\{scanDocs}'):  # check if Scan Folder exists
            print('Scanned Docs Folder does not exists')
            os.mkdir(scanDocs) # if scan docs folder does not exist create one
        if os.path.isdir(f'{cwd}\\{scanDocs}'):
            print('Scanned Docs has already been Generated') # else do nothing

# global app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
