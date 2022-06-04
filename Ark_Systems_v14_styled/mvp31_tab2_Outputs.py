# Functions for Tab1 Form
# These functions sets up the database and adds the inputs to the DB
# This module will then be imported from the main.py file
import PyQt5.QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,QHeaderView,
                             QAbstractScrollArea, QTableWidget,QMessageBox,
                             QTableWidgetItem, QLabel, QLineEdit, QHBoxLayout)
import sys
import sqlite3
from mvp31_deepViewUpdateWindow import DeepViewUpdateWindow
from customMessageBoxClass import customMessage
import pandas as pd
import openpyxl


class Tab2(QWidget):
    def __init__(self):
        super().__init__()

        # Display Records from the Database
        # Search Function
        self.table = QTableWidget()
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        # header columns width
        header_column_width = self.table.horizontalHeader()
        header_column_width.setSectionResizeMode(QHeaderView.ResizeToContents)
        # self.table.setRowCount(5)
        self.table.setColumnCount(91)

        self.table.setHorizontalHeaderLabels(['File No.', 'Company Name', 'Company Old Name', 'Registered No', 'Date of Name Change', 'Date of Incorporation',
        'Company Status', 'Registration Address', 'Business Address', 'Nature of Bussiness', 'Paid Up Capital', 'Member 1', 'No of Shares', 'Member 2', 'No of Shares',
        'Member 3', 'No of Shares', 'Member 4', 'No of Shares', 'Member 5', 'No of Shares', 'Director 1', 'Director 2', 'Secretaries 1',
        'Secretaries 1 Appointed Date','Secretaries 1 Resigned Date','Secretaries 1 Vacated Date', 'Secretaries 2',
        'Secretaries 2 Appointed Date', 'Secretaries 2 Resigned Date','Secretaries 2 Vacated Date',
        'Contact Name', 'Contact Phone','Contact Email', 'Prepared By', 'Prepared Date',
        'Scanned By', 'Scanned Date', 'Checked By', 'Checked Date','Dir_or_BOD','AGM_or_EGM','Directors Circular','Members Meeting', 'Register', 'Share Certificate',
        'Summary', 'Checklist', 'Correspondence', 'Bill_SOA', 'SSM_Receipt', 'Application Of Reg',
        'Availability Names Reg', 'Application Change Name', 'Lodgement Constitution', 'Notify Alteration Amendment', 'Change Reg Add',
        'Not at Reg Add', 'Change Add Reg Are Kept', 'Change Reg of Members', 'Change Reg Dir Mgr Sec', 'Annual Return of Company',
        'Approval for Allotment', 'Return for Allotment', 'Variation Class of Rights', 'Instrument of Transfer', 'Solvency Statement',
        'Declaration Appnt as Director', 'Notice Contract Serv Director', 'Declaration Appnt as Secretary', 'Vacate Office of Secretary',
        'Dec by Sec to Cease Off', 'Reg to Act as Sec', 'Diff Accounting Periods', 'EOT Financial Statements', 'Exempt Private Company',
        'Lodge with Charge', 'Series of Debentures', 'Assignment of Charge', 'Variations Terms of Change', 'Property Undertaking Memo',
        'Memo Satisfaction Reg Charge', 'Dec Verifying Memo', 'Satisfaction of Charge', 'Strike of Company', 'Object Striking of Company',
        'Withdraw Striking of Company', 'Change in Bus Add or Nature of Bus', 'Miscellaneous 1', 'Temporary Folder'])

        self.refreshRecordsBtn = QPushButton('Refresh Records')
        self.refreshRecordsBtn.clicked.connect(self.loadData)

        self.deepViewUpdateBtn = QPushButton('Update Record')
        self.deepViewUpdateBtn.clicked.connect(self.deepViewWithBriefLayout)

        self.exportToCSVBtn = QPushButton("Export to Spreadsheet")
        self.exportToCSVBtn.clicked.connect(self.exportToCSVFunction)

        self.deleteSelectedRecord = QPushButton("Delete Selected Record")
        self.deleteSelectedRecord.clicked.connect(self.deleteRecord)




        self.mainLayoutTab2 = QVBoxLayout()
        self.tableLayout = QVBoxLayout()
        self.tableLayout.addWidget(self.table)
        # self.tableLayout.addSpacing(50)

        self.buttonHLayout = QHBoxLayout()
        self.buttonHLayout.addWidget(self.refreshRecordsBtn)
        self.buttonHLayout.addWidget(self.deepViewUpdateBtn)
        self.buttonHLayout.addWidget(self.exportToCSVBtn)
        self.buttonHLayout.addWidget(self.deleteSelectedRecord)
        self.mainLayoutTab2.addLayout(self.tableLayout)
        self.mainLayoutTab2.addLayout(self.buttonHLayout)

        self.setLayout(self.mainLayoutTab2)
        self.loadData()

    def deepViewWithBriefLayout(self):

        try:
            self.getRowForDeepView()

            selectedRowToDeepView = [self.field1, self.field2, self.field3, self.field4,
                  self.field5, self.field6, self.field7, self.field8, self.field9,
                  self.field10, self.field11, self.field12, self.field13, self.field14,
                  self.field15, self.field16, self.field17, self.field18, self.field19,
                  self.field20, self.field21, self.field22, self.field23, self.field24,
                  self.field25, self.field26, self.field27, self.field28, self.field29,
                  self.field30, self.field31, self.field32, self.field33, self.field34,
                  self.field35, self.field36, self.field37, self.field38, self.field39,
                  self.field40, self.field41, self.field42, self.field43]

            selectedRow =  self.selectedRow
            self.window2 = DeepViewUpdateWindow(selectedRowToDeepView)
            self.window2.show()
        except:
            pass

    def deleteRecord(self):
        # customMessage("Record Deleted")
        try:

            self.selectedRow = self.table.currentRow()


            self.field1 = self.table.item(self.selectedRow, 0).text()
            self.field2 = self.table.item(self.selectedRow, 1).text()

            self.databaseName = 'mvp31'
            self.databaseName = f'{self.databaseName}.db'
            self.tableName = 'MVP31'

            self.conn = sqlite3.connect(self.databaseName)
            self.c = self.conn.cursor()
            self.c.execute(f"""DELETE FROM {self.tableName} WHERE FileNo = '{self.field1}' """)

            self.conn.commit()
            self.table.removeRow(self.selectedRow)

            customMessage(f"Deleted {self.field1},{self.field2}")

        except:
            print('Please select the record you would like to delete')

    def loadData(self):

        ######################################################
        # new db
        ######################################################

        self.con = sqlite3.connect("mvp31.db")
        self.cur = self.con.cursor()
        self.query = "SELECT * FROM MVP31"
        self.cur.execute(self.query)

        self.table.setRowCount(100)
        tableRowIndex = 0
        for row in self.cur.execute(self.query):
            self.table.setItem(tableRowIndex, 0, QTableWidgetItem(row[0]))
            self.table.setItem(tableRowIndex, 1, QTableWidgetItem(row[1]))
            self.table.setItem(tableRowIndex, 2, QTableWidgetItem(row[2]))
            self.table.setItem(tableRowIndex, 3, QTableWidgetItem(row[3]))
            self.table.setItem(tableRowIndex, 4, QTableWidgetItem(row[4]))
            self.table.setItem(tableRowIndex, 5, QTableWidgetItem(row[5]))
            self.table.setItem(tableRowIndex, 6, QTableWidgetItem(row[6]))
            self.table.setItem(tableRowIndex, 7, QTableWidgetItem(row[7]))
            self.table.setItem(tableRowIndex, 8, QTableWidgetItem(row[8]))
            self.table.setItem(tableRowIndex, 9, QTableWidgetItem(row[9]))
            self.table.setItem(tableRowIndex, 10, QTableWidgetItem(row[10]))
            self.table.setItem(tableRowIndex, 11, QTableWidgetItem(row[11]))
            self.table.setItem(tableRowIndex, 12, QTableWidgetItem(row[12]))
            self.table.setItem(tableRowIndex, 13, QTableWidgetItem(row[13]))
            self.table.setItem(tableRowIndex, 14, QTableWidgetItem(row[14]))
            self.table.setItem(tableRowIndex, 15, QTableWidgetItem(row[15]))
            self.table.setItem(tableRowIndex, 16, QTableWidgetItem(row[16]))
            self.table.setItem(tableRowIndex, 17, QTableWidgetItem(row[17]))
            self.table.setItem(tableRowIndex, 18, QTableWidgetItem(row[18]))
            self.table.setItem(tableRowIndex, 19, QTableWidgetItem(row[19]))
            self.table.setItem(tableRowIndex, 20, QTableWidgetItem(row[20]))
            self.table.setItem(tableRowIndex, 21, QTableWidgetItem(row[21]))
            self.table.setItem(tableRowIndex, 22, QTableWidgetItem(row[22]))
            self.table.setItem(tableRowIndex, 23, QTableWidgetItem(row[23]))
            self.table.setItem(tableRowIndex, 24, QTableWidgetItem(row[24]))
            self.table.setItem(tableRowIndex, 25, QTableWidgetItem(row[25]))
            self.table.setItem(tableRowIndex, 26, QTableWidgetItem(row[26]))
            self.table.setItem(tableRowIndex, 27, QTableWidgetItem(row[27]))
            self.table.setItem(tableRowIndex, 28, QTableWidgetItem(row[28]))
            self.table.setItem(tableRowIndex, 29, QTableWidgetItem(row[29]))
            self.table.setItem(tableRowIndex, 30, QTableWidgetItem(row[30]))
            self.table.setItem(tableRowIndex, 31, QTableWidgetItem(row[31]))
            self.table.setItem(tableRowIndex, 32, QTableWidgetItem(row[32]))
            self.table.setItem(tableRowIndex, 33, QTableWidgetItem(row[33]))
            self.table.setItem(tableRowIndex, 34, QTableWidgetItem(row[34]))
            self.table.setItem(tableRowIndex, 35, QTableWidgetItem(row[35]))
            self.table.setItem(tableRowIndex, 36, QTableWidgetItem(row[36]))
            self.table.setItem(tableRowIndex, 37, QTableWidgetItem(row[37]))
            self.table.setItem(tableRowIndex, 38, QTableWidgetItem(row[38]))
            self.table.setItem(tableRowIndex, 39, QTableWidgetItem(row[39]))
            self.table.setItem(tableRowIndex, 40, QTableWidgetItem(row[40]))
            self.table.setItem(tableRowIndex, 41, QTableWidgetItem(row[41]))
            self.table.setItem(tableRowIndex, 42, QTableWidgetItem(row[42]))
            self.table.setItem(tableRowIndex, 43, QTableWidgetItem(row[43]))
            self.table.setItem(tableRowIndex, 44, QTableWidgetItem(row[44]))
            self.table.setItem(tableRowIndex, 45, QTableWidgetItem(row[45]))
            self.table.setItem(tableRowIndex, 46, QTableWidgetItem(row[46]))
            self.table.setItem(tableRowIndex, 47, QTableWidgetItem(row[47]))
            self.table.setItem(tableRowIndex, 48, QTableWidgetItem(row[48]))
            self.table.setItem(tableRowIndex, 49, QTableWidgetItem(row[49]))
            self.table.setItem(tableRowIndex, 50, QTableWidgetItem(row[50]))
            self.table.setItem(tableRowIndex, 51, QTableWidgetItem(row[51]))
            self.table.setItem(tableRowIndex, 52, QTableWidgetItem(row[52]))
            self.table.setItem(tableRowIndex, 53, QTableWidgetItem(row[53]))
            self.table.setItem(tableRowIndex, 54, QTableWidgetItem(row[54]))
            self.table.setItem(tableRowIndex, 55, QTableWidgetItem(row[55]))
            self.table.setItem(tableRowIndex, 56, QTableWidgetItem(row[56]))
            self.table.setItem(tableRowIndex, 57, QTableWidgetItem(row[57]))
            self.table.setItem(tableRowIndex, 58, QTableWidgetItem(row[58]))
            self.table.setItem(tableRowIndex, 59, QTableWidgetItem(row[59]))
            self.table.setItem(tableRowIndex, 60, QTableWidgetItem(row[60]))
            self.table.setItem(tableRowIndex, 61, QTableWidgetItem(row[61]))
            self.table.setItem(tableRowIndex, 62, QTableWidgetItem(row[62]))
            self.table.setItem(tableRowIndex, 63, QTableWidgetItem(row[63]))
            self.table.setItem(tableRowIndex, 64, QTableWidgetItem(row[64]))
            self.table.setItem(tableRowIndex, 65, QTableWidgetItem(row[65]))
            self.table.setItem(tableRowIndex, 66, QTableWidgetItem(row[66]))
            self.table.setItem(tableRowIndex, 67, QTableWidgetItem(row[67]))
            self.table.setItem(tableRowIndex, 68, QTableWidgetItem(row[68]))
            self.table.setItem(tableRowIndex, 69, QTableWidgetItem(row[69]))
            self.table.setItem(tableRowIndex, 70, QTableWidgetItem(row[70]))
            self.table.setItem(tableRowIndex, 71, QTableWidgetItem(row[71]))
            self.table.setItem(tableRowIndex, 72, QTableWidgetItem(row[72]))
            self.table.setItem(tableRowIndex, 73, QTableWidgetItem(row[73]))
            self.table.setItem(tableRowIndex, 74, QTableWidgetItem(row[74]))
            self.table.setItem(tableRowIndex, 75, QTableWidgetItem(row[75]))
            self.table.setItem(tableRowIndex, 76, QTableWidgetItem(row[76]))
            self.table.setItem(tableRowIndex, 77, QTableWidgetItem(row[77]))
            self.table.setItem(tableRowIndex, 78, QTableWidgetItem(row[78]))
            self.table.setItem(tableRowIndex, 79, QTableWidgetItem(row[79]))
            self.table.setItem(tableRowIndex, 80, QTableWidgetItem(row[80]))
            self.table.setItem(tableRowIndex, 81, QTableWidgetItem(row[81]))
            self.table.setItem(tableRowIndex, 82, QTableWidgetItem(row[82]))
            self.table.setItem(tableRowIndex, 83, QTableWidgetItem(row[83]))
            self.table.setItem(tableRowIndex, 84, QTableWidgetItem(row[84]))
            self.table.setItem(tableRowIndex, 85, QTableWidgetItem(row[85]))
            self.table.setItem(tableRowIndex, 86, QTableWidgetItem(row[86]))
            self.table.setItem(tableRowIndex, 87, QTableWidgetItem(row[87]))
            self.table.setItem(tableRowIndex, 88, QTableWidgetItem(row[88]))
            #

            tableRowIndex += 1

    def getRowForQuickView(self):

        try:
            self.selectedRow = self.table.currentRow()

            self.field1 = self.table.item(self.selectedRow, 0).text()
            self.field2 = self.table.item(self.selectedRow, 1).text()
            self.field3 = self.table.item(self.selectedRow, 2).text()
            self.field4 = self.table.item(self.selectedRow, 3).text()
            self.field5 = self.table.item(self.selectedRow, 4).text()
            self.field6 = self.table.item(self.selectedRow, 5).text()
            self.field7 = self.table.item(self.selectedRow, 6).text()
            self.field8 = self.table.item(self.selectedRow, 7).text()
            self.field9 = self.table.item(self.selectedRow, 8).text()
            self.field10 = self.table.item(self.selectedRow, 9).text()
            self.field11 = self.table.item(self.selectedRow, 10).text()
            self.field12 = self.table.item(self.selectedRow, 11).text()
            self.field13 = self.table.item(self.selectedRow, 12).text()
            self.field14 = self.table.item(self.selectedRow, 13).text()
            self.field15 = self.table.item(self.selectedRow, 14).text()
            self.field16 = self.table.item(self.selectedRow, 15).text()
            self.field17 = self.table.item(self.selectedRow, 16).text()
            self.field18 = self.table.item(self.selectedRow, 17).text()
            self.field19 = self.table.item(self.selectedRow, 18).text()
            self.field20 = self.table.item(self.selectedRow, 19).text()
            self.field21 = self.table.item(self.selectedRow, 20).text()
            self.field22 = self.table.item(self.selectedRow, 21).text()
            self.field23 = self.table.item(self.selectedRow, 22).text()
            self.field24 = self.table.item(self.selectedRow, 23).text()
            self.field25 = self.table.item(self.selectedRow, 24).text()
            self.field26 = self.table.item(self.selectedRow, 25).text()
            self.field27 = self.table.item(self.selectedRow, 26).text()
            self.field28 = self.table.item(self.selectedRow, 27).text()
            self.field29 = self.table.item(self.selectedRow, 28).text()
            self.field30 = self.table.item(self.selectedRow, 29).text()
            self.field31 = self.table.item(self.selectedRow, 30).text()
            self.field32 = self.table.item(self.selectedRow, 31).text()
            self.field33 = self.table.item(self.selectedRow, 32).text()
            self.field34 = self.table.item(self.selectedRow, 33).text()
            self.field35 = self.table.item(self.selectedRow, 34).text()
            self.field36 = self.table.item(self.selectedRow, 35).text()
            self.field37 = self.table.item(self.selectedRow, 36).text()
            self.field38 = self.table.item(self.selectedRow, 37).text()
            self.field39 = self.table.item(self.selectedRow, 38).text()
            self.field40 = self.table.item(self.selectedRow, 39).text()
            self.field41 = self.table.item(self.selectedRow, 40).text()
            self.field42 = self.table.item(self.selectedRow, 41).text()
            self.field43 = self.table.item(self.selectedRow, 42).text()

            self.displaySelectedRecords()
        except:
            customMessage('Please select a record to be displayed')

    def getRowForDeepView(self):

        try:
            self.selectedRow = self.table.currentRow()

            self.field1 = self.table.item(self.selectedRow, 0).text()
            self.field2 = self.table.item(self.selectedRow, 1).text()
            self.field3 = self.table.item(self.selectedRow, 2).text()
            self.field4 = self.table.item(self.selectedRow, 3).text()
            self.field5 = self.table.item(self.selectedRow, 4).text()
            self.field6 = self.table.item(self.selectedRow, 5).text()
            self.field7 = self.table.item(self.selectedRow, 6).text()
            self.field8 = self.table.item(self.selectedRow, 7).text()
            self.field9 = self.table.item(self.selectedRow, 8).text()
            self.field10 = self.table.item(self.selectedRow, 9).text()
            self.field11 = self.table.item(self.selectedRow, 10).text()
            self.field12 = self.table.item(self.selectedRow, 11).text()
            self.field13 = self.table.item(self.selectedRow, 12).text()
            self.field14 = self.table.item(self.selectedRow, 13).text()
            self.field15 = self.table.item(self.selectedRow, 14).text()
            self.field16 = self.table.item(self.selectedRow, 15).text()
            self.field17 = self.table.item(self.selectedRow, 16).text()
            self.field18 = self.table.item(self.selectedRow, 17).text()
            self.field19 = self.table.item(self.selectedRow, 18).text()
            self.field20 = self.table.item(self.selectedRow, 19).text()
            self.field21 = self.table.item(self.selectedRow, 20).text()
            self.field22 = self.table.item(self.selectedRow, 21).text()
            self.field23 = self.table.item(self.selectedRow, 22).text()
            self.field24 = self.table.item(self.selectedRow, 23).text()
            self.field25 = self.table.item(self.selectedRow, 24).text()
            self.field26 = self.table.item(self.selectedRow, 25).text()
            self.field27 = self.table.item(self.selectedRow, 26).text()
            self.field28 = self.table.item(self.selectedRow, 27).text()
            self.field29 = self.table.item(self.selectedRow, 28).text()
            self.field30 = self.table.item(self.selectedRow, 29).text()
            self.field31 = self.table.item(self.selectedRow, 30).text()
            self.field32 = self.table.item(self.selectedRow, 31).text()
            self.field33 = self.table.item(self.selectedRow, 32).text()
            self.field34 = self.table.item(self.selectedRow, 33).text()
            self.field35 = self.table.item(self.selectedRow, 34).text()
            self.field36 = self.table.item(self.selectedRow, 35).text()
            self.field37 = self.table.item(self.selectedRow, 36).text()
            self.field38 = self.table.item(self.selectedRow, 37).text()
            self.field39 = self.table.item(self.selectedRow, 38).text()
            self.field40 = self.table.item(self.selectedRow, 39).text()
            self.field41 = self.table.item(self.selectedRow, 40).text()
            self.field42 = self.table.item(self.selectedRow, 41).text()
            self.field43 = self.table.item(self.selectedRow, 42).text()


        except:
            customMessage('Please select a record to be displayed')

    def displaySelectedRecords(self):
        """Layout, labels and lineEdits that displays the table selection"""

        # Main Vertical Box Layout for Output Section
        self.mainQuickViewVboxLayout = QVBoxLayout()


        # Horizontal Line 1
        self.hboxLayoutLine1 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 1

        # File No
        self.fileNoLabel = QLabel('File No:')
        self.fileNoOutputLabel = QLabel(f'{self.field1}')

        # Company Name
        self.coNameLabel = QLabel('Company Name:')
        self.coNameOutputLabel = QLabel(f'{self.field2}')

        # Company Reg No
        self.coRegNoLabel = QLabel('Reg No:')
        self.coRegNoOutputLabel = QLabel(f'{self.field4}')

        # Company Old Name
        self.coOldNameLabel = QLabel('Company Old Name:')
        self.coOldNameOutputLabel = QLabel(f'{self.field3}')

        # Add Widgets to Horizontal Layout 1
        self.hboxLayoutLine1.addWidget(self.fileNoLabel)
        self.hboxLayoutLine1.addWidget(self.fileNoOutputLabel)
        self.hboxLayoutLine1.addWidget(self.coNameLabel)
        self.hboxLayoutLine1.addWidget(self.coNameOutputLabel)
        self.hboxLayoutLine1.addWidget(self.coRegNoLabel)
        self.hboxLayoutLine1.addWidget(self.coRegNoOutputLabel)
        self.hboxLayoutLine1.addWidget(self.coOldNameLabel)
        self.hboxLayoutLine1.addWidget(self.coOldNameOutputLabel)
        #----------------------------------------------------------------------------------------------------

        self.hboxLayoutLine2 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 2

        # Date of Change
        self.dateOfChangeLabel = QLabel('Name Changed:')
        self.dateOfChangeOutputLabel = QLabel(f'{self.field5}')

        # Incorporated Date
        self.incorporatedDateLabel = QLabel('Inc:')
        self.incorporatedDateOutputLabel = QLabel(f'{self.field6}')

        # Company Type
        self.companyTypeLabel = QLabel('Type:')
        self.companyTypeOutputLabel = QLabel(f'{self.field7}')

        # Company Status
        self.companyStatusLabel = QLabel('Status:')
        self.companyStatusOutputLabel = QLabel(f'{self.field8}')

        # Add Widgets to Horizontal Layout 2
        self.hboxLayoutLine2.addWidget(self.dateOfChangeLabel)
        self.hboxLayoutLine2.addWidget(self.dateOfChangeOutputLabel)
        self.hboxLayoutLine2.addWidget(self.incorporatedDateLabel)
        self.hboxLayoutLine2.addWidget(self.incorporatedDateOutputLabel)
        self.hboxLayoutLine2.addWidget(self.companyTypeLabel)
        self.hboxLayoutLine2.addWidget(self.companyTypeOutputLabel)
        self.hboxLayoutLine2.addWidget(self.companyStatusLabel)
        self.hboxLayoutLine2.addWidget(self.companyStatusOutputLabel)

        #---------------------------------------------------------------------------------
        self.hboxLayoutLine3 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 3

        # Registered Address
        self.registeredAddressLabel = QLabel('Reg Add:')
        self.registeredAddressOutputLabel = QLabel(f'{self.field9}')

        # Add Widgets to Horizontal Layout 1
        self.hboxLayoutLine3.addWidget(self.registeredAddressLabel)
        self.hboxLayoutLine3.addWidget(self.registeredAddressOutputLabel)

        #---------------------------------------------------------------------------------
        self.hboxLayoutLine4 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 4

        # Business Address
        self.businessAddressLabel = QLabel('Bus Add:')
        self.businessAddressOutputLabel = QLabel(f'{self.field10}')

        # Add Widgets to Horizontal Layout 1
        self.hboxLayoutLine4.addWidget(self.businessAddressLabel)
        self.hboxLayoutLine4.addWidget(self.businessAddressOutputLabel)
        #----------------------------------------------------------------------------------------------------
        self.hboxLayoutLine5 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 5

        # Nature of Business
        self.natureOfBusinessLabel = QLabel('Nature of Business:')
        self.natureOfBusinessOutputLabel = QLabel(f'{self.field11}')

        # Paid Up Capital
        self.paidUpCapitalLabel = QLabel('Paid Up Capital:')
        self.paidUpCapitalOutputLabel = QLabel(f'{self.field12}')

        # Add Widgets to Horizontal Layout 1
        self.hboxLayoutLine5.addWidget(self.natureOfBusinessLabel)
        self.hboxLayoutLine5.addWidget(self.natureOfBusinessOutputLabel)
        self.hboxLayoutLine5.addWidget(self.paidUpCapitalLabel)
        self.hboxLayoutLine5.addWidget(self.paidUpCapitalOutputLabel)

        #----------------------------------------------------------------------------------------------------
        self.hboxLayoutLine6 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 6
        # Members (Each Member may require a horizontal line

        # Member 1
        self.member1Label = QLabel('Member 1:')
        self.member1OutputLabel = QLabel(f'{self.field13}')
        # Member 1 Shares
        self.member1SharesLabel = QLabel('Shares:')
        self.member1SharesOutputLabel = QLabel(f'{self.field18}') # Need to check if this is the correct field or is it the field for Member 2 Name

        # Add Widgets to Horizontal Layout 6
        # Member1 Layout
        self.hboxLayoutLine6.addWidget(self.member1Label)
        self.hboxLayoutLine6.addWidget(self.member1OutputLabel)
        # Member1 Shares Layout
        self.hboxLayoutLine6.addWidget(self.member1SharesLabel)
        self.hboxLayoutLine6.addWidget(self.member1SharesOutputLabel)


        self.hboxLayoutLine7 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 7

        # Member 2
        self.member2Label = QLabel('Member 2:')
        self.member2OutputLabel = QLabel(f'{self.field14}')
        # Member 2 Shares
        self.member2SharesLabel = QLabel('Shares:')
        self.member2SharesOutputLabel = QLabel(f'{self.field19}')

        # Add Widgets to Horizontal Layout 7
        # Member2 Layout
        self.hboxLayoutLine7.addWidget(self.member2Label)
        self.hboxLayoutLine7.addWidget(self.member2OutputLabel)
        # Member2 Shares Layout
        self.hboxLayoutLine7.addWidget(self.member2SharesLabel)
        self.hboxLayoutLine7.addWidget(self.member2SharesOutputLabel)

        self.hboxLayoutLine8 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 8

        # Member 3
        self.member3Label = QLabel('Member 3:')
        self.member3OutputLabel = QLabel(f'{self.field15}')
        # Member 3 Shares
        self.member3SharesLabel = QLabel('Shares:')
        self.member3SharesOutputLabel = QLabel(f'{self.field20}')

        # Add Widgets to Horizontal Layout 8
        # Member3 Layout
        self.hboxLayoutLine8.addWidget(self.member3Label)
        self.hboxLayoutLine8.addWidget(self.member3OutputLabel)
        # Member3 Shares Layout
        self.hboxLayoutLine8.addWidget(self.member3SharesLabel)
        self.hboxLayoutLine8.addWidget(self.member3SharesOutputLabel)

        self.hboxLayoutLine9 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 9


        # Member 4
        self.member4Label = QLabel('Member 4:')
        self.member4OutputLabel = QLabel(f'{self.field16}')
        # Member 4 Shares
        self.member4SharesLabel = QLabel('Shares:')
        self.member4SharesOutputLabel = QLabel(f'{self.field21}')

        # Add Widgets to Horizontal Layout 9
        # Member4 Layout
        self.hboxLayoutLine9.addWidget(self.member4Label)
        self.hboxLayoutLine9.addWidget(self.member4OutputLabel)
        # Member4 Shares Layout
        self.hboxLayoutLine9.addWidget(self.member4SharesLabel)
        self.hboxLayoutLine9.addWidget(self.member4SharesOutputLabel)


        self.hboxLayoutLine10 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 10

        # Member 5
        self.member5Label = QLabel('Member 5:')
        self.member5OutputLabel = QLabel(f'{self.field17}')
        # Member 5 Shares
        self.member5SharesLabel = QLabel('Shares:')
        self.member5SharesOutputLabel = QLabel(f'{self.field22}')


        # Add Widgets to Horizontal Layout 10
        # Member5 Layout
        self.hboxLayoutLine10.addWidget(self.member5Label)
        self.hboxLayoutLine10.addWidget(self.member5OutputLabel)
        # Member5 Shares Layout
        self.hboxLayoutLine10.addWidget(self.member5SharesLabel)
        self.hboxLayoutLine10.addWidget(self.member5SharesOutputLabel)


        #____________________________________________________________________________________________________
        self.hboxLayoutLine11 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 11

        # Director 1
        self.director1NameLabel = QLabel('Director 1:')
        self.director1NameOutputLabel = QLabel(f'{self.field17}')

        # Director 2
        self.director2NameLabel = QLabel('Director 2:')
        self.director2NameOutputLabel = QLabel(f'{self.field22}')


        # Add Widgets to Horizontal Layout 11
        # Director 1 Layout
        self.hboxLayoutLine11.addWidget(self.director1NameLabel)
        self.hboxLayoutLine11.addWidget(self.director1NameOutputLabel)

        # Director 2 Layout
        self.hboxLayoutLine11.addWidget(self.director2NameLabel)
        self.hboxLayoutLine11.addWidget(self.director2NameOutputLabel)


        self.hboxLayoutLine12 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 12
        # Secretary 1 Name
        self.secretary1Label = QLabel('Secretary 1:')
        self.secretary1OutputLabel = QLabel(f'{self.field17}')

        self.hboxLayoutLine12.addWidget(self.secretary1Label)
        self.hboxLayoutLine12.addWidget(self.secretary1OutputLabel)

        self.hboxLayoutLine13 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 13

        # Secretary 1 Appointed Date
        self.sec1AppointedDateLabel = QLabel('Appointed Date:')
        self.sec1AppointedDateOutputLabel = QLabel(f'{self.field17}')

        # Secretary 1 Resigned Date
        self.sec1ResignedDateLabel = QLabel('Resigned Date:')
        self.sec1ResignedDateOutputLabel = QLabel(f'{self.field17}')

        # Secretary 1 Vacated Date
        self.sec1VacatedDateLabel = QLabel('Vacated Date:')
        self.sec1VacatedDateOutputLabel = QLabel(f'{self.field17}')

        self.hboxLayoutLine13.addWidget(self.sec1AppointedDateLabel)
        self.hboxLayoutLine13.addWidget(self.sec1AppointedDateOutputLabel)
        self.hboxLayoutLine13.addWidget(self.sec1ResignedDateLabel)
        self.hboxLayoutLine13.addWidget(self.sec1ResignedDateOutputLabel)
        self.hboxLayoutLine13.addWidget(self.sec1VacatedDateLabel)
        self.hboxLayoutLine13.addWidget(self.sec1VacatedDateOutputLabel)


        self.hboxLayoutLine14 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 14
        # Secretary 2 Name
        self.secretary2Label = QLabel('Secretary 2:')
        self.secretary2OutputLabel = QLabel(f'{self.field17}')

        self.hboxLayoutLine14.addWidget(self.secretary2Label)
        self.hboxLayoutLine14.addWidget(self.secretary2OutputLabel)

        self.hboxLayoutLine15 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 15
        # Secretary 2 Appointed Date
        self.sec2AppointedDateLabel = QLabel('Appointed Date:')
        self.sec2AppointedDateOutputLabel = QLabel(f'{self.field17}')

        # Secretary 2 Resigned Date
        self.sec2ResignedDateLabel = QLabel('Resigned Date:')
        self.sec2ResignedDateOutputLabel = QLabel(f'{self.field17}')

        # Secretary 2 Vacated Date
        self.sec2VacatedDateLabel = QLabel('Vacated Date:')
        self.sec2VacatedDateOutputLabel = QLabel(f'{self.field17}')

        self.hboxLayoutLine15.addWidget(self.sec2AppointedDateLabel)
        self.hboxLayoutLine15.addWidget(self.sec2AppointedDateOutputLabel)
        self.hboxLayoutLine15.addWidget(self.sec2ResignedDateLabel)
        self.hboxLayoutLine15.addWidget(self.sec2ResignedDateOutputLabel)
        self.hboxLayoutLine15.addWidget(self.sec2VacatedDateLabel)
        self.hboxLayoutLine15.addWidget(self.sec2VacatedDateOutputLabel)



        self.hboxLayoutLine16 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 16
        # Contact Person
        self.contactPersonNameLabel = QLabel('Contact Person:')
        self.contactPersonNameOutputLabel = QLabel(f'{self.field19}')

        # Contact Tel
        self.contactTelLabel = QLabel('Phone:')
        self.contactTelOutputLabel = QLabel(f'{self.field19}')

        # Contact Email
        self.contactEmailLabel = QLabel('Email:')
        self.contactEmailOutputLabel = QLabel(f'{self.field19}')

        # Contact Layout
        self.hboxLayoutLine16.addWidget(self.contactPersonNameLabel)
        self.hboxLayoutLine16.addWidget(self.contactPersonNameOutputLabel)
        self.hboxLayoutLine16.addWidget(self.contactTelLabel)
        self.hboxLayoutLine16.addWidget(self.contactTelOutputLabel)
        self.hboxLayoutLine16.addWidget(self.contactEmailLabel)
        self.hboxLayoutLine16.addWidget(self.contactEmailOutputLabel)





        self.hboxLayoutLine17 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 17

        # Prepared By
        self.preparedByLabel = QLabel('Prepared By:')
        self.preparedByOutputLabel = QLabel(f'{self.field19}')

        # Prepared Date
        self.preparedDateLabel = QLabel('Prepared Date:')
        self.preparedDateOutputLabel = QLabel(f'{self.field19}')

        # Prepared By and Prepared Date Layout
        self.hboxLayoutLine17.addWidget(self.preparedByLabel)
        self.hboxLayoutLine17.addWidget(self.preparedByOutputLabel)
        self.hboxLayoutLine17.addWidget(self.preparedDateLabel)
        self.hboxLayoutLine17.addWidget(self.preparedDateOutputLabel)



        self.hboxLayoutLine18 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 18
        # Scanned By
        self.scannedByLabel = QLabel('Scanned By:')
        self.scannedByOutputLabel = QLabel(f'{self.field19}')

        # Scanned Date
        self.scannedDateLabel = QLabel('Scanned Date:')
        self.member2SharesOutputLabel = QLabel(f'{self.field19}')

        # SCanned By & Scanned Date Layout
        self.hboxLayoutLine18.addWidget(self.scannedByLabel)
        self.hboxLayoutLine18.addWidget(self.scannedByOutputLabel)
        self.hboxLayoutLine18.addWidget(self.scannedDateLabel)
        self.hboxLayoutLine18.addWidget(self.member2SharesOutputLabel)

        self.hboxLayoutLine19 = QHBoxLayout() #-------------------------------------------- Hrizontal Layout 19

        # Checked By
        self.checkedByLabel = QLabel('Checked By:')
        self.checkedByOutputLabel = QLabel(f'{self.field19}')

        # Checked Date
        self.checkedDateLabel = QLabel('Checked Date:')
        self.checkedDateOutputLabel = QLabel(f'{self.field19}')

        # Checked By & Checked Date Layout
        self.hboxLayoutLine19.addWidget(self.checkedByLabel)
        self.hboxLayoutLine19.addWidget(self.checkedByOutputLabel)
        self.hboxLayoutLine19.addWidget(self.checkedDateLabel)
        self.hboxLayoutLine19.addWidget(self.checkedDateOutputLabel)

        # Add HBox Text Layouts (Horizontal Lines) Layouts to main/QuickView Section's VBox layout
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine1)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine2)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine3)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine4)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine5)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine6)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine7)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine8)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine9)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine10)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine11)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine12)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine13)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine14)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine15)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine16)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine17)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine18)
        self.mainQuickViewVboxLayout.addLayout(self.hboxLayoutLine19)

        # Vertical spacing between show record button and the bottom of widget
        self.mainQuickViewVboxLayout.addSpacing(20)

        # Add VBox to Main Layout
        self.mainLayoutTab2.addLayout(self.mainQuickViewVboxLayout)

    def exportToCSVFunction(self):

        ######################################################
        # new db
        ######################################################

        self.tableName = 'MVP31'
        sqlite_db = sqlite3.connect('mvp31.db')
        df = pd.read_sql_query(f""" SELECT * FROM {self.tableName}""", sqlite_db)

        df.to_excel(f'{self.tableName}.xlsx')


