import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from yolov3.utils import Load_Yolo_model, image_preprocess, postprocess_boxes, nms, draw_bbox, read_class_names
from yolov3.configs import *
import time
from deep_sort import nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker
from deep_sort import generate_detections as gdet

def return_time(frames,fps):
    seconds = int(frames / fps)
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    seconds = int(seconds % 60)
    minutes = int(minutes % 60)
    time = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    return time

class Deep:
    def __init__(self, nn_budget=10):
        return
    def Object_tracking(self,video_path,output_path,save_people_folder):
        Yolo = Load_Yolo_model()
        nn_budget = None
        input_size = 416
        show = False
        CLASSES = YOLO_COCO_CLASSES
        score_threshold = 0.3
        iou_threshold = 0.45
        max_cosine_distance = 0.7
        Track_only = ["person"]

        # initialize deep sort object
        model_filename = 'model_data/mars-small128.pb'
        encoder = gdet.create_box_encoder(model_filename, batch_size=1)
        metric = nn_matching.NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
        tracker = Tracker(metric)

        if video_path:
            vid = cv2.VideoCapture(video_path)  # detect on video
        else:
            vid = cv2.VideoCapture(0)  # detect from webcam

        width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(vid.get(cv2.CAP_PROP_FPS))
        codec = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_path, codec, fps, (width, height))

        NUM_CLASS = read_class_names(CLASSES)
        #print(NUM_CLASS)
        key_list = list(NUM_CLASS.keys())
        val_list = list(NUM_CLASS.values())

        frame_number=0
        people =[]
        time="0:0:0"
        while True:
            # print(os.getcwd())
            _, frame = vid.read()
            original_frame = frame.copy()

            image_data = image_preprocess(np.copy(original_frame), [input_size, input_size])
            image_data = image_data[np.newaxis, ...].astype(np.float32)

            if YOLO_FRAMEWORK == "tf":
                pred_bbox = Yolo.predict(image_data)
            elif YOLO_FRAMEWORK == "trt":
                batched_input = tf.constant(image_data)
                result = Yolo(batched_input)
                pred_bbox = []
                for key, value in result.items():
                    value = value.numpy()
                    pred_bbox.append(value)

            pred_bbox = [tf.reshape(x, (-1, tf.shape(x)[-1])) for x in pred_bbox]
            pred_bbox = tf.concat(pred_bbox, axis=0)

            bboxes = postprocess_boxes(pred_bbox, original_frame, input_size, score_threshold)
            bboxes = nms(bboxes, iou_threshold, method='nms')
            boxes, scores, names = [], [], []
            #print(bboxes)
            for bbox in bboxes:
                if int(bbox[5])==0:
                    boxes.append([bbox[0].astype(int), bbox[1].astype(int), bbox[2].astype(int) - bbox[0].astype(int),
                                  bbox[3].astype(int) - bbox[1].astype(int)])
                    scores.append(bbox[4])
                    names.append("person")

            # Obtain all the detections for the given frame.
            boxes = np.array(boxes)
            names = np.array(names)
            scores = np.array(scores)
            features = np.array(encoder(original_frame, boxes))
            detections = [Detection(bbox, score, class_name, feature) for bbox, score, class_name, feature in
                          zip(boxes, scores, names, features)]

            #STARTING DEEPSORT
            tracker.predict()
            tracker.update(detections)

            # Obtain info from the tracks
            tracked_bboxes = []
            for track in tracker.tracks:
                if not track.is_confirmed() or track.time_since_update > 5:
                    continue
                bbox = track.to_tlbr()
                class_name = track.get_class()
                tracking_id = track.track_id
                index = key_list[val_list.index(class_name)]
                bboxToList = bbox.tolist()
                tracked_bboxes.append(bboxToList + [tracking_id, index])

            #FUNCTION POINTS
            for i in tracked_bboxes:
                image = cv2.circle(original_frame, (int(i[0]), int(i[1])), radius=20, color=(0, 255, 0), thickness=2)
                image = cv2.circle(original_frame, (int(i[2]), int(i[3])), radius=20, color=(0, 255, 255), thickness=2)

            for i in tracked_bboxes:
                if(i[4] not in people):
                    if((i[0]-20>0 and i[1]-20>0 and i[2]+20<width and i[3]+20<height)or
                            (i[3]-i[1]>height*3/4)or
                            (i[2]-i[0]>width*3/4)):
                        x1 = int(i[0])
                        y1 = int(i[1])
                        x2 = int(i[2])
                        y2 = int(i[3])
                        crop_img = frame[y1:y2, x1:x2]
                        time = time.replace(':','.')
                        name = time+"-id."+str(i[4])
                        print(save_people_folder+name)
                        bool = cv2.imwrite(save_people_folder+name+'.jpg', crop_img)
                        print(bool)
                        people.append(i[4])

            #print(tracked_bboxes)
            #Draw
            image = draw_bbox(original_frame, tracked_bboxes, CLASSES=CLASSES, tracking=True,rectangle_colors='')
            #image = draw_bbox()

            #frame
            time = return_time(frame_number,fps)
            frame_number += 1
            #print(frame_number)
            #print(time)
            image = cv2.putText(image, "Time: "+time, (0, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0, 0, 255), 2)

            #Display
            cv2.imshow('output', image)

            #Write
            if output_path != '': out.write(image)


            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

    def sort_tracker(self):
        return
