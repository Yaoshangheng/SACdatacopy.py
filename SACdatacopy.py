'''
Written by Yuan Yao.
The functions:
1.Copy SACdata to Newfolder
2.Select and separate by Data
3.Both linux or Windows by changing Dirpath on line 43
'''
import os
import datetime
import shutil

def copy_file(filePath, toDir):
    # YN.KMI.2018.122.HHE.SAC
    values = filePath.split(".")
    i = len(values) - 1
    while i >= 0:
        if values[i].isdigit() and len(values[i]) == 4:
            break
        i -= 1
    if i < 0 or (i+1) >= len(values) or not values[i+1].isdigit():
        print("invalid filename:", filePath)
        return
    beginDate = datetime.datetime.strptime(values[i],'%Y')
    endDate = beginDate + datetime.timedelta(days=(int(values[i+1]) - 1))
    new_dir = os.path.join(toDir, endDate.strftime("%Y%m%d"))
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    shutil.copy(filePath, new_dir)
    print("copy", filePath, "to", new_dir)

def main(fromDir, toDir, iyear):
    if not os.path.exists(fromDir):
        print("not exits:", fromDir)
        return
    if not os.path.exists(toDir):
        print("not exits:", toDir)
        return    
    for root, sub_dirs, files in os.walk(fromDir):
        for f in files:
            filePath = os.path.join(root, f)
            if str(iyear) in filePath and filePath.upper().endswith(".SAC"):
                copy_file(filePath, toDir)
main(r"I:\", r"G:/", 2019)

