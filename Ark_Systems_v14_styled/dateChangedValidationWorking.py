from PyQt5.QtWidgets import (QApplication, QDialog, QDateEdit, QLabel, QVBoxLayout,QHBoxLayout,
                             QPushButton)
import sys
from customMessageBoxClass import customMessage


# This is Working

class Date(QDialog):
    def __init__(self):
        super().__init__()

        self.show()

        self.dateLabel1 = QLabel('Date1')
        self.dateEdit1 = QDateEdit()
        self.dateEdit1.dateChanged.connect(self.checkDateChange1)

        self.dateLabel2 = QLabel('Date2')
        self.dateEdit2 = QDateEdit()
        self.dateEdit2.dateChanged.connect(self.checkDateChange2)

        self.hboxlayout1 = QHBoxLayout()
        self.hboxlayout2 = QHBoxLayout()

        self.vboxlayout = QVBoxLayout()

        self.hboxlayout1.addWidget(self.dateLabel1)
        self.hboxlayout1.addWidget(self.dateEdit1)

        self.hboxlayout2.addWidget(self.dateLabel2)
        self.hboxlayout2.addWidget(self.dateEdit2)


        self.vboxlayout.addLayout(self.hboxlayout1)
        self.vboxlayout.addLayout(self.hboxlayout2)
        self.setLayout(self.vboxlayout)

        self.submitButton = QPushButton('Submit')
        self.submitButton.clicked.connect(self.submitButtonClicked)

        self.vboxlayout.addWidget(self.submitButton)


    def checkDateChange1(self):

        self.dateChanged1 = self.dateEdit1

        if self.dateChanged1 == True:
            print('Date1 was changed')

    def checkDateChange2(self):

        self.dateChanged2 = self.dateEdit2

        if self.dateChanged2 == True:
            print('Date2 was changed')


    def submitButtonClicked(self):

        try:
            if self.dateChanged1 == True:
                pass

            if self.dateChanged2 == True:
                pass

            customMessage('Well done Submitting.....................')

        except:
            customMessage('Please ensure all dates are changed')



app = QApplication(sys.argv)
win = Date()
sys.exit(app.exec())


