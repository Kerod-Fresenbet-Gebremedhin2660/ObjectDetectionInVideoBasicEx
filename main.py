from ComputerVisionTraffic.computer_vision import Detect
import os

BASE_DIR = os.getcwd() + "/Frames/video/"


if __name__ == "__main__":

    detect = Detect(BASE_DIR)
    try:
        detect.set_images()
    except:
        print("Exception Occurred")

    detect.gray_scale(0, 1)

