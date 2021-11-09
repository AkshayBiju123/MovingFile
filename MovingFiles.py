import os
import shutil

source = input('enter the source folder')
destination = input('enter the destination folder')
source = 'source+'/''
destination = 'destination+'/''
list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.move((source+file), destination)