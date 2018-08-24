import os

inputfile = "/home/pwm4/Desktop/cg342/cleaned_raw_comparison/PVT/redo/clean/path_clean.txt"


# read file line by line
with open(inputfile, "r") as f:
    
    for line in f:
#      path = line.encode('string-escape')
      path = line
#      path = path.strip("\n")
#      path = path.replace("\\n", "")
#      linelist = path.split(',')
#      path = linelist[1]
#      print(linelist)
#      path = path.replace("\\n", "")
      path = path.replace(":\\", "/")
      path = path.replace("\\", "/")
#      path = path.replace("//", "/")
      path = "/"+path
#      print path
#     
 
# create a new txt file      
      with open("path_clean_linux.txt", 'a') as out:
        out.write(path)
        print path


