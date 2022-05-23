import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import time

print(cv2.__version__)

# make_edges reads an image from /images and outputs the result of running
# edge detection on that image to /out
def make_edges(image):
   img = cv2.imread(image)
   tail = os.path.split(image)[1]
   edges = cv2.Canny(img,100,200)
   plt.imsave(os.path.join("/out", os.path.splitext(tail)[0]+'.png'), edges, cmap = 'gray')

# save start time
start_time = time.monotonic()

# walk /images and call make_edges on every file found
for dirpath, dirs, files in os.walk("/images"):
   for file in files:
       make_edges(os.path.join(dirpath, file))

# print execution time
print('\nexecution time: ', time.monotonic() - start_time, '\n')