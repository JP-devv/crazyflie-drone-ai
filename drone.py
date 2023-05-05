import os
import sys

if len(sys.argv) > 1:
  image = sys.argv[1]
else:
  image = './data/images/bus.jpg'

os.system(f'python detect.py --weights yolov5s.pt --class 0 --save-txt --device mps --source {image}')
