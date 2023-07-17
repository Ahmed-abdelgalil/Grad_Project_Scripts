import cv2

def draw_bounding_boxes(image_path, label_path):
    """
        draw_bounding_boxes on images using text label in yolov8 format 
        @image_path: path for image 
        @label_path: path for its corresponding label 
    """
    # Load the image and its corresponding labels
    image = cv2.imread(image_path)
    labels = open(label_path, "r").readlines()

    img_height ,img_width= image.shape[:2]
    # print(type(image))
    # print(img_width,'*',img_height)

    # Loop through each label and draw a bounding box on the image
    for label in labels:
        label_parts = label.split()
        class_index, x_center, y_center, x_width, y_height = map(float, label_parts)
        # convert yolo to points
        x_center *= img_width
        y_center *= img_height
        x_width *= img_width
        y_height *= img_height
        x_width /= 2.0
        y_height /= 2.0
        x1, y1, x2, y2 = int(x_center - x_width), int(y_center - y_height), int(x_center + x_width), int(y_center + y_height)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Show the image with bounding boxes
    cv2.imshow("Image with bounding boxes", image)
    cv2.waitKey(0)

# Example usage
label_path = "label path "
image_path = "image_path"
draw_bounding_boxes(image_path, label_path)
