import os

def change_class_number(file_path, new_num):
    """
        Change the first number at the beginning of each line in a text file(YOLOV8 Format).
        @file_path:path contain labels text files 
        @new_num:new class number

    """
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            parts = line.strip().split()
            if parts and parts[0].isdigit():
                parts[0] = str(new_num)
                line = ' '.join(parts) + '\n'
            file.write(line)
        file.truncate()

folder_path ='patthhhhhh'
for root, _ , files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                change_class_number(file_path, 2)


