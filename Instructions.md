__1 create a text file for all the paths (clean/raw)__

__2 run  `1_covert_paths.py`  (after changing file path and output file name)__

 - creating a new txt file with all the linux paths

__3 check all the filenames in that file (if they all have extension)__

__4 run `2_move_files.py` (after creating a new folder for copying files, changing filepaths)__

__5 check sheet name__

   - acceptable, FEV, etc.

     __6 run `3_xls_to_csv.py` __

- somehow running in small batches works better

__7 run `4_dbf_to_csv.py`__

- paths
- line 10 ```"*.dbf" to "*.DBF"```

__8 run `5_merge.py`__

