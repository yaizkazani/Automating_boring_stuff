import ezsheets

myss = ezsheets.Spreadsheet("1rQy_naW3iWzvSgOS9_9bjGZoNa5p_f4bIDhYdSREINQ")
mysheet = ezsheets.Sheet(spreadsheet=myss, sheetId=532309872)
sheet_title = mysheet.title
sheet_google_form_name = mysheet["B1"]
emails = []
print(f"rowcount is: {mysheet.rowCount}")
print(f"columncount is {mysheet.columnCount}")
i = 2
while mysheet[2, i]:
    emails.append(mysheet[2, i])
    i += 1
emails.clear()
for email in mysheet.getColumn(2)[1:]:
    emails.append(email) if email else ""
myss.downloadAsPDF("Sheet_in_PDF.pdf")