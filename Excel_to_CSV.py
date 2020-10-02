# A single Excel file might contain multiple sheets; you’ll have to create one CSV file per sheet.
# The filenames of the CSV files should be <excel filename>_<sheet title>.csv, where <excel filename>
# the filename of the Excel file without the file extension (for example, 'spam_data', not 'spam_data.xlsx')
# and <sheet title> is the string from the Worksheet object’s title variable.

import os, csv, openpyxl, pathlib, sys


def excel_reader(excel_file_path):
    """
    Reads excel file, row by row, returns contents
    :param excel_file_path: path to excel file
    :return: data - dict: keys = sheet titles, values = list of lists (list of rows)
             excel_file_name - name of the file
    """
    data = {}
    wb = openpyxl.load_workbook(excel_file_path)
    excel_file_name = pathlib.Path(excel_file_path).stem
    for i in range(len(wb.sheetnames)):  # loop through sheets indices
        sheet_data = []
        wb.active = i  # make current sheet active
        sheet = wb.active
        for row in sheet.rows:  # loop trough rows
            row_data = []
            for cell in row:  # loop through cells
                row_data.append(cell.value)
            sheet_data.append(row_data)
        data[sheet.title] = sheet_data
    return data, excel_file_name


def csv_writer(excel_reader_data, excel_file_name):
    """
    Makes a new csv file(s) out of data provided by excel_reader()
    :param excel_reader_data: dict: keys = sheet titles, values = list of lists (list of rows)
    :return:
    """
    if not excel_reader_data:
        print("Empty data, exiting")
        return None
    os.makedirs(f"{excel_file_name}", exist_ok=True)  # create dir for the csv files to not make a mess in cwd
    for sheet in excel_reader_data.keys():  # go through sheets, write sheet - > .csv
        writer = csv.writer(open(f".\\{excel_file_name}\\{excel_file_name}_{sheet}.csv", mode="w+"))
        for row in excel_reader_data[sheet]:
            writer.writerow(row)


if len(sys.argv) < 2:
    excel_path = input("No arguments were passed to the script, please input a string of the path\nWhere .xlsx files that need to be converted to .csv are located\n")
else:
    excel_path = sys.argv[2]

if not pathlib.Path(excel_path).exists():
    print("Invalid path was provided, cannot find it, exiting")
    sys.exit("Path error")

for excel_file in pathlib.Path(excel_path).glob("*.xlsx"):
    csv_writer(*excel_reader(pathlib.Path(excel_file)))


#csv_writer(*excel_reader(r"C:\Users\yaizk\PycharmProjects\coursera_l2\Practice Python\Automating_boring_stuff\book exercises\CSV\Excel_to_CSV\excelSpreadsheets\spreadsheet-A.xlsx"))
