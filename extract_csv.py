import sys

file_name = ""

if len(sys.argv)==1:
    print(">>> Error Please specify the source excel file...")
    exit(0)
else:
    file_name = sys.argv[1].strip()
    
csv_file = open(file_name,'r')

lines = csv_file.read().split('\n')

for line in lines:
    row = line.split(',')
    if row:
        for entry in row:
            print(entry,end = "  ")
        print(" ")
    else:
        print("\n********************\n")

