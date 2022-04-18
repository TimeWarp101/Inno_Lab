import csv
import openpyxl
from pathlib import Path

xlsx_file = Path('BlockTimestampInfo.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file) 

sheet = wb_obj.active
timestamps = {}
for row in sheet.iter_rows():
    timestamps[row[0].value] = row[1].value

file = open("dataset.csv")
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
file.close()

f = open('Simplified_Dataset.csv', 'w', newline = "")
writer = csv.writer(f)

headers = []
headers.append('Block Number')
headers.append('Source')
headers.append('Target')
headers.append('Amount')
headers.append('Time Stamp')
writer.writerow(headers)

for row in rows:
    if row[1] == "Success" and row[2][0] == '1' and float(row[6]) > 0:
        new_row = []
        new_row.append(row[2])
        new_row.append(row[4])
        new_row.append(row[5])
        new_row.append(row[6])
        new_row.append(timestamps[int(row[2])])
        writer.writerow(new_row)

