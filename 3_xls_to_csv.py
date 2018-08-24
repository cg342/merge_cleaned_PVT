import xlrd
import csv
import glob
import os

mypath = "/home/pwm4/Desktop/cg342/cleaned_raw_comparison/PVT/redo/clean/cleaned_data/PVTALL-FEV/"
allfiles = glob.glob(mypath+"*.xls")
writetopath="/home/pwm4/Desktop/cg342/cleaned_raw_comparison/PVT/redo/clean/cleaned_data/PVTALL-FEV_csv/"

for filepath in allfiles:
#    print filepath
    wb = xlrd.open_workbook(filepath)
    sh = wb.sheet_by_name('PVTALL-FEV')
    filename = os.path.basename(os.path.splitext(filepath)[0])
    newfilepath = writetopath + filename + '.csv'
   
    your_csv_file = open(newfilepath, 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    print(newfilepath)

    your_csv_file.close()





