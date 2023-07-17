# Grad_Project_Scripts
## Descripion 
===> These scripts made while working on my graduation project to help me finsih some tasks with dataset faster 


#### Change_class_num
- this script to edit class number in each text file

#### DrawLabels
- i used this to draw labels on image to check tha coordination is right

#### data_handle
===> this script contain two functions 

1. count: this only counts specific pattern in my folder to know 
        how much images of each class i have for train
2. move: To Move specific images from folder to another

#### remove_img_dublicate
- calculate images hashes and remove images with same hash
  that help me to remove dublicates from my dataset

#### xml2yolo
===> this script contain two functions 
1. xml_to_yolo: convert XML bounding box (xmin, ymin, xmax, ymax)
             to YOLO bounding box (x_center, y_center, width, height)
2. get_xmls: to return all xml files in dir and thier corresponding images and parse content 

#### rename
- to rename some images wit pattern to new pattern
  
#### resizing 
- make all images don't exceed max width and h resize it

#### split_dataset
- split dataset to train and validation 

