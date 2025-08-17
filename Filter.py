import cv2
import numpy as np

def apply_colour_filter(image, filtertype):
    filterimage = image.copy()
    if filtertype == "red_tint":
        filterimage[:, :, 0] = 0
        filterimage[:, :, 1] = 0
    elif filtertype == "blue_tint":
        filterimage[:, :, 2] = 0
        filterimage[:, :, 1] = 0
    elif filtertype == "green_tint":
        filterimage[:, :, 0] = 0
        filterimage[:, :, 2] = 0
    elif filtertype == "increased_red":
        filterimage[:, :, 2] = cv2.add(filterimage[:, :, 2], 50)
    elif filtertype == "decreased_red":
        filterimage[:, :, 2] = cv2.subtract(filterimage[:, :, 2], 50)
    elif filtertype == "decreased_blue":
        filterimage[:, :, 0] = cv2.subtract(filterimage[:, :, 0], 50)
    elif filtertype == "decreased_green":
        filterimage[:, :, 1] = cv2.subtract(filterimage[:, :, 1], 50)
    return filterimage

image = cv2.imread("zara.jpg")
if image is None:
    print("Image not found. Please make sure 'zara.jpg' is in the same directory.")
else:
    filtertype = "original"
    print("Press the following key to apply filter:")
    print("R: red tint")
    print("B: blue tint")
    print("G: green tint")
    print("I: increased red")
    print("P: decreased red")
    print("D: decreased blue")
    print("E: decreased green")
    print("Q: quit")
    
    while True:
        filterimage = apply_colour_filter(image, filtertype)
        cv2.imshow("filterimage", filterimage)
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord("R"):
            filtertype = "red_tint"
        elif key == ord("B"):
            filtertype = "blue_tint"
        elif key == ord("G"):
            filtertype = "green_tint"
        elif key == ord("I"):
            filtertype = "increased_red"
        elif key == ord("P"):
            filtertype = "decreased_red"
        elif key == ord("D"):
            filtertype = "decreased_blue"
        elif key == ord("E"):
            filtertype = "decreased_green"
        elif key == ord("Q"):
            break
        else:
            print("Invalid key. Please press a valid key.")

cv2.destroyAllWindows()