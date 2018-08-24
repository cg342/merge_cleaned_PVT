import csv
from dbfpy import dbf
import os
import xlrd
import glob

path = "/home/pwm4/Desktop/cg342/cleaned_raw_comparison/PVT/redo/clean/cleaned_data/dbf/"
csv_path = "/home/pwm4/Desktop/cg342/cleaned_raw_comparison/PVT/redo/clean/cleaned_data/dbf_csv/"

allfiles = glob.glob(path + "*.DBF")

for filepath in allfiles:
##    print(filepath)
#    
    filename = os.path.basename(os.path.splitext(filepath)[0])
##    print filename
    csv_file_name = csv_path + filename+ ".csv"
#    print csv_file_name
    with open(csv_file_name,'wb') as csvfile:
        in_db = dbf.Dbf(filepath)
        out_csv = csv.writer(csvfile)
        names = []
        for field in in_db.header.fields:
           names.append(field.name)
        out_csv.writerow(names)
        for rec in in_db:
           out_csv.writerow(rec.fieldData)
        print(filename)
        in_db.close()

###################
#mainpath = r"/home/pwm4/Desktop/cg342/cleaned_raw_comparison/KSS/KSS_cleaned/KSS_cleaned_data/DBF/"
#csv_path = r"/home/pwm4/Desktop/cg342/cleaned_raw_comparison/KSS/KSS_cleaned/KSS_cleaned_csv/"

#for dirpath, dirnames, filenames in os.walk(mainpath):
#    
#    for filename in filenames:
##      print("filename ", filename)
#      if filename.endswith('.DBF'):
#        filepath = mainpath + filename
#        name_stripped = os.path.basename(os.path.splitext(filepath)[0])
#        file_to_write = csv_path + name_stripped + ".csv"
#        with open(file_to_write,'wb') as csvfile:
##            print(filepath)
##            print("csvpath is:  \n" + file_to_write)             
#            print("filepath is .....", filepath)
#            in_db = dbf.Dbf(filepath)
##             
##            out_csv = csv.writer(csvfile)
##            names = []
##            for field in in_db.header.fields:
##                names.append(field.name)
##            out_csv.writerow(names)
##            for rec in in_db:
##                out_csv.writerow(rec.fieldData)
##            in_db.close()
##            print("done")

