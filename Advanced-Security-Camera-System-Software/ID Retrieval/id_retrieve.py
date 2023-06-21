import os
from os import listdir
from os.path import isfile, join
import shutil
##FACE DETECTION LIBRARY
import cv2
import face_recognition
##RECOGNIZED
rec_path = "C://Users/Dhana/PycharmProjects/IdentityRetrieval/output/recognized/"

##FUNCTIONS
def faceDetected(image):
    try:
        encode = face_recognition.face_encodings(image1)[0]
        print(encode)
        return True
    except:
        return False

def compareFace(encode1,encode2):
    try:
        #print(encode1)
        #print(encode2)
        print(face_recognition.compare_faces(encode1, encode2)[0])
        if(face_recognition.compare_faces(encode1,encode2)[0]):

            #print(face_recognition.compare_faces([encodeElon],encode))
            return True
        return False
    except:
        return False
        pass

def copyImage(image,name):
    shutil.copyfile(image,rec_path+name)

def createTxt(path,name):
    f = open(path,"r")
    lines = f.read()
    f.close()
    f_new = open(rec_path+name[0:-4]+".txt","w")
    f_new.write(lines)
    f_new.close()
    print(rec_path+name[0:-4]+".txt")

##DATABASE
DB_path = "C://Users/Dhana/PycharmProjects/IdentityRetrieval4/ID database/"
os.chdir(DB_path)
my_list = os.listdir(DB_path)
print(my_list)

##OUTPUT PICTURES
output_path = "C://Users/Dhana/PycharmProjects/IdentityRetrieval/output/people/"
list_of_images = [f for f in listdir(output_path) if isfile(join(output_path, f))]

count_output = 0
total_output = len(list_of_images)
for i in list_of_images:
    print(str(count_output)+"/"+str(total_output))
    count_output+=1
    #image2 = cv2.imread(output_path+i)
    image2 = face_recognition.load_image_file(output_path+i)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    try:
        encode2 = face_recognition.face_encodings(image2)[0]
        #encode = face_recognition.face_encodings(image)[0]
    except:
        print("nope")
    #cv2.imshow("K",image2)
    #cv2.waitKey(0)
    # if(not faceDetected(image2)):
    #     print(faceDetected(image2))
    #     continue
    for j in my_list:
        os.chdir(DB_path+j)
        n_db_images = [f for f in listdir(DB_path+j) if isfile(join(DB_path+j, f))]
        count=0
        total=0
        for k in n_db_images:
            if(k.endswith('jpeg')):
                print(k)
                total+=1
                #image1 = cv2.imread(k)
                image1 = face_recognition.load_image_file(k)
                image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                try:
                    encode1 = face_recognition.face_encodings(image1)[0]
                    #print(encode2)
                    if (face_recognition.compare_faces([encode1], encode2)[0]):
                        # print(face_recognition.compare_faces([encodeElon],encode))
                        count += 1
                except:
                    print("nope2")
                # if(compareFace(encode1,encode2)):
                #     print(k)
                #     count+=1

        #print(count)
        if(count>=len(n_db_images)/2):
            #copyImage(,i)
            print(shutil.copy(output_path+i, rec_path + i))
            createTxt(DB_path+j+"/details.txt",i)
            break
