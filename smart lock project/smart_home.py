import face_recognition
import cv2 #Open Computer Vision
import numpy as np
import os
import time
from pygame import mixer
from email.message import EmailMessage
import smtplib



import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#from send_mail import sendmail
#import send_mail 

#from receive_mail import receivemailq

video_capture = cv2.VideoCapture(0)

print('Capturing video..')
known_face_encodings = [] #an empty list
path="faces/"
for i, x in zip(os.listdir(path),range(0,len(os.listdir(path)))):
    img_path=os.path.join(path,i)
    img=face_recognition.load_image_file(img_path)
    encoding = face_recognition.face_encodings(img)[0] #binary bit stream
    known_face_encodings.append(encoding)
    
    
    
    if x==0 and i != None:
        print('Face encodings of all the images in the known directory are as follows:')
        print('The first image and its encoding: \n')
        plt.axis('off')
        plt.imshow(img)
        plt.show()
        print('\n Face encodings of the first image =', known_face_encodings[0], '\n')
        
        
    elif x==1 and i != None:    
        
        
        print('The second image and its encoding: \n')
        plt.axis('off')
        plt.imshow(img)
        plt.show()
        print('\n Face encodings of the second image =', known_face_encodings[1], '\n')
        
    
    elif x==2 and i != None:    
        
        
        print('The third image and its encoding: \n')
        plt.axis('off')
        plt.imshow(img)
        plt.show()
        print('\n Face encodings of the third image =', known_face_encodings[2], '\n')
    elif x==3 and i != None:    
        
        
        print('The fourth image and its encoding: \n')
        plt.axis('off')
        plt.imshow(img)
        plt.show()
        print('\n Face encodings of the fourth image =', known_face_encodings[3], '\n')
    
    elif x==4 and i != None:    
        
        
        print('The fourth image and its encoding: \n')
        plt.axis('off')
        plt.imshow(img)
        plt.show()
        print('\n Face encodings of the fourth image =', known_face_encodings[4], '\n')
    
    elif x==5 and i != None:    
        
        
        print('The fourth image and its encoding: \n')
        plt.axis('off')
        plt.imshow(img)
        plt.show()
        print('\n Face encodings of the fourth image =', known_face_encodings[5], '\n')
        
        
        
   
        
        
  
known_face_names = ['Obama', 'raghav'  , 'Ram','rahul','kohli']
# for i in os.listdir(path):
#     name=i.split('.')[0]
#     known_face_names.append(name)

def capture():
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    count=0
    flag=0
    name = "Unknown"
    flag1 = 0
    flag2 = 0
    flag3=0

    while True:
        ret, frame = video_capture.read()
        # bw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # faces = face_cascade.detectMultiScale(bw,1.3,5)
        crop_img = []
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]


        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        if flag1==0:
            print('Face encodings of faces captured by the web-camera  =', face_encodings)
            flag1=1
            #face_encoding = face_recognition.face_encodings(image)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    #name = "Unknown"
            if flag2==0:
                print('Matches  =', matches)
                flag2=1
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            if flag3==0:    
                print('Euclidian Distances are \n',face_distances)
                flag3=1
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            else:
                name = "Unknown"
            
        face_names.append(name)
        # for (x,y,w,h),name in zip(faces,face_names):
        #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)            
        #     font = cv2.FONT_HERSHEY_DUPLEX
        #     cv2.putText(frame, name, ((h*2) + 6, (w*2) - 6), font, 1.0, (255, 0, 0), 1)
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

        # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 1) #image, start_point, end_point, color, thickness

        # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)    
            #crop_img = frame[y:y+h,x:x+w]
            #crop_img = frame[right:right+left,top:top+bottom]
            #cv2.imwrite("D:/python/projects/smart_home_project/smart_home_new/Smart-Door-Unlocking-System-Using-Face-Recognition-master/detected_face/temp.png",crop_img)
            
            

        if name == "Unknown":
            
            #cv2.imshow("performing_face_Detection",frame)
            count = count + 1
            if count == 10:
                    # video_capture.release()
                    # cv2.destroyAllWindows()
                
                
    
                
                #execfile('send_mail.py')
                exec(open("send_mail.py").read())
                #time.sleep(60)
                flag=1
                break
                

                
            else:
                continue

        elif name != "Unknown" and flag==0:
            #cv2.putText(frame, name, ((h*4) + 6, (w*4) - 6), font, 1.0, (255, 0, 0), 1)
            #cv2.imshow("performing_face_Detection",frame)
            print("Hello,", known_face_names[best_match_index],"\n Welcome home.","\nUnlocking the door.")
            #print('Opening the door...'+name)
            #os.system('python3 lock.py')
            #print('2')
            #print(name)
            flag=1
            #break

            #os.remove("detected_face/temp.png")
        
            
            
            
        
        cv2.imshow("performing_face_Detection",frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        # if flag == 1:
        #     break
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()                
capture()
