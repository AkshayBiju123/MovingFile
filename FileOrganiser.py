import os
import shutil


path = input('Which file would you like to sort?')
list_or_files = os.listdir(path)

for file in list_or_files:
    os.name, ext = os.path.splitext(file)
    ext = ext[1:]

    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

    else:
        os.makedir(os.path+'/'+ext)
        shutil.move(os.path+'/'+file, path+'/'+ext+'/'+file)
