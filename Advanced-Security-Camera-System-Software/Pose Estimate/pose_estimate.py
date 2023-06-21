import cv2
import mediapipe as mp
import time
import face_recognition

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
#Employee = "emp3"
Employee = "emp2"

#SAVED FACE
#FRONT
imgEmpFront = face_recognition.load_image_file('Faces/'+Employee+'/front.jpg')
imgEmpFront = cv2.cvtColor(imgEmpFront, cv2.COLOR_BGR2RGB)
encodeEmpFront = face_recognition.face_encodings(imgEmpFront)[0]

#LEFT
imgEmpLeft = face_recognition.load_image_file('Faces/'+Employee+'/left.jpg')
imgEmpLeft = cv2.cvtColor(imgEmpLeft, cv2.COLOR_BGR2RGB)
encodeEmpLeft = face_recognition.face_encodings(imgEmpLeft)[0]

#RIGHT
imgEmpRight = face_recognition.load_image_file('Faces/'+Employee+'/right.jpg')
imgEmpRight = cv2.cvtColor(imgEmpRight, cv2.COLOR_BGR2RGB)
encodeEmpRight = face_recognition.face_encodings(imgEmpRight)[0]

#UP
imgEmpUp = face_recognition.load_image_file('Faces/'+Employee+'/up.jpg')
imgEmpUp = cv2.cvtColor(imgEmpUp, cv2.COLOR_BGR2RGB)
encodeEmpUp = face_recognition.face_encodings(imgEmpUp)[0]

#DOWN
imgEmpDown = face_recognition.load_image_file('Faces/'+Employee+'/down.jpg')
imgEmpDown = cv2.cvtColor(imgEmpDown, cv2.COLOR_BGR2RGB)
encodeEmpDown = face_recognition.face_encodings(imgEmpDown)[0]

#WEB CAM
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#DETECT FACE
def compareFace(image,encodeEmpFront,encodeEmpLeft,encodeEmpRight,encodeEmpUp,encodeEmpDown):
    try:
        encode = face_recognition.face_encodings(image)[0]
        probability = 0
        if(face_recognition.compare_faces([encodeEmpFront],encode)[0]):
            #print(face_recognition.compare_faces([encodeElon],encode))
            probability+=1

        if (face_recognition.compare_faces([encodeEmpLeft], encode)[0]):
            # print(face_recognition.compare_faces([encodeElon],encode))
            probability += 1

        if (face_recognition.compare_faces([encodeEmpRight], encode)[0]):
            # print(face_recognition.compare_faces([encodeElon],encode))
            probability += 1

        if (face_recognition.compare_faces([encodeEmpUp], encode)[0]):
            # print(face_recognition.compare_faces([encodeElon],encode))
            probability += 1

        if (face_recognition.compare_faces([encodeEmpDown], encode)[0]):
            # print(face_recognition.compare_faces([encodeElon],encode))
            probability += 1

        if(probability>2):
            return True
        return False
    except:
        return False

#DETECT ARM RAISE
def detectArmRaise(left_elbow,right_elbow,nose):
    if(left_elbow.y<nose.y and right_elbow.y<nose.y):
        return True

    return False

#DETECT HAND SIGNAL
def detectHandSignal(nose,thumb_tip,index_finger_tip,index_finger_pip,middle_finger_tip,ring_finger_tip,pinky_tip):

    if(index_finger_pip.y<index_finger_tip.y):
        return False

    if(middle_finger_tip.y<index_finger_pip.y or ring_finger_tip.y<index_finger_pip.y or pinky_tip.y<index_finger_pip.y):
        return False

    if(abs(nose.x-index_finger_tip.x)<abs(nose.x-thumb_tip.x)):
        return False

    #print("True")
    return True

def drawPose(color):
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2), mp_drawing.DrawingSpec(color=color, thickness=2, circle_radius=2))

t1=time.time()
t2=time.time()
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = holistic.process(image)
        image.flags.writeable = True
        #print(results.face_landmarks)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            body_landmarks = results.pose_landmarks.landmark

            leftHand_landmarks = results.left_hand_landmarks.landmark

            rightHand_landmarks = results.right_hand_landmarks.landmark
            #print(rightHand_landmarks)

        except:
            pass

        try:
            if(body_landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].visibility > 0.5):
                Left_Elbow = body_landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value]
            if (body_landmarks[mp_holistic.PoseLandmark.RIGHT_ELBOW.value].visibility > 0.5):
                Right_Elbow = body_landmarks[mp_holistic.PoseLandmark.RIGHT_ELBOW.value]
            if (body_landmarks[mp_holistic.PoseLandmark.NOSE.value].visibility > 0.5):
                Nose = body_landmarks[mp_holistic.PoseLandmark.NOSE.value]
            if  (body_landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].visibility > 0.5):
                Left_Thumb = leftHand_landmarks[mp_holistic.HandLandmark.THUMB_TIP.value]
                Left_Index_Tip = leftHand_landmarks[mp_holistic.HandLandmark.INDEX_FINGER_TIP.value]
                Left_Index_Pip = leftHand_landmarks[mp_holistic.HandLandmark.INDEX_FINGER_PIP.value]
                Left_Pinky = leftHand_landmarks[mp_holistic.HandLandmark.PINKY_TIP.value]
                Left_Middle = leftHand_landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_TIP.value]
                Left_Ring = leftHand_landmarks[mp_holistic.HandLandmark.RING_FINGER_TIP.value]
            if (body_landmarks[mp_holistic.PoseLandmark.RIGHT_WRIST.value].visibility > 0.5):
                Right_Thumb = rightHand_landmarks[mp_holistic.HandLandmark.THUMB_TIP.value]
                Right_Index_Tip = rightHand_landmarks[mp_holistic.HandLandmark.INDEX_FINGER_TIP.value]
                Right_Index_Pip = rightHand_landmarks[mp_holistic.HandLandmark.INDEX_FINGER_PIP.value]
                Right_Pinky = rightHand_landmarks[mp_holistic.HandLandmark.PINKY_TIP.value]
                Right_Middle = rightHand_landmarks[mp_holistic.HandLandmark.MIDDLE_FINGER_TIP.value]
                Right_Ring = rightHand_landmarks[mp_holistic.HandLandmark.RING_FINGER_TIP.value]

            #CHECKING FACE
            faceLoc = face_recognition.face_locations(image)[0]
            checkFace = compareFace(image,encodeEmpFront,encodeEmpLeft,encodeEmpRight,encodeEmpUp,encodeEmpDown)
            if (checkFace):
                cv2.rectangle(image, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 255, 0))

            else:
                cv2.rectangle(image, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 255))
            center = (int((faceLoc[1] + faceLoc[3]) / 2), int((faceLoc[0] + faceLoc[2]) / 2))
            cv2.circle(image, center, radius=20, color=(0, 255, 0), thickness=2)

            #CHECKING POSE

            if (detectHandSignal(Nose, Left_Thumb, Left_Index_Tip, Left_Index_Pip, Left_Middle, Left_Ring, Left_Pinky) and detectHandSignal(Nose, Right_Thumb, Right_Index_Tip, Right_Index_Pip, Right_Middle, Right_Ring, Right_Pinky) and detectArmRaise(Left_Elbow, Right_Elbow, Nose) and checkFace):
                t1=time.time()
                timer = int(t1-t2)
                if(timer<5):
                    drawPose((255, 0, 255))
                    cv2.putText(image,str(timer),(int(width/2),int(height/2)),cv2.FONT_HERSHEY_DUPLEX, 7, (255, 0, 255),4)
                else:
                    drawPose((0, 0, 255))
                    cv2.putText(image, "SENDING", (0, int(height / 2)), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 2)
                    cv2.putText(image, "ALERT", ( 0, int((height / 2)+(height/3)) ), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 2)

            elif(not checkFace):
                drawPose((0, 255, 255))
                t2 = time.time()
                #print(t1)

            else:
                drawPose((0, 255, 0))
                t2 = time.time()

        except:
            drawPose((0, 255, 0))
            t2 = time.time()

        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
