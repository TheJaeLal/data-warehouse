import openpyxl,sys

file_name = ""

if len(sys.argv)==1:
    print(">>> Error Please specify the source excel file...")
    exit(0)
else:
    file_name = sys.argv[1].strip()

excel_workbook = openpyxl.load_workbook(file_name)

faculty_sheet = excel_workbook.get_sheet_by_name('Sheet1')
student_sheet = excel_workbook.get_sheet_by_name('Sheet2')

for k,my_sheet in enumerate([faculty_sheet,student_sheet]):
    print("*********Sheet",k,"*********",end = "\n")
    for i in range(1,10):
        for j in range(1,30):
            current_cell = my_sheet.cell(row = i, column = j).value
            if current_cell==None:
                print("",end = "  ")
            else:
                print(current_cell,end = " ")
        print("")
        

