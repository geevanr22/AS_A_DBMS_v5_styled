from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QPushButton, QTextEdit,
                             QRadioButton, QVBoxLayout, QHBoxLayout,QButtonGroup, QDateEdit)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from customMessageBoxClass import customMessage

class MainUI(QWidget):
    def __init__(self):
        super().__init__()

    def uiSetup2(self):
        # File No
        # Horizontal Layout 1
        self.horizontalLayout_1 = QHBoxLayout()
        self.label_fileNo = QLabel('File No')
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

        # Vertical Layout for Date of Change and Incorporation
        self.dateOfChangeVerticalLayout_1 = QVBoxLayout()
        self.dateOfChangeVerticalLayout_1.addWidget(self.label_DateOfChange)
        self.dateOfChangeVerticalLayout_1.addWidget(self.dateEditDateOfChange)

        self.dateOfIncorporationVerticalLayout_1 = QVBoxLayout()
        self.dateOfIncorporationVerticalLayout_1.addWidget(self.label_IncorporatedDate)
        self.dateOfIncorporationVerticalLayout_1.addWidget(self.dateEditIncorporatedDate)

        # Vertical Layout: Type of Company
        self.radioButtonTypeVerticalLayout_1 = QVBoxLayout()
        self.typeLabel = QLabel('Type')
        self.typeLabelBlank = QLabel('')  # This is used to insert blank spacing
        # Radio Buttons: Type of Company
        self.typeRadioButton_1 = QRadioButton('Limited By Shares')
        self.typeRadioButton_2 = QRadioButton('Private Limited')
        # Radio Button Group: Type of Company
        self.radioButtonGroup_Company_Type = QButtonGroup(self)
        self.radioButtonGroup_Company_Type.addButton(self.typeRadioButton_1)
        self.radioButtonGroup_Company_Type.addButton(self.typeRadioButton_2)

        self.radioButtonTypeVerticalLayout_1.addWidget(self.typeLabel)
        self.radioButtonTypeVerticalLayout_1.addWidget(self.typeLabelBlank)  # Blank Spacing for better alignment of Vertical Radio Buttons
        self.radioButtonTypeVerticalLayout_1.addWidget(self.typeRadioButton_1)
        self.radioButtonTypeVerticalLayout_1.addWidget(self.typeRadioButton_2)

        # Vertical Layout: Status of Company
        self.radioButtonStatusVerticalLayout_2 = QVBoxLayout()
        self.statusLabel = QLabel('Status')
        # Radio Buttons: Status of Company
        self.statusRadioButton_1 = QRadioButton('Existing')
        self.statusRadioButton_2 = QRadioButton('Dissolved')
        self.statusRadioButton_3 = QRadioButton('Winding Up')
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
        self.horizontalLayout_2.addLayout(self.radioButtonTypeVerticalLayout_1)
        self.horizontalLayout_2.addLayout(self.radioButtonStatusVerticalLayout_2)

        # Horizontal Layout 3: Registered & Business Address ######################################################################################

        # Registered & Business Address
        self.labelRegisteredAdd = QLabel('Registered Address')
        self.lineRegisteredAdd = QTextEdit()
        self.verticalLayout3_RegisteredAdd = QVBoxLayout()
        self.verticalLayout3_RegisteredAdd.addWidget(self.labelRegisteredAdd)
        self.verticalLayout3_RegisteredAdd.addWidget(self.lineRegisteredAdd)

        self.labelBusinessAdd = QLabel('Business Address')
        self.lineBusinessAdd = QTextEdit()
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

        self.labelSecretariesName = QLabel('Secretaries:')
        self.lineEditSecretariesName_1 = QLineEdit()
        self.lineEditSecretariesName_2 = QLineEdit()

        self.verticalLayout7_DirectorsSecretaries = QVBoxLayout()
        self.verticalLayout7_DirectorsSecretaries.addWidget(self.labelDirectorName)
        self.verticalLayout7_DirectorsSecretaries.addWidget(self.lineEditDirectorName_1)
        self.verticalLayout7_DirectorsSecretaries.addWidget(self.lineEditDirectorName_2)
        self.verticalLayout7_DirectorsSecretaries.addWidget(self.labelSecretariesName)
        self.verticalLayout7_DirectorsSecretaries.addWidget(self.lineEditSecretariesName_1)
        self.verticalLayout7_DirectorsSecretaries.addWidget(self.lineEditSecretariesName_2)

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
        self.horizontalLayout_5_DirectorAndContact.addLayout(self.verticalLayout7_DirectorsSecretaries)
        self.horizontalLayout_5_DirectorAndContact.addLayout(self.verticalLayout8_Contact)

        # Final Horizontal Layout has 3 Sub Vertical Layouts within

        self.labelAppointedDate = QLabel('Appointed Date')
        self.labelResignedDate = QLabel('Resigned Date')
        self.labelVacatedDate = QLabel('Vacated Date')
        self.verticalLayout9_AppointedDateLabel = QVBoxLayout()
        self.verticalLayout9_AppointedDateLabel.addWidget(self.labelAppointedDate)
        self.verticalLayout9_AppointedDateLabel.addWidget(self.labelResignedDate)
        self.verticalLayout9_AppointedDateLabel.addWidget(self.labelVacatedDate)

        self.dateEditAppointedDate = QDateEdit()
        self.dateEditResignedDate = QDateEdit()
        self.dateEditVacatedDate = QDateEdit()
        self.verticalLayout10_AppointedDate = QVBoxLayout()
        self.verticalLayout10_AppointedDate.addWidget(self.dateEditAppointedDate)
        self.verticalLayout10_AppointedDate.addWidget(self.dateEditResignedDate)
        self.verticalLayout10_AppointedDate.addWidget(self.dateEditVacatedDate)

        self.labelPreparedBy = QLabel('Prepared By')
        self.labelScannedBy = QLabel('Scanned By')
        self.labelCheckedBy = QLabel('Checked By')
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
        self.dateEditChecked = QDateEdit()
        self.dateEditScanned = QDateEdit()
        self.verticalLayout13_datePrepared = QVBoxLayout()
        self.verticalLayout13_datePrepared.addWidget(self.dateEditPrepared)
        self.verticalLayout13_datePrepared.addWidget(self.dateEditChecked)
        self.verticalLayout13_datePrepared.addWidget(self.dateEditScanned)
        self.horizontalLayout_6_AppointedBy = QHBoxLayout()
        self.horizontalLayout_6_AppointedBy.addLayout(self.verticalLayout9_AppointedDateLabel)
        self.horizontalLayout_6_AppointedBy.addLayout(self.verticalLayout10_AppointedDate)
        self.horizontalLayout_6_AppointedBy.addLayout(self.verticalLayout11_Prepared)
        self.horizontalLayout_6_AppointedBy.addLayout(self.verticalLayout12_linePrepared)
        self.horizontalLayout_6_AppointedBy.addLayout(self.verticalLayout13_datePrepared)
        self.mainLayoutTab1 = QVBoxLayout()  # The final main layout
        self.mainLayoutTab1.addLayout(self.horizontalLayout_1)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_2)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_3_RegBusiness_Add)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_4_NatureOfBusiness)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_5_DirectorAndContact)
        self.mainLayoutTab1.addLayout(self.horizontalLayout_6_AppointedBy)
        self.buttonSubmitRecord = QPushButton('Submit Record')
        self.mainLayoutTab1.addWidget(self.buttonSubmitRecord)
        self.buttonDeleteAllRecords = QPushButton('Delete All Records')
        self.mainLayoutTab1.addWidget(self.buttonDeleteAllRecords)
        self.buttonOpenFilingSystem = QPushButton('Open Filing System')
        self.mainLayoutTab1.addWidget(self.buttonOpenFilingSystem)

        self.setLayout(self.mainLayoutTab1)

        # Submit Record Button Functionality
        self.buttonSubmitRecord.clicked.connect(self.submitRecordsButton)
        self.buttonOpenFilingSystem.clicked.connect(self.openFilingSystemButton)
        # self.buttonSubmitRecord.clicked.connect(self.connectDB)
        self.buttonDeleteAllRecords.clicked.connect(self.deleteAllRecords)

    def uiSetup(self):

        # File No
        self.label_fileNo = QLabel('File No')
        self.lineEdit_1_FileNo = QLineEdit()


        # Company Name
        self.label_companyName = QLabel('Company Name')
        self.lineEdit_2_companyName = QLineEdit()


        # Company Old Name
        self.labelCompanyOldName = QLabel('Company Old Name')
        self.lineEditCompanyOldName = QLineEdit()


        # Buttons
        self.submitButton = QPushButton('Submit to Database')
        self.submitButton.clicked.connect(self.submitRecordsButton)

        self.folderButton = QPushButton('Generate Folders')
        self.folderButton.clicked.connect(self.generateFolders)

        self.clearButton = QPushButton('Clear Records')
        self.clearButton.clicked.connect(self.deleteAllRecords)

        self.filingButton = QPushButton('Filing Tray')
        self.filingButton.clicked.connect(self.openFilingSystemButton)

        self.checkDuplicateCoNameButton = QPushButton('checkDuplicateCoName')
        self.checkDuplicateCoNameButton.clicked.connect(self.checkDuplicateCoName)


        # Horizontal Layouts
        # Input Layouts
        self.hLayout_1 = QHBoxLayout()
        self.hLayout_2 = QHBoxLayout()
        self.hLayout_1.addWidget(self.label_fileNo)
        self.hLayout_1.addWidget(self.lineEdit_1_FileNo)
        self.hLayout_1.addWidget(self.label_companyName)
        self.hLayout_1.addWidget(self.lineEdit_2_companyName)
        self.hLayout_2.addWidget(self.labelCompanyOldName)
        self.hLayout_2.addWidget(self.lineEditCompanyOldName)

        # Button Layouts
        self.hbuttonLayout1 = QHBoxLayout()
        self.hbuttonLayout1.addWidget(self.submitButton)
        self.hbuttonLayout1.addWidget(self.clearButton)
        self.hbuttonLayout1.addWidget(self.filingButton)

        # MainLayouts
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.hLayout_1)
        self.mainLayout.addLayout(self.hLayout_2)
        self.mainLayout.addLayout(self.hbuttonLayout1)
        self.mainLayout.addSpacing(30)

        self.setLayout(self.mainLayout)



