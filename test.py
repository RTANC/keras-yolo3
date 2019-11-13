import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image

def detect_img(yolo):
    for i in range(120):
        img = "test\\" + str(i+1) + ".jpg"
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            fname = r_image.filename.split("\\")
            save_path = "results\\" + fname[len(fname) - 1]
            r_image.save(save_path)
            # r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    detect_img(YOLO())
   
