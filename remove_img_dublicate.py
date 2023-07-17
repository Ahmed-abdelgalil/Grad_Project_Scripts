import os
import hashlib
import fnmatch


def get_img_hash(img_path):
    """Calculate the hash of a img."""
    with open(img_path, 'rb') as img:
        img_hash = hashlib.md5()
        while chunk := img.read(8192):
            img_hash.update(chunk)
    return img_hash.hexdigest()

def delete_duplicates(img_dir):
    """Delete duplicate image and text imgs with the same hash."""
    img_hashes ={}
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.PNG', '*.JPEG']  
    ## these line used to combare between two directories
    # img_dir2 = ''
    # for i in os.listdir(img_dir2):
    #     img_path2 = os.path.join(img_dir2, i)
   
    #     name, _ = i.split('.')
    #     label_name = name + '.txt'
    #     label_path = os.path.join(lbl_dir, label_name)
    #     if os.path.isfile(img_path2) and any(fnmatch.fnmatch(i, ext) for ext in image_extensions):
    #         img_hash = get_img_hash(img_path2)
    #         img_hashes[img_hash] = img_path2
    for img_name in os.listdir(img_dir):
        img_path = os.path.join(img_dir, img_name)
        name, _ = img_name.split('.')
        label_name = name + '.txt'
        label_path = os.path.join(img_dir, label_name)
        if os.path.isfile(img_path) and any(fnmatch.fnmatch(img_name, ext) for ext in image_extensions):
            img_hash = get_img_hash(img_path)
            if img_hash in img_hashes:
                print(f"Duplicate img found: {img_path}")
                os.remove(img_path)
                os.remove(label_path)
            else:
                img_hashes[img_hash] = img_path

# Specify the directory where the image and text imgs are located
images_path = " "
# labels_path = " "
delete_duplicates(images_path)




