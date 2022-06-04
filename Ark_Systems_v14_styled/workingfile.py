RegNO = '{self.RegNO}',
DateOfChange = '{self.DateOfChange}',
IncDate = '{self.IncDate}',
CoType = '{self.CoType}',
CoStatus = '{self.CoStatus}',
RegisteredAdd = '{self.RegisteredAdd}',
BusinessAdd = '{self.BusinessAdd}',
NatureOfBusiness = '{self.NatureOfBusiness}',
PaidUpCapital = '{self.PaidUpCapital}',
Member1 = '{self.Member1}',
Member1_Shares = '{self.Member1_Shares}',
Member2 = '{self.Member2}',
Member2_Shares = '{self.Member2_Shares}',
Member3 = '{self.Member3}',
Member3_Shares = '{self.Member3_Shares}',
Member4 = '{self.Member4}',
Member4_Shares = '{self.Member4_Shares}',
Member5 = '{self.Member5}',
Member5_Shares = '{self.Member5_Shares}',
Director1 = '{self.Director1}',
Director2 = '{self.Director2}',
Secretaries1 = '{self.Secretaries1}',
Sec1_Appointed_Date = '{self.Secretaries1AppointedDate}',
Sec1_Resigned_Date = '{self.Secretaries1ResignedDate}',
Sec1_Vacated_Date = '{self.Secretaries1VacatedDate}',
Secretaries2 = '{self.Secretaries2}',
Sec2_Appointed_Date = '{self.Secretaries2AppointedDate}',
Sec2_Resigned_Date = '{self.Secretaries2ResignedDate}',
Sec2_Vacated_Date = '{self.Secretaries2VacatedDate}',
ContactPerson = '{self.ContactPerson}',
ContactPersonTel = '{self.ContactPersonTel}',
ContactPersonEmail = '{self.ContactPersonEmail}',
PreparedBy = '{self.PreparedBy}',
PreparedDate = '{self.PreparedDate}',
ScannedBy = '{self.ScannedBy}',
ScannedDate = '{self.ScannedDate}',
CheckedBy = '{self.CheckedBy}',
CheckedDate = '{self.CoType}'







import os
docFolderNameList = ['Directors_Circular', 'Members_Meeting', 'Register', 'Share_Certificate', 'Summary',
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

print(f'docFolderNameList: {len(docFolderNameList)}')



list4 = ['_Directors_Circular','_Members_Meeting','_Register','_Share_Certificate','_Summary','_Checklist',
         '_Correspondence','_Bill_SOA','_SSM_Receipt','_Application_Of_Reg','_Availability_Names_Reg','_Application_Change_Name','_Lodgement_Constitution',
         '_Notify_Alteration_Amendment','_Change_Reg_Add','_Not_at_Reg_Add','_Change_Add_Reg_Are_Kept','_Change_Reg_of_Members',
         '_Change_Reg_Dir_Mgr_Sec','_Annual_Return_of_Company','_Approval_for_Allotment','_Return_for_Allotment',
         '_Variation_Class_of_Rights','_Instrument_of_Transfer','_Solvency_Statement','_Declaration_Appnt_as_Director',
         '_Notice_Contract_Serv_Director','_Declaration_Appnt_as_Secretary','_Vacate_Office_of_Secretary','_Dec_by_Sec_to_Cease_Off',
         '_Reg_to_Act_as_Sec','_Diff_Accounting_Periods','_EOT_Financial_Statements','_Exempt_Private_Company','_Lodge_with_Charge',
         '_Series_of_Debentures','_Assignment_of_Charge','_Variations_Terms_of_Change','_Property_Undertaking_Memo',
         '_Memo_Satisfaction_Reg_Charge','_Dec_Verifying_Memo','_Satisfaction_of_Charge','_Strike_of_Company',
         '_Object_Striking_of_Company','_Withdraw_Striking_of_Company','_Change_in_Bus_Add_or_Nat_of_Bus','_Miscellaneous_1',
         '_Temporary_Folder']

print(f'List4: {len(list4)}')


list = ['File No', 'Company Name', 'Co Old Name', 'Reg No', 'Date of Change', 'Inc Date', 'Co Type',
        'Co Status', 'Reg Address', 'Business Add', 'Nature of Bus', 'Paid Up Capital', 'Member 1',
        'Shares', 'Member 2', 'Shares', 'Member 3', 'Shares', 'Member 4', 'Shares', 'Member 5', 'Shares',
        'Director 1', 'Director 2', 'Secretaries 1', 'Secretaries 2', 'Contact Name', 'Contact Tel',
        'Contact Email', 'Appointed Date', 'Resigned Date', 'Vacated Date', 'Prepared By', 'Prepared Date',
        'Scanned By', 'Scanned Date', 'Checked By', 'Checked Date', 'Directors Circular', 'Members Meeting',
        'Register', 'Share Certificate', 'Summary', 'Checklist', 'Correspondence', 'Bill SOA', 'SSM Receipt',
        'Application Of Reg', 'Availability Names Reg', 'Application Change Name', 'Lodgement Constitution',
        'Notify Alteration Amendment', 'Change Reg Add', 'Not at Reg Add', 'Change Add Reg Are Kept',
        'Change Reg of Members', 'Change Reg Dir Mgr Sec', 'Annual Return of Company', 'Approval for Allotment',
        'Return for Allotment', 'Variation Class of Rights', 'Instrument of Transfer', 'Solvency Statement',
        'Declaration Appnt as Director', 'Notice Contract Serv Director', 'Declaration Appnt as Secretary',
        'Vacate Office of Secretary', 'Dec by Sec to Cease Off', 'Reg to Act as Sec', 'Diff Accounting Periods',
        'EOT Financial Statements', 'Exempt Private Company', 'Lodge with Charge', 'Series of Debentures',
        'Assignment of Charge', 'Variations Terms of Change', 'Property Undertaking Memo', 'Memo Satisfaction Reg Charge',
        'Dec Verifying Memo', 'Satisfaction of Charge', 'Strike of Company', 'Object Striking of Company',
        'Withdraw Striking of Company', 'Change in Bus Add or Nat of Bus', 'Miscellaneous 1', 'Temporary Folder']


print(len(list))


list2 = ['Members_Meeting', 'Register', 'Share_Certificate', 'Summary',
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


print(f'List2 Count:{len(list2)}')

list3 = ['Members Meeting', 'Register', 'Share Certificate', 'Summary', 'Checklist', 'Correspondence', 'Bill SOA', 'SSM Receipt', 'Application Of Reg', 'Availability Names Reg', 'Application Change Name', 'Lodgement Constitution', 'Notify Alteration Amendment', 'Change Reg Add', 'Not at Reg Add', 'Change Add Reg Are Kept', 'Change Reg of Members', 'Change Reg Dir Mgr Sec', 'Annual Return of Company', 'Approval for Allotment', 'Return for Allotment', 'Variation Class of Rights', 'Instrument of Transfer', 'Solvency Statement', 'Declaration Appnt as Director', 'Notice Contract Serv Director', 'Declaration Appnt as Secretary', 'Vacate Office of Secretary', 'Dec by Sec to Cease Off', 'Reg to Act as Sec', 'Diff Accounting Periods', 'EOT Financial Statements', 'Exempt Private Company', 'Lodge with Charge', 'Series of Debentures', 'Assignment of Charge', 'Variations Terms of Change', 'Property Undertaking Memo', 'Memo Satisfaction Reg Charge', 'Dec Verifying Memo', 'Satisfaction of Charge', 'Strike of Company', 'Object Striking of Company', 'Withdraw Striking of Company', 'Change in Bus Add or Nat of Bus', 'Miscellaneous 1', 'Temporary Folder']

for i in list2:
        new = i.replace('_', ' ')
        list3.append(new)

print(list3)

print(f'List1 Count:{len(list)}')
print(f'List2 Count:{len(list2)}')
print(f'Corp Brief: {(len(list))-(len(list2))}')






"""
"Remember, the fileFolder name is fine for the for loop, 
we just need to change the file folder name to the stackedwidget title,
by removing the underscore. This is to be used as the instance parameter
for the Filing System Instance/Object constructor FilingSystem(xxxx)."

editedFolderList = []

def editFileFolderName(editedFolderName):

    folderList = ['Directors_Circular', 'Members_Meeting', 'Register', 'Share_Certificate', 'Summary',
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
                             'Dec Verifying Memo', 'Satisfaction_of_Charge', 'Strike_of_Company', 'Object_Striking_of_Company',
                             'Withdraw_Striking_of_Company', 'Change_in_Bus_Add_or_Nat_of_Bus', 'Miscellaneous_1', 'Temporary']

    for fileFolderName in folderList:

        title_list = fileFolderName.split('_')


        title_len = (len(title_list))
        if (title_len) == 1:
            title1 = fileFolderName.split('_')[0]
            # print(f'{title1} Folder')
            editedFolderName = (f'{title1} Folder')
            # editedFolderList.append(editedFolderName)



        elif (title_len) == 2:
            title1 = fileFolderName.split('_')[0]
            title2 = fileFolderName.split('_')[1]
            # print(f'{title1} {title2} Folder')
            editedFolderName = (f'{title1} {title2} Folder')
            # editedFolderList.append(editedFolderName)


        elif (title_len) == 3:
            title1 = fileFolderName.split('_')[0]
            title2 = fileFolderName.split('_')[1]
            title3 = fileFolderName.split('_')[2]
            # print(f'{title1} {title2} {title3} Folder')
            editedFolderName = (f'{title1} {title2} {title3} Folder')
            # editedFolderList.append(editedFolderName)
        return editedFolderName

    # elif (title_len) == 4:
    #     title1 = fileFolderName.split('_')[0]
    #     title2 = fileFolderName.split('_')[1]
    #     title3 = fileFolderName.split('_')[2]
    #     title4 = fileFolderName.split('_')[3]
    #     # print(f'{title1} {title2} {title3} {title4} Folder')
    #     folderList.append(f'{title1} {title2} {title3} {title4} Folder')

    # elif (title_len) == 5:
    #     title1 = fileFolderName.split('_')[0]
    #     title2 = fileFolderName.split('_')[1]
    #     title3 = fileFolderName.split('_')[2]
    #     title4 = fileFolderName.split('_')[3]
    #     title5 = fileFolderName.split('_')[4]
    #     # print(f'{title1} {title2} {title3} {title4} {title5} Folder')
    #     folderList.append(f'{title1} {title2} {title3} {title4} {title5} Folder')



# print(editedFolderList)












    # fileFolderListFieldName = fileFolderName.split('_')
    # fileFolderListFieldName = (f'{fileFolderListFieldName[1]}_{fileFolderListFieldName[2]}')
    # print(f'File Folder List Field Name: {fileFolderListFieldName}')

uploadFileFolderList()
"""