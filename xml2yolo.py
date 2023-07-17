import xml.etree.ElementTree as ET
import glob
import os
import json

# xml_to_yolo: convert XML bounding box (xmin, ymin, xmax, ymax)
#              to YOLO bounding box (x_center, y_center, width, height)
# get_xmls: to return all xml files in dir and thier corresponding images and parse content 

classes = []
input_dir = ""
output_dir = ""
image_dir = ""
#to check if the directory is exist before create a new one 
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

def xml_to_yolo_bbox(bbox, w, h):
    # xmin, ymin, xmax, ymax
    x_center = ((bbox[2] + bbox[0]) / 2) / w
    y_center = ((bbox[3] + bbox[1]) / 2) / h
    width = (bbox[2] - bbox[0]) / w
    height = (bbox[3] - bbox[1]) / h
    return [x_center, y_center, width, height]

def get_xmls(input_dir):
    files = glob.glob(os.path.join(input_dir, '*.xml'))
    for f in files:
        basename = os.path.basename(f)
        filename = os.path.splitext(basename)[0]
        # if not os.path.exists(os.path.join(image_dir, f"{filename}.jpg")):
        #     print(f"{filename} image does not exist!")
        #     continue

        result = []

        # parse the content of the xml file
        tree = ET.parse(f)
        root = tree.getroot()
        img_width = int(root.find("size").find("width").text)
        img_height = int(root.find("size").find("height").text)

        for obj in root.findall('object'):
            label = obj.find("name").text
            # check for new classes and append to list
            if label not in classes:
                classes.append(label)
            index = classes.index(label)
            bbox = [int(x.text) for x in obj.find("bndbox")]
            yolo_bbox = xml_to_yolo_bbox(bbox, img_width, img_height)
            # convert data to string
            bbox_string = " ".join([str(x) for x in yolo_bbox])
            result.append(f"{index} {bbox_string}")

        if result:
            # generate a YOLO format text file for each xml file
            with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf-8") as f:
                f.write("\n".join(result))
    # generate the classes file as reference
    with open('classes.txt', 'w', encoding='utf8') as f:
        f.write(json.dumps(classes))

if __name__ == '__main__':
    
    get_xmls(input_dir)
    

