from deep_sort_v4 import Deep
from yolo_detection import *

od = ObjectDetection()

deep = Deep(nn_budget=10)
video1 = "sample/gsf.mp4"
video2 = "sample/test.mp4"
video3 = "sample/shop front door.mp4"
video4 = "sample/OscarTest.mp4"

deep.Object_tracking(video4,"output/detection.mp4","output/people/")
cv2.destroyAllWindows()
