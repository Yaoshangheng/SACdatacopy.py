'''
Written by Yuan Yao.
The functions:
1. Copy SAC data to Newfolder
2. Select and separate by Data
3. Both Linux or Windows by changing Dirpath on line 43
'''
import os
import datetime
import shutil

def copy_file(filePath, toDir):
    # YN.KMI.20231115.HHE.SAC
    values = filePath.split(".")
    
    if len(values) < 4:
        print("Invalid filename:", filePath)
        return

    date_str = values[2]
    try:
        # Parsing date from the filename
        beginDate = datetime.datetime.strptime(date_str, '%Y%m%d')
    except ValueError:
        print("Invalid date format in filename:", filePath)
        return

    new_dir = os.path.join(toDir, beginDate.strftime("%Y%m%d"))
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    shutil.copy(filePath, new_dir)
    print("Copy", filePath, "to", new_dir)

def main(fromDir, toDir):
    if not os.path.exists(fromDir):
        print("Source directory does not exist:", fromDir)
        return
    if not os.path.exists(toDir):
        print("Destination directory does not exist:", toDir)
        return    
    for root, sub_dirs, files in os.walk(fromDir):
        for f in files:
            filePath = os.path.join(root, f)
            if filePath.upper().endswith(".SAC"):
                copy_file(filePath, toDir)

# Example usage:
main("/run/media/yaoyuan/data2/TC_data/2", "/run/media/yaoyuan/data2/TC_sacdata/test")