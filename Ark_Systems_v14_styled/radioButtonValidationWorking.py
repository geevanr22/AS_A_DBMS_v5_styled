from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QVBoxLayout, QRadioButton, QDialog, QButtonGroup)
import sys



class StatusRadioButton(QDialog):
    def __init__(self):
        super().__init__()

        self.show()

        self.radioButtonGroup = QButtonGroup()
        self.statusRadioButton_1 = QRadioButton('Existing')
        self.statusRadioButton_1.clicked.connect(self.buttonClicked)
        self.statusRadioButton_2 = QRadioButton('Dissolved')
        self.statusRadioButton_2.clicked.connect(self.buttonClicked)
        self.statusRadioButton_3 = QRadioButton('Winding Up')
        self.statusRadioButton_3.clicked.connect(self.buttonClicked)
        self.radioButtonGroup.addButton(self.statusRadioButton_1)
        self.radioButtonGroup.addButton(self.statusRadioButton_2)
        self.radioButtonGroup.addButton(self.statusRadioButton_3)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.statusRadioButton_1)
        self.layout.addWidget(self.statusRadioButton_2)
        self.layout.addWidget(self.statusRadioButton_3)
        self.setLayout(self.layout)

    def buttonClicked(self):
        if self.statusRadioButton_1.isChecked():
            self.CoStatus = self.statusRadioButton_1.text()
            print('RB1')

        elif self.statusRadioButton_2.isChecked():
            self.CoStatus = self.statusRadioButton_2.text()
            print('RB1')

        elif self.statusRadioButton_3.isChecked():
            self.CoStatus = self.statusRadioButton_3.text()
            print('RB1')
        else:
            pass



# app = QApplication(sys.argv)
# win = StatusRadioButton()
# sys.exit(app.exec_())
