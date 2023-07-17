#read all images 
import glob
import os 
import shutil
from sklearn.model_selection import train_test_split
from data_handle import count

img_path = "PUT YOUR PATH HERE"
label_path = "PUT YOUR PATH HERE"

target_train_path = "PUT YOUR PATH HERE"
target_val_path = "PUT YOUR PATH HERE"

def split_YOLOV8_dataset(img_path,label_path,target_train_path,target_val_path):
  """
    this function to split my dataset into validation and train dataset 

    @img_path: path contain all images 
    @label_path:path contain all images corresponding labels
    @target_train_path: target_train_path that contain both images and thier labels for train 
    @target_val_path: target_val_path that contain both images and thier labels for validation 
  """

  # Get all files in the current directory
  files = glob.glob(img_path + "/*")

  # Filter out text files
  labels = [f for f in files if f.endswith(".txt")]

  # Get all non-text files
  images = [f for f in files if f not in labels]

  # images = glob.glob (img_path + "/*")
  # labels = glob.glob (label_path + "/*.txt")

  X = images
  Y = labels
  #set no.imgs to use for experimenting
  # divide by 2 because my folder contain both labels and images 
  NUm_imgs= int(count(img_path)/2)

  print(NUm_imgs)

  #split our data into train and validation
  x_train,x_valid,y_train,y_valid =train_test_split(X[:NUm_imgs],
                                                    Y[:NUm_imgs],
                                                    test_size=0.2,
                                                    random_state=42,
                                                    shuffle=True)


  print(len(x_train),len(y_train))

  print(len(x_valid),len(y_valid))

  for n in range(len(x_train)):
    path = x_train[n]
    pathl = y_train[n]
    img_name = os.path.basename(path)
    label_name = os.path.basename(pathl)
    #move train image to target path 
    target_path = os.path.join(target_train_path, img_name)
    shutil.move(path, target_path)
    #move train labels to target path 
    targetl_path = os.path.join(target_train_path, label_name)
    shutil.move(pathl, targetl_path)

  for n in range(len(x_valid)):
    path = x_valid[n]
    pathl = y_valid[n]
    img_name = os.path.basename(path)
    label_name = os.path.basename(pathl)
    #move valid image to target path 
    target_path = os.path.join(target_val_path, img_name)
    shutil.move(path, target_path)
    #move val labels to target path 
    targetl_path = os.path.join(target_val_path, label_name)
    shutil.move(pathl, targetl_path)




