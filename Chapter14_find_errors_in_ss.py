import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')  # create SS object with google SS ID
print(ss.sheets)
sheet = ezsheets.Sheet(spreadsheet=ss, sheetId=289119951)  # get sheet using sheetID
i = 1
rows = sheet.getRows()  # get rows from sheet
while list(filter(None, rows[i])):  # while row not empty
	if int(rows[i][0]) * int(rows[i][1]) != int(rows[i][2]):
		print(f"{i} string has error: {int(rows[i][0])} * {int(rows[i][1])} = {int(rows[i][0]) * int(rows[i][1])} table value is:  {int(rows[i][2])}")
		break
	i += 1

def tst(a):
	"""
	:param a:
	:return:
	"""