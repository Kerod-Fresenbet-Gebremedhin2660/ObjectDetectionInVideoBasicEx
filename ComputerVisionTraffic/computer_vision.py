import os
import cv2  # opencv library
import numpy as np

BASE_DIR = os.getcwd() + "/Frames/"


class Detect:
    def __init__(self, folder_path):
        self.images = []
        self.folder_path = folder_path
        self.frames = []
        self.diff_images = []
        self.threshold_images = []
        self.dilated_images = []

    def set_images(self):
        self.frames = os.listdir(self.folder_path)
        if len(self.frames) != 0:
            for i in self.frames:
                img = cv2.imread(f"{self.folder_path}/{i}")
                self.images.append(img)
        else:
            print("Exception Occurred")
            raise Exception

    def gray_scale(self, difference):
        try:
            for i in range(len(self.frames) // 2):
                grayColorA = cv2.cvtColor(self.images[i], cv2.COLOR_BGR2GRAY)
                grayColorB = cv2.cvtColor(self.images[i + difference], cv2.COLOR_BGR2GRAY)
                self.diff_images.append(cv2.absdiff(grayColorB, grayColorA))

        except IndexError:
            print("Index Out of Bounds Error")

    def apply_threshold(self):
        try:
            for i in range(len(self.frames) // 2):
                ret, thresh = cv2.threshold(self.diff_images, 30, 255, cv2.THRESH_BINARY)
                self.threshold_images.append(thresh)
        except IndexError:
            print("Index Out of Bounds Error")

    def apply_dilation(self):
        try:
            kernel = np.ones((3, 3), np.uint8)
            for i in range(len(self.frames) // 2):
                self.dilated_images.append(cv2.dilate(self.threshold_images[i], iterations=1))
        except IndexError:
            print("Index Out of BOunds Error")

# Here, the contours for the detection zone has to be set

# Steps

## Apply frame differencing on every pair of consecutive frames
## Apply image thresholding on the output image of the previous step
## Perform image dilation on the output image of the previous step
## Find contours in the output image of the previous step
## Shortlist contours appearing in the detection zone
## Save frames along with the final contours
