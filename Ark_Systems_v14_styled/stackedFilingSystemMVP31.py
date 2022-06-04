import sys
import sqlite3
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QStackedWidget, QVBoxLayout, QHBoxLayout,)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from mvp31_filingEngine import FilingSystem


class StackedFilingSystem(QWidget):
    def __init__(self):
        super().__init__()

        #Set Window Title

        self.setWindowTitle('Filing Tray')
        self.setGeometry(1530, 580, 400, 300)
        self.show()

        # StackedWidget
        self.stackedWidget = QStackedWidget()
        self.docFolderNameList = ['Directors_Circular', 'Members_Meeting', 'Register', 'Share_Certificate', 'Summary',
                         'Checklist', 'Correspondence', 'Bill_SOA', 'SSM_Receipt', 'Application_Of_Reg',
                         'Availability_Names_Reg', 'Application_Change_Name', 'Lodgement_Constitution',
                         'Notify_Alteration_Amendment', 'Change_Reg_Add', 'Not_at_Reg_Add', 'Change_Add_Reg_Are_Kept',
                         'Change_Reg_of_Members', 'Change_Reg_Dir_Mgr_Sec', 'Annual_Return_of_Company',
                         'Approval_for_Allotment', 'Return_for_Allotment', 'Variation_Class_of_Rights',
                         'Instrument_of_Transfer', 'Solvency_Statement', 'Declaration_Appnt_as_Director',
                         'Notice_Contract_Serv_Director', 'Declaration_Appnt_as_Secretary', 'Vacate_Office_of_Secretary',
                         'Dec_by_Sec_to_Cease_Off', 'Reg_to_Act_as_Sec', 'Diff_Accounting_Periods', 'EOT_Financial_Statements',
                         'Exempt_Private_Company', 'Lodge_with_Charge', 'Series_of_Debentures', 'Assignment_of_Charge',
                         'Variations_Terms_of_Change', 'Property_Undertaking_Memo', 'Memo_Satisfaction_Reg_Charge',
                         'Dec_Verifying_Memo', 'Satisfaction_of_Charge', 'Strike_of_Company', 'Object_Striking_of_Company',
                         'Withdraw_Striking_of_Company', 'Change_in_Bus_Add_or_Nat_of_Bus', 'Miscellaneous_1', 'Temporary_Folder']

        self.countDocFolderNameList = len(self.docFolderNameList)
        print(self.countDocFolderNameList)

        for folder in self.docFolderNameList:
            self.stackedWidget.addWidget(FilingSystem(f'{folder}'))



        self.stackedWidgetButtons()
        self.layoutSetup()


    def stackedWidgetButtons(self):
        # Note: StackedWidget Buttons (Separate from the filing system buttons, StackedWidget Buttons are fixed to the StackedWidget)
        self.prevButton = QPushButton('Previous')
        self.prevButton.clicked.connect(self.clickPreviousButton)
        self.nextButton = QPushButton('Next')
        self.nextButton.clicked.connect(self.clickNextButton)

    def clickPreviousButton(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex()-1) % int(f'{self.countDocFolderNameList}')) # programatically fetches the number of folders in list

    def clickNextButton(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex()+1) % int(f'{self.countDocFolderNameList}')) # programatically fetches the number of folders in list

    def layoutSetup(self):

        #Button Layout
        self.buttonLayout_h = QHBoxLayout()
        self.buttonLayout_h.addWidget(self.prevButton)
        self.buttonLayout_h.addWidget(self.nextButton)

        #MainLayouts
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addSpacing(10)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addWidget(self.stackedWidget)
        self.mainLayout.addLayout(self.buttonLayout_h)
        self.setLayout(self.mainLayout)



# app = QApplication(sys.argv)
# window = StackedFilingSystem()
# sys.exit(app.exec())
