from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QPushButton, QTextEdit,
                             QRadioButton, QVBoxLayout, QHBoxLayout,QButtonGroup,
                             QDateEdit, QApplication, QScrollArea, QGroupBox)
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QDate, Qt


class MainUI(QWidget):
    def __init__(self):
        super().__init__()

        self.uiSetup2()

        # self.typeRadioButtonGetSelection()




    def uiSetup2(self):
        # File No
        # Horizontal Layout 1

        self.setStyleSheet("""
            QLabel#test {
                background: #53a8b6;
            }
            QPushButton#submit {
                background-color: #2772db;
                color: white;
                font-weight: bold;
            }

        """)

        self.widget = QWidget()
        self.horizontalLayout_1 = QHBoxLayout()
        self.label_fileNo = QLabel('File No', objectName= 'test')
        self.horizontalLayout_1.addWidget(self.label_fileNo)
        self.lineEdit_3_FileNo = QLineEdit()
        self.horizontalLayout_1.addWidget(self.lineEdit_3_FileNo)

        self.label_name = QLabel('Company Name')
        self.horizontalLayout_1.addWidget(self.label_name)
        self.lineEdit_coName = QLineEdit()
        self.horizontalLayout_1.addWidget(self.lineEdit_coName)

        self.label_oldName = QLabel('Old Name')
        self.horizontalLayout_1.addWidget(self.label_oldName)
        self.lineEdit_coOldName = QLineEdit()
        self.horizontalLayout_1.addWidget(self.lineEdit_coOldName)

        self.label_regNo = QLabel('Reg No')
        self.horizontalLayout_1.addWidget(self.label_regNo)

        self.lineEdit_regNo = QLineEdit()
        self.horizontalLayout_1.addWidget(self.lineEdit_regNo)



        # Horizontal Line 2 Date of Change ############################################################################################################

        self.label_DateOfChange = QLabel('Date Of Change')
        self.dateEditDateOfChange = QDateEdit()
        self.dateEditDateOfChange.setDisplayFormat("d-MMM-yyyy")



        # https://www.geeksforgeeks.org/pyqt5-qdateedit-date-changed-signal/
        # Need to check if date is changed and if not need to put out a message or else set date to something obvious as unusable

        """ 
        date.dateChanged.connect(lambda: method())

        # method called when signal emitted
        def method():
        "Maybe we can insert a warning message here under the function when date is not changed"

        or a workaround, if datehanged, use function to print date to var else print 0000 to variable

        """

        # Horizontal Line 2 : Date Incorporated
        self.label_IncorporatedDate = QLabel('Incorporated Date')
        self.dateEditIncorporatedDate = QDateEdit()
        self.dateEditIncorporatedDate.dateChanged.connect(self.incorporatedDateChanged)
        self.dateEditIncorporatedDate.setDisplayFormat("d-MMM-yyyy")

        # Vertical Layout for Date of Change and Incorporation
        self.dateOfChangeVerticalLayout_1 = QVBoxLayout()
        self.dateOfChangeVerticalLayout_1.addWidget(self.label_DateOfChange)
        self.dateOfChangeVerticalLayout_1.addWidget(self.dateEditDateOfChange)

        self.dateOfIncorporationVerticalLayout_1 = QVBoxLayout()
        self.dateOfIncorporationVerticalLayout_1.addWidget(self.label_IncorporatedDate)
        self.dateOfIncorporationVerticalLayout_1.addWidget(self.dateEditIncorporatedDate)

        # Vertical Layout: Type of Company
        # self.radioButtonTypeVerticalLayout_1 = QVBoxLayout()
        # self.typeLabel = QLabel('Type')
        # self.typeLabelBlank = QLabel('')  # This is used to insert blank spacing

        # Radio Buttons: Type of Company
        # self.typeRadioButton_1 = QRadioButton('Limited By Shares')
        # self.typeRadioButton_1.clicked.connect(self.typeRadioButtonClicked) # Function is in the tab1CompanyBrief File
        # self.typeRadioButton_2 = QRadioButton('Private Limited')
        # self.typeRadioButton_2.clicked.connect(self.typeRadioButtonClicked)# Function is in the tab1CompanyBrief File

        # Radio Button Group: Type of Company
        # self.radioButtonGroup_Company_Type = QButtonGroup(self)
        # self.radioButtonGroup_Company_Type.addButton(self.typeRadioButton_1)
        # self.radioButtonGroup_Company_Type.addButton(self.typeRadioButton_2)

        # self.radioButtonTypeVerticalLayout_1.addWidget(self.typeLabel)
        # self.radioButtonTypeVerticalLayout_1.addWidget(self.typeLabelBlank)  # Blank Spacing for better alignment of Vertical Radio Buttons
        # self.radioButtonTypeVerticalLayout_1.addWidget(self.typeRadioButton_1)
        # self.radioButtonTypeVerticalLayout_1.addWidget(self.typeRadioButton_2)

        # Vertical Layout: Status of Company
        self.radioButtonStatusVerticalLayout_2 = QVBoxLayout()
        self.statusLabel = QLabel('Status')

        # Radio Buttons: Status of Company
        self.statusRadioButton_1 = QRadioButton('Existing')
        self.statusRadioButton_1.clicked.connect(self.statusRadioButtonClicked)
        self.statusRadioButton_2 = QRadioButton('Dissolved')
        self.statusRadioButton_2.clicked.connect(self.statusRadioButtonClicked)
        self.statusRadioButton_3 = QRadioButton('Winding Up')
        self.statusRadioButton_3.clicked.connect(self.statusRadioButtonClicked)


        # Radio Button Group: Status of Company
        self.radioButtonGroup_Company_Status = QButtonGroup(self)
        self.radioButtonGroup_Company_Status.addButton(self.statusRadioButton_1)
        self.radioButtonGroup_Company_Status.addButton(self.statusRadioButton_2)
        self.radioButtonGroup_Company_Status.addButton(self.statusRadioButton_3)

        self.radioButtonStatusVerticalLayout_2.addWidget(self.statusLabel)
        self.radioButtonStatusVerticalLayout_2.addWidget(self.statusRadioButton_1)
        self.radioButtonStatusVerticalLayout_2.addWidget(self.statusRadioButton_2)
        self.radioButtonStatusVerticalLayout_2.addWidget(self.statusRadioButton_3)

        self.horizontalLayout_2 = QHBoxLayout()  # Horizontal Line 2

        self.horizontalLayout_2.addLayout(self.dateOfChangeVerticalLayout_1)
        self.horizontalLayout_2.addLayout(self.dateOfIncorporationVerticalLayout_1)
        # self.horizontalLayout_2.addLayout(self.radioButtonTypeVerticalLayout_1)
        self.horizontalLayout_2.addLayout(self.radioButtonStatusVerticalLayout_2)

        # Horizontal Layout 3: Registered & Business Address ######################################################################################

        # Registered & Business Address
        self.labelRegisteredAdd = QLabel('Registered Address')
        self.lineRegisteredAdd = QTextEdit()
        self.lineRegisteredAdd.setFixedHeight(40)
        self.verticalLayout3_RegisteredAdd = QVBoxLayout()
        self.verticalLayout3_RegisteredAdd.addWidget(self.labelRegisteredAdd)
        self.verticalLayout3_RegisteredAdd.addWidget(self.lineRegisteredAdd)

        self.labelBusinessAdd = QLabel('Business Address')
        self.lineBusinessAdd = QTextEdit()
        self.lineBusinessAdd.setFixedHeight(40)
        self.verticalLayout4_BusinessAdd = QVBoxLayout()
        self.verticalLayout4_BusinessAdd.addWidget(self.labelBusinessAdd)
        self.verticalLayout4_BusinessAdd.addWidget(self.lineBusinessAdd)

        self.horizontalLayout_3_RegBusiness_Add = QHBoxLayout()  # Business and Registered Address VBox
        self.horizontalLayout_3_RegBusiness_Add.addLayout(self.verticalLayout3_RegisteredAdd)
        self.horizontalLayout_3_RegBusiness_Add.addLayout(self.verticalLayout4_BusinessAdd)

        # Nature of Business

        self.labelNatureOfBusiness = QLabel('Nature of Business')
        self.lineEditNatureOfBusiness = QLineEdit()

        self.labelPaidUpCapital = QLabel('Paid-Up Capital')
        self.lineEditPaidUpCapital = QLineEdit()

        self.horizontalLayout_4_NatureOfBusiness = QHBoxLayout()
        self.horizontalLayout_4_NatureOfBusiness.addWidget(self.labelNatureOfBusiness)
        self.horizontalLayout_4_NatureOfBusiness.addWidget(self.lineEditNatureOfBusiness)
        self.horizontalLayout_4_NatureOfBusiness.addWidget(self.labelPaidUpCapital)
        self.horizontalLayout_4_NatureOfBusiness.addWidget(self.lineEditPaidUpCapital)

        # Members, Shares, Directors Name, Secretaries, Contact Person, Contact Tel, Contact Email

        # self.labelRegisteredAdd = QLabel('Registered Address')
        # self.lineRegisteredAdd = QTextEdit()

        self.labelMembersShares = QLabel('Members / Shares:')
        self.editMembers_1 = QLineEdit()
        self.editMembers_2 = QLineEdit()
        self.editMembers_3 = QLineEdit()
        self.editMembers_4 = QLineEdit()
        self.editMembers_5 = QLineEdit()

        self.verticalLayout5_MemberShares = QVBoxLayout()
        self.verticalLayout5_MemberShares.addWidget(self.labelMembersShares)
        self.verticalLayout5_MemberShares.addWidget(self.editMembers_1)
        self.verticalLayout5_MemberShares.addWidget(self.editMembers_2)
        self.verticalLayout5_MemberShares.addWidget(self.editMembers_3)
        self.verticalLayout5_MemberShares.addWidget(self.editMembers_4)
        self.verticalLayout5_MemberShares.addWidget(self.editMembers_5)

        self.labelShares = QLabel('Shares:')
        self.lineEditShares_1 = QLineEdit()
        self.lineEditShares_2 = QLineEdit()
        self.lineEditShares_3 = QLineEdit()
        self.lineEditShares_4 = QLineEdit()
        self.lineEditShares_5 = QLineEdit()

        self.verticalLayout6_Shares = QVBoxLayout()
        self.verticalLayout6_Shares.addWidget(self.labelShares)
        self.verticalLayout6_Shares.addWidget(self.lineEditShares_1)
        self.verticalLayout6_Shares.addWidget(self.lineEditShares_2)
        self.verticalLayout6_Shares.addWidget(self.lineEditShares_3)
        self.verticalLayout6_Shares.addWidget(self.lineEditShares_4)
        self.verticalLayout6_Shares.addWidget(self.lineEditShares_5)

        self.labelDirectorName = QLabel('Director(s) Name:')
        self.lineEditDirectorName_1 = QLineEdit()
        self.lineEditDirectorName_2 = QLineEdit()



        self.verticalLayout7_Directors = QVBoxLayout()
        self.verticalLayout7_Directors.addWidget(self.labelDirectorName)
        self.verticalLayout7_Directors.addWidget(self.lineEditDirectorName_1)
        self.verticalLayout7_Directors.addWidget(self.lineEditDirectorName_2)



        # Contact Person and Details

        self.labelContactPerson = QLabel('Contact Person:')
        self.lineEditContactPerson = QLineEdit()
        self.labelContactTel = QLabel('Contact Tel:')
        self.lineEditContactTel = QLineEdit()
        self.labelContactEmail = QLabel('Contact Email')
        self.lineEditContactEmail = QLineEdit()

        self.verticalLayout8_Contact = QVBoxLayout()
        self.verticalLayout8_Contact.addWidget(self.labelContactPerson)
        self.verticalLayout8_Contact.addWidget(self.lineEditContactPerson)
        self.verticalLayout8_Contact.addWidget(self.labelContactTel)
        self.verticalLayout8_Contact.addWidget(self.lineEditContactTel)
        self.verticalLayout8_Contact.addWidget(self.labelContactEmail)
        self.verticalLayout8_Contact.addWidget(self.lineEditContactEmail)

        self.horizontalLayout_5_DirectorAndContact = QHBoxLayout()
        self.horizontalLayout_5_DirectorAndContact.addLayout(self.verticalLayout5_MemberShares)
        self.horizontalLayout_5_DirectorAndContact.addLayout(self.verticalLayout6_Shares)
        self.horizontalLayout_5_DirectorAndContact.addLayout(self.verticalLayout7_Directors)
        self.horizontalLayout_5_DirectorAndContact.addLayout(self.verticalLayout8_Contact)

        # Final Horizontal Layout has 3 Sub Vertical Layouts within

        # Secretaries 1 ----------------------------------------------------------------------
        self.labelSecretaries_1_Name = QLabel('Company Secretary (CoSEC) 1:')
        self.lineEditSecretariesName_1 = QLineEdit()
        # self.labelSecretaries_2_Name = QLabel('Secretaries 2:')
        # self.lineEditSecretariesName_2 = QLineEdit()

        self.labelAppointedDate_Secretary_1 = QLabel('(CoSEC) 1: Appointed Date')
        self.labelResignedDate_Secretary_1 = QLabel('(CoSEC) 1: Resigned Date')
        self.labelVacatedDate_Secretary_1 = QLabel('(CoSEC) 1: Vacated Date')

        self.dateEditAppointedDate_Secretary_1 = QDateEdit()
        self.dateEditAppointedDate_Secretary_1.setDisplayFormat("d-MMM-yyyy")
        self.dateEditResignedDate_Secretary_1 = QDateEdit()
        self.dateEditResignedDate_Secretary_1.setDisplayFormat("d-MMM-yyyy")
        self.dateEditVacatedDate_Secretary_1 = QDateEdit()
        self.dateEditVacatedDate_Secretary_1.setDisplayFormat("d-MMM-yyyy")

        # Vertical Layouts for both Secretaries Vertical 9 & 10
        # Vertical Layout 9

        self.verticalLayout9_Secretaries_1 = QVBoxLayout()
        self.verticalLayout9_Secretaries_1.addWidget(self.labelSecretaries_1_Name)
        self.verticalLayout9_Secretaries_1.addWidget(self.lineEditSecretariesName_1)
        self.verticalLayout9_Secretaries_1.addWidget(self.labelAppointedDate_Secretary_1)
        self.verticalLayout9_Secretaries_1.addWidget(self.dateEditAppointedDate_Secretary_1)
        self.verticalLayout9_Secretaries_1.addWidget(self.labelResignedDate_Secretary_1)
        self.verticalLayout9_Secretaries_1.addWidget(self.dateEditResignedDate_Secretary_1)
        self.verticalLayout9_Secretaries_1.addWidget(self.labelVacatedDate_Secretary_1)
        self.verticalLayout9_Secretaries_1.addWidget(self.dateEditVacatedDate_Secretary_1)


        # Secretaries 2 ----------------------------------------------------------------------
        self.labelSecretaries_2_Name = QLabel('Company Secretary (CoSEC) 2:')
        self.lineEditSecretariesName_2 = QLineEdit()

        self.labelAppointedDate_Secretary_2 = QLabel('(CoSEC) 2: Appointed Date')
        self.labelResignedDate_Secretary_2 = QLabel('(CoSEC) 2: Resigned Date')
        self.labelVacatedDate_Secretary_2 = QLabel('(CoSEC) 2: Vacated Date')

        self.dateEditAppointedDate_Secretary_2 = QDateEdit()
        self.dateEditAppointedDate_Secretary_2.setDisplayFormat("d-MMM-yyyy")
        self.dateEditResignedDate_Secretary_2 = QDateEdit()
        self.dateEditResignedDate_Secretary_2.setDisplayFormat("d-MMM-yyyy")
        self.dateEditVacatedDate_Secretary_2 = QDateEdit()
        self.dateEditVacatedDate_Secretary_2.setDisplayFormat("d-MMM-yyyy")

        # Vertical Layouts 10

        self.verticalLayout10_Secretaries_2 = QVBoxLayout()
        self.verticalLayout10_Secretaries_2.addWidget(self.labelSecretaries_2_Name)
        self.verticalLayout10_Secretaries_2.addWidget(self.lineEditSecretariesName_2)

        self.verticalLayout10_Secretaries_2.addWidget(self.labelAppointedDate_Secretary_2)
        self.verticalLayout10_Secretaries_2.addWidget(self.dateEditAppointedDate_Secretary_2)
        self.verticalLayout10_Secretaries_2.addWidget(self.labelResignedDate_Secretary_2)
        self.verticalLayout10_Secretaries_2.addWidget(self.dateEditResignedDate_Secretary_2)
        self.verticalLayout10_Secretaries_2.addWidget(self.labelVacatedDate_Secretary_2)
        self.verticalLayout10_Secretaries_2.addWidget(self.dateEditVacatedDate_Secretary_2)

        # Vertical Layout 10

        # Secretaries Horizontal Layout add vertical layout 9 & 10 here

        self.horizontalLayout_6_Secretaries = QHBoxLayout()
        self.horizontalLayout_6_Secretaries.addLayout(self.verticalLayout9_Secretaries_1)
        self.horizontalLayout_6_Secretaries.addLayout(self.verticalLayout10_Secretaries_2)


        # Final Horizontal Line
        self.labelPreparedBy = QLabel('Current Project Prepared By:')
        self.labelScannedBy = QLabel('Current Project Scanned By:')
        self.labelCheckedBy = QLabel('Current Project Checked By:')

        self.verticalLayout11_Prepared = QVBoxLayout()
        self.verticalLayout11_Prepared.addWidget(self.labelPreparedBy)
        self.verticalLayout11_Prepared.addWidget(self.labelScannedBy)
        self.verticalLayout11_Prepared.addWidget(self.labelCheckedBy)

        self.lineEditPreparedBy = QLineEdit()
        self.lineEditCheckedBy = QLineEdit()
        self.lineEditScannedBy = QLineEdit()

        self.verticalLayout12_linePrepared = QVBoxLayout()
        self.verticalLayout12_linePrepared.addWidget(self.lineEditPreparedBy)
        self.verticalLayout12_linePrepared.addWidget(self.lineEditCheckedBy)
        self.verticalLayout12_linePrepared.addWidget(self.lineEditScannedBy)

        self.dateEditPrepared = QDateEdit()
        self.dateEditPrepared.setDisplayFormat("d-MMM-yyyy")
        self.dateEditChecked = QDateEdit()
        self.dateEditChecked.setDisplayFormat("d-MMM-yyyy")
        self.dateEditScanned = QDateEdit()
        self.dateEditScanned.setDisplayFormat("d-MMM-yyyy")






        self.verticalLayout13_datePrepared = QVBoxLayout()
        self.verticalLayout13_datePrepared.addWidget(self.dateEditPrepared)
        self.verticalLayout13_datePrepared.addWidget(self.dateEditChecked)
        self.verticalLayout13_datePrepared.addWidget(self.dateEditScanned)

        self.horizontalLayout_7_PreparedScannedChecked = QHBoxLayout()
        # self.horizontalLayout_6_AppointedBy.addLayout(self.verticalLayout9_AppointedDateLabel)
        # self.horizontalLayout_6_AppointedBy.addLayout(self.verticalLayout10_AppointedDate)
        self.horizontalLayout_7_PreparedScannedChecked.addLayout(self.verticalLayout11_Prepared)

        self.horizontalLayout_7_PreparedScannedChecked.addLayout(self.verticalLayout12_linePrepared)
        self.horizontalLayout_7_PreparedScannedChecked.addLayout(self.verticalLayout13_datePrepared)

        self.mainLayoutTab1 = QVBoxLayout()  # The final main layout



        self.mainLayoutTab1.addLayout(self.horizontalLayout_1)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_2)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_3_RegBusiness_Add)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_4_NatureOfBusiness)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_5_DirectorAndContact)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_6_Secretaries)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_7_PreparedScannedChecked)

        # Buttons cased in an Horizontal Layout
        self.buttonHorizontal = QHBoxLayout()
        self.buttonSubmitRecord = QPushButton('Submit Record', objectName='submit')
        self.buttonHorizontal.addWidget(self.buttonSubmitRecord)
        # self.buttonDeleteAllRecords = QPushButton('Delete All Records') # Removing 'Delete All Records' button from Corporate Brief / Tab1
        # self.buttonHorizontal.addWidget(self.buttonDeleteAllRecords)
        self.buttonOpenFilingSystem = QPushButton('Open Filing System')
        self.buttonHorizontal.addWidget(self.buttonOpenFilingSystem)

        self.mainLayoutTab1.addLayout(self.buttonHorizontal)

        # Scroll Area ________________________________________________________________________________________________
        # self.scroll = QScrollArea()
        # self.groupBox = QGroupBox()
        # self.groupBox.setLayout(self.mainLayoutTab1)
        # self.scroll.setWidget(self.groupBox)
        #
        # # self.mainLayoutTab1.addWidget(self.scroll)
        # self.mainLayoutTab2 = QVBoxLayout()
        # self.mainLayoutTab2.addWidget(self.scroll)

        self.scrollingWidget = QWidget()
        self.scrollingWidget.setLayout(self.mainLayoutTab1)
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidget(self.scrollingWidget)
        self.scrollArea.setMinimumSize(1100, 800)

        # self.scrollArea.setFixedHeight(800)
        # self.scrollArea.setFixedWidth(1500)
        self.parentMainLayout = QVBoxLayout(self)
        self.parentMainLayout.addWidget(self.scrollArea)
        # ____________________________________________________________________________________________________________________


        self.setLayout(self.mainLayoutTab1)

        # Submit Record Button Functionality
        self.buttonSubmitRecord.clicked.connect(self.submitRecordsButton)
        self.buttonOpenFilingSystem.clicked.connect(self.openFilingSystemButton)
        # self.buttonDeleteAllRecords.clicked.connect(self.deleteAllRecords) # removing this button's functionality








