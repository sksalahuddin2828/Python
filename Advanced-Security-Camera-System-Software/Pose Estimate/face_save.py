import time
import face_recognition
import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

#SAVE FOLDER
folder_name = "faces/emp1/"
cap = cv2.VideoCapture(0)

view = [0,0,0,0,0]
t1=-1
x1=-1
y1=-1
process_complete=False
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        image = cv2.flip(image, 1)

        try:
            #DRAW BOX ON FACE
            faceLoc = face_recognition.face_locations(image)[0]
            cv2.rectangle(image, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 0))
            #face_landmarks = results.multi_face_landmarks
            for facial_landmarks in results.multi_face_landmarks:
                pt1 = facial_landmarks.landmark[1]
                #print(pt1)
                if(x1==-1 or y1==-1):
                    x1 = int(pt1.x*width)
                    y1 = int(pt1.y*height)
                xc = int(pt1.x*width)
                yc = int(pt1.y * height)
                #cv2.circle(image, (x1, y1), radius=20, color=(0, 255, 0), thickness=2)


                if(t1 == -1):
                    t1 = time.time()

                #Front
                if(view[0]==0):
                    image = cv2.putText(image, "Look Ahead", (0+int(width/12), int(height / 2)), cv2.FONT_HERSHEY_DUPLEX, 3,
                                (0, 0, 255), 2)
                    t2=time.time()

                    if(int(t2-t1)>3 and int(t2-t1)<5):
                        #faceLoc = face_recognition.face_locations(image)[0]
                        front_name = "front.jpg"
                        cv2.imwrite(folder_name+front_name, frame)

                        image = cv2.putText(image, "Complete", (0 + int(width / 12), int((height / 2)+(height/4))),
                                            cv2.FONT_HERSHEY_DUPLEX, 3,
                                            (0, 255, 0), 2)
                    elif (int(t2-t1)<=3):
                        image = cv2.putText(image, str(int(t2-t1)), (0 + int(width / 2), int((height / 2) +(height/4))),
                                            cv2.FONT_HERSHEY_DUPLEX, 3,
                                            (0, 0, 255), 2)
                    else:
                        view[0] = 1
                        t1 = time.time()

                #LEFT
                if (view[0] == 1 and view[1] == 0):
                    image = cv2.putText(image, "Look Left", (0 + int(width / 12), int(height / 2)),
                                        cv2.FONT_HERSHEY_DUPLEX, 3,
                                        (0, 0, 255), 2)
                    t2 = time.time()

                    if (xc > x1 + 20):
                        if (int(t2 - t1) > 3 and int(t2 - t1) < 5):
                            #faceLoc = face_recognition.face_locations(image)[0]
                            front_name = "left.jpg"
                            cv2.imwrite(folder_name + front_name, frame)

                            image = cv2.putText(image, "Complete",
                                                (0 + int(width / 12), int((height / 2) + (height / 4))),
                                                cv2.FONT_HERSHEY_DUPLEX, 3,
                                                (0, 255, 0), 2)
                        elif (int(t2 - t1) <= 3):
                            image = cv2.putText(image, str(int(t2 - t1)),
                                                (0 + int(width / 2), int((height / 2) + (height / 4))),
                                                cv2.FONT_HERSHEY_DUPLEX, 3,
                                                (0, 0, 255), 2)
                        else:
                            view[1] = 1
                            t1 = time.time()
                    else:
                        t1 = time.time()

                #RIGHT
                if(view[0]==1 and view[1]==1 and view[2]==0):
                    image = cv2.putText(image, "Look Right", (0 + int(width / 12), int(height / 2)),
                                        cv2.FONT_HERSHEY_DUPLEX, 3,
                                        (0, 0, 255), 2)
                    t2=time.time()

                    if(xc<x1-20):
                        if (int(t2 - t1) > 3 and int(t2-t1)<5):
                            #faceLoc = face_recognition.face_locations(image)[0]
                            front_name = "right.jpg"
                            cv2.imwrite(folder_name + front_name, frame)

                            image = cv2.putText(image, "Complete", (0 + int(width / 12), int((height / 2)+(height/4))),
                                                cv2.FONT_HERSHEY_DUPLEX, 3,
                                                (0, 255, 0), 2)
                        elif(int(t2-t1)<=3):
                            image = cv2.putText(image, str(int(t2 - t1)), (0 + int(width / 2), int((height / 2) +(height/4))),
                                                cv2.FONT_HERSHEY_DUPLEX, 3,
                                                (0, 0, 255), 2)
                        else:
                            view[2] = 1
                            t1 = time.time()
                    else:
                        t1=time.time()

                #UP
                if (view[0] == 1 and view[1] == 1 and view[2]==1 and view[3]==0):
                    image = cv2.putText(image, "Look Up", (0 + int(width / 12), int(height / 2)),
                                        cv2.FONT_HERSHEY_DUPLEX, 3,
                                        (0, 0, 255), 2)
                    t2 = time.time()

                    if (yc < y1 - 20):
                        if (int(t2 - t1) > 3 and int(t2 - t1) < 5):
                            #faceLoc = face_recognition.face_locations(image)[0]
                            front_name = "up.jpg"
                            cv2.imwrite(folder_name + front_name, frame)

                            image = cv2.putText(image, "Complete",
                                                (0 + int(width / 12), int((height / 2) + (height / 4))),
                                                cv2.FONT_HERSHEY_DUPLEX, 3,
                                                (0, 255, 0), 2)
                        elif (int(t2 - t1) <= 3):
                            image = cv2.putText(image, str(int(t2 - t1)),
                                                (0 + int(width / 2), int((height / 2) + (height / 4))),
                                                cv2.FONT_HERSHEY_DUPLEX, 3,
                                                (0, 0, 255), 2)
                        else:
                            view[3] = 1
                            t1 = time.time()
                    else:
                        t1 = time.time()

                # DOWN
                if (view[0] == 1 and view[1] == 1 and view[2] == 1 and view[3] == 1 and view[4] == 0):
                    image = cv2.putText(image, "Look Down", (0 + int(width / 12), int(height / 2)),
                                        cv2.FONT_HERSHEY_DUPLEX, 3,
                                        (0, 0, 255), 2)
                    t2 = time.time()

                    if (yc > y1 + 20):
                        if (int(t2 - t1) > 3 and int(t2 - t1) < 5):
                            #faceLoc = face_recognition.face_locations(image)[0]
                            front_name = "down.jpg"
                            cv2.imwrite(folder_name + front_name, frame)

                            image = cv2.putText(image, "Complete",
                                                (0 + int(width / 12), int((height / 2) + (height / 4))),
                                                cv2.FONT_HERSHEY_DUPLEX, 3,
                                                (0, 255, 0), 2)
                        elif (int(t2 - t1) <= 3):
                            image = cv2.putText(image, str(int(t2 - t1)),
                                                (0 + int(width / 2), int((height / 2) + (height / 4))),
                                                cv2.FONT_HERSHEY_DUPLEX, 3,
                                                (0, 0, 255), 2)
                        else:
                            view[4] = 1
                            t1 = time.time()
                    else:
                        t1 = time.time()

                if(view[0] == 1 and view[1] == 1 and view[2] == 1 and view[3] == 1 and view[4] == 1):
                    t2 = time.time()
                    if(int(t2 - t1) <= 3):
                        image = cv2.putText(image, "Picture",
                                            (0 + int(width / 12), int((height / 2) )),
                                            cv2.FONT_HERSHEY_DUPLEX, 3,
                                            (0, 255, 0), 2)
                        image = cv2.putText(image, "Added",
                                            (0 + int(width / 12), int((height / 2) + (height / 4))),
                                            cv2.FONT_HERSHEY_DUPLEX, 3,
                                            (0, 255, 0), 2)
                    else:
                        process_complete=True
                        break

        except:
            print("Face Not Detected")
            t1=time.time()
            pass

        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        if (process_complete):
            break

cap.release()
cv2.destroyAllWindows()
