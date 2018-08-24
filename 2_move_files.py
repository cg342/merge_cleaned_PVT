# copy files from paths
# to a new directory (of current folder)

import shutil
import os


inputfile = "path_clean_linux.txt"
dst_path = "/home/pwm4/Desktop/cg342/cleaned_raw_comparison/PVT/redo/clean/cleaned_data/"
filenum = 1
# read file line by line
with open(inputfile, "r") as f:
    for line in f:
      # get source paths
      scr = line.rstrip('\n')
      filename = os.path.basename(os.path.splitext(scr)[0])
      extension = os.path.splitext(scr)[1]
      # destination 
      dst_stripped = os.path.join(dst_path,filename) # path without extension
      fileindex = "_" + str(filenum)
      dst_stripped += fileindex
#      dst_check = dst_stripped + extension
#      while os.path.exists(dst_check):
#        
#        dst_stripped += "_duplicate"
#        dst_check = dst_stripped + extension
      # add extension to the end - ultimate destination
      dst_stripped += extension
      shutil.copy2(scr, dst_stripped)
      filenum += 1      
      print(scr)
      
      
