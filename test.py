# test 5_merge.py

# merge the csv files by columns
# adding the csv columns into a dictionary by column name
# create a new csv file for the dictionary

#import csv
import unicodecsv as csv
from collections import defaultdict
from collections import OrderedDict
import glob
import codecs
try:
    # Python 3
    from itertools import zip_longest
except ImportError:
    # Python 2
    from itertools import izip_longest as zip_longest



#csv_files = glob.glob("/home/pwm4/Desktop/cg342/cleaned_raw_comparison/KSS/KSS_cleaned/KSS_cleaned_csv/special_case/*.csv")
path = "/home/pwm4/Desktop/cg342/cleaned_raw_comparison/PVT/redo/clean/cleaned_data/PVT_cleaned_all_csv/"
#path = "/home/pwm4/Desktop/cg342/cleaned_raw_comparison/KSS/KSS_cleaned/KSS_cleaned_csv/"
csv_files = glob.glob(path+"*.csv")

# generate output folder
timestr = time.strftime("%Y%m%d-%H%M%S")
outputpath =  inputpath + "output_" + timestr + "/"
if not os.path.exists(outputpath):
    os.makedirs(outputpath)


# keep the order same as the order it was added
adict = OrderedDict()

### create lists ###
allcolumns = [] # for all files
listofcolumn = [] # for current file


for filename in csv_files:

    print filename
    with open(filename, 'r') as f1:
#        data = f1.read()
#        data.decode("utf-16")
#        first_line = data[0]
#        data = [line.decode("utf-16", "ignore") for line in f1]
#        first_line = data[0]
#        print(first_line)
        first_line = f1.readline()
        # strip the first line only: the quotation marks
        first_line = first_line.replace('"', '')
        # all capitalized
        first_line = first_line.upper()
        first_line = first_line.rstrip()
#        first_line = first_line.rstrip("\n").decode("utf-16")
        listofcolumn = first_line.split(",")
#       print(filename)        
#        print(first_line)
#        print(listofcolumn)
#        # listofcolumn is the dictionary for current file


    with open(filename, 'r') as f:
        columns = defaultdict(list)
        reader = csv.DictReader(f) # read rows into a dictionary format
#        reader = csv.reader(codecs.open(filename, 'rU', 'utf-16'))
#        reader = csv.DictReader(x.replace('\0', '') for x in f)
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k.upper()].append(v)

#        print(columns['A'])
##        print(listofcolumn)
        for col in listofcolumn:
            if (col == "") or (len(col)>25):
#                print("here")
                pass
            elif col not in allcolumns:
                allcolumns.append(col)
#                if col != allcolumns[0]:
                if not adict: # check if adict is empty (empty dic = false)
                    l=0
                else: 
                    l = len(adict[allcolumns[0]]) - len(columns[allcolumns[0]])
                adict[col] = [None] * l
                
                adict[col] += columns[col]
            else:     
                adict[col] += columns[col]
####                print("here")

with open(outputpath + "output.csv", "wb") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(adict.keys())
    export_data = zip_longest(*adict.values(), fillvalue = "")
    writer.writerows(export_data)
   


