import cv2
import numpy as np
def apply_colour_filter(image,filtertype):
    filterimage=image.copy()
    if filtertype=="red_tint":
        filterimage[:,:,0]=0
        filterimage[:,:,1]=0
    elif filtertype=="blue_tint":
         filterimage[:,:,2]=0
         filterimage[:,:,1]=0
    elif filtertype=="green_tint":
         filterimage[:,:,0]=0
         filterimage[:,:,2]=0
    elif filtertype=="increased_red":
         filterimage[:,:,2]=cv2.add(filterimage[:,:,2],50)
    elif filtertype=="decreased_blue":
         filterimage[:,:,0]=cv2.subtract(filterimage[:,:,0],50)
    return(filterimage)
image=cv2.imread("zara.jpg")
if image is None:
     print("GO to hell")
else:
     filtertype="original"
     print("Press the following key to apply filter: R for red, B for blue, G for green, I for increased red, D for decreased blue and Q for quit")
     while True:
          filterimage=apply_colour_filter(image,filtertype)
          cv2.imshow("filterimage",filterimage)
          key=cv2.waitKey(0) & 0xFF
          if key==ord("R"):
               filtertype="red_tint"
          elif  key==ord("B"):
               filtertype="blue_tint"
          elif  key==ord("G"):  
               filtertype="green_tint"
          elif  key==ord("I"):
               filtertype="increased_red"
          elif  key==ord("D"):
               filtertype="decreased_blue"
          elif key==ord("Q"):
               break
          else:
               print("Invalid please read instructions")
cv2.destroyAllWindows()