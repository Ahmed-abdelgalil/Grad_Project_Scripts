import os
import fnmatch

""" Rename some files with specific patter set to new pattern """

folder_path = " "
pattern = ['*knife*', '*Knife*', 'Defense*', '*frame*', '*Krav*', '*DSC*', 'Ruso*']
new = "knifest2_"
count = 1

for filename in os.listdir(folder_path):
    # if filename.startswith(pattern):  # Change the file extension to match your image format
     if any(fnmatch.fnmatch(filename, p) for p in pattern):
        new_filename = new + str(count) + ".txt"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        count +=1 
