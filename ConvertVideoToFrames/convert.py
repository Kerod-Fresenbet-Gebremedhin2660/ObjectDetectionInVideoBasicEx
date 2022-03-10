import cv2
import os

BASE_DIR = os.getcwd() + "/Frames/"


class Video:
    def __init__(self, file_name, fps, file_path, file_extension):
        """
        This is used to initialize the Video Instance
        :param file_name -> Video Name
        :param fps -> Video Frames Per Second
        :param file_path -> File Path to The Video
        :param file_extension -> File Extension of The Video File
        """
        self.fileName = file_name
        self.filePath = file_path
        self.fps = fps
        self.fileExtension = file_extension
        try:
            os.mkdir(BASE_DIR + file_name)
            self.framesFolder = BASE_DIR + file_name
        except FileExistsError:
            self.framesFolder = BASE_DIR + file_name

    def __str__(self):
        print(
            f"File Name => {self.fileName}\nFPS => {self.fps}\nFile Extension => {self.fileExtension}\nFrames Folder => {self.framesFolder}")

    def save_frame(self, gap=10):
        video_path = f"{self.filePath}/{self.fileName}.{self.fileExtension}"
        save_path = self.framesFolder

        cap = cv2.VideoCapture(video_path)
        idx = 0

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                cap.release()
                break

            if idx == 0:
                try:
                    cv2.imwrite(f"{save_path}/{idx}.png", frame)
                except:
                    print("Exception Occurred")
            else:
                if idx % gap == 0:
                    try:
                        cv2.imwrite(f"{save_path}/{idx}.png", frame)
                    except:
                        print("Exception Occurred")
            idx += 1




