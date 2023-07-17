import glob
import os 
import fnmatch
import Change_class_num
import shutil

# set the pattern you're looking for
knife_pattern1 = ['*knife*', '*Knife*', 'Defense*', '*frame*', '*Krav*', '*DSC*', 'Ruso*','knive*']
gun_pattern = ['*gun*' , '*pistol*']
rifle_pattern = '*Rifle*'
sword_pattern = 'Sword*'
phones_pattern = '*phone*'
bazz_pattern = 'Bazooka*'
billete_pattern = '*billete*'
monedero_pattern = ['*monedro*' , 'monedero*']
grenade_pattern = 'Grenade*'
snipers_pattern = 'Sniper*'
smg_pattern = 'SMG*'
tarjeta_pattern = '*tarjeta*'

def count(folder_path):
    """
        this only counts specific pattern in my folder to know 
        how much images of each class i have for train
        @folder_path: path contain all images
    """
    # initialize a counter
    knife_count, gun_count, rifle_count, sword_count = 0, 0, 0, 0
    bazz_count, phones_count, billete_count, monedero_count, tarjeta_count = 0,0, 0, 0, 0
    snipers_count, smg_count, grenade_count , total= 0, 0, 0, 0
    
    # iterate over the file names and check if each one contains the pattern
    for root, _ , files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if any(fnmatch.fnmatch(file_name, pattern) for pattern in knife_pattern1):
                knife_count += 1
                total += 1
               #Change_class_num.change_class_number(file_path, 0)
            elif any(fnmatch.fnmatch(file_name, pattern1) for pattern1 in gun_pattern):
                gun_count += 1
                total +=1
               #Change_class_num.change_class_number(file_path, 1)

            elif fnmatch.fnmatch(file_name, phones_pattern):
                phones_count += 1
                total +=1
                # Change_class_num.change_class_number(file_path, 2)
            elif fnmatch.fnmatch(file_name, billete_pattern):
                billete_count += 1
                total +=1
                # Change_class_num.change_class_number(file_path,3)
            elif any(fnmatch.fnmatch(file_name, pattern2) for pattern2 in monedero_pattern):
                monedero_count += 1
                total +=1
                # Change_class_num.change_class_number(file_path, 4)
            
            elif fnmatch.fnmatch(file_name, tarjeta_pattern):
                tarjeta_count += 1
                total +=1
                # Change_class_num.change_class_number(file_path, 5)
    
    non_weapon = phones_count+tarjeta_count+billete_count+monedero_count
    # print the count
    print("knife", int(knife_count/2)," class num: 0")
    print("gun", int(gun_count/2)," class num: 1")
    print('non_weapons',int(non_weapon/2)," class num: 2")
    # # print("rifle", rifle_count," class num: 2")
    # # print("sword", sword_count," class num: 3")
    # print("phones", phones_count," class num: 2")
    # # print("bazz", bazz_count," class num: 5")
    # print("billete", billete_count," class num: 3")
    # print("monedero", monedero_count," class num: 4")
    # # print("grenade", grenade_count," class num: 8")
    # # print("snipers", snipers_count," class num: 9")
    # # print("smg", smg_count," class num: 10")
    # print("tarjeta", tarjeta_count," class num: 5")
    print("total", int(total/2))
    
    return total

def move(path, target_path):
    """
        To Move specific images from folder to another 

        @path: path for images 
        @target_path: path to move this images to 
    """
    for image in os.listdir(path):        
        if any(fnmatch.fnmatch(image, pattern) for pattern in sword_pattern):
            #move sword image to new test path 
            img_path = os.path.join(path, image)
            target_path1 = os.path.join(target_path, image)
            shutil.move(img_path, target_path1)
        elif any(fnmatch.fnmatch(image, pattern) for pattern in snipers_pattern):
            #move sniper image to new test path 
            img_path = os.path.join(path, image)
            target_path1 = os.path.join(target_path, image)
            shutil.move(img_path, target_path1)
        elif any(fnmatch.fnmatch(image, pattern) for pattern in smg_pattern):
            #move smg image to new test path 
            img_path = os.path.join(path, image)
            target_path1 = os.path.join(target_path, image)
            shutil.move(img_path, target_path1)
        elif any(fnmatch.fnmatch(image, pattern) for pattern in grenade_pattern):
            #move sniper image to new test path 
            img_path = os.path.join(path, image)
            target_path1 = os.path.join(target_path, image)
            shutil.move(img_path, target_path1)
        elif any(fnmatch.fnmatch(image, pattern) for pattern in rifle_pattern):
            #move sniper image to new test path 
            img_path = os.path.join(path, image)
            target_path1 = os.path.join(target_path, image)
            shutil.move(img_path, target_path1)
        elif any(fnmatch.fnmatch(image, pattern) for pattern in bazz_pattern):
            #move sniper image to new test path 
            img_path = os.path.join(path, image)
            target_path1 = os.path.join(target_path, image)
            shutil.move(img_path, target_path1)
        

path = "your ppath "
target = "your target path "













##################### more gun 
# elif fnmatch.fnmatch(file_name, grenade_pattern):
            #     grenade_count += 1
            #     total +=1
            #    #Change_class_num.change_class_number(file_path, 8)
            # elif fnmatch.fnmatch(file_name, snipers_pattern):
            #     snipers_count += 1
            #     total +=1
            #    #Change_class_num.change_class_number(file_path, 9)
            # elif fnmatch.fnmatch(file_name, smg_pattern):
            #     smg_count += 1
            #     total +=1
            #    #Change_class_num.change_class_number(file_path, 10)
# elif fnmatch.fnmatch(file_name, bazz_pattern):
            #     bazz_count += 1
            #     total +=1
            #    #Change_class_num.change_class_number(file_path, 5)

# elif fnmatch.fnmatch(file_name, rifle_pattern):
            #     rifle_count += 1
            #     total +=1
            #    #Change_class_num.change_class_number(file_path, 2)
            # elif fnmatch.fnmatch(file_name, sword_pattern):
            #     sword_count += 1
            #     total +=1
            #    #Change_class_num.change_class_number(file_path, 3)