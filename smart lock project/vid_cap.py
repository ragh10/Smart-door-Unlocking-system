import cv2
import time
import face_recognition
from email.message import EmailMessage



name = "Unknown"
flag=1
def vid_capture():
    print("Video Capturing...")
    start = time.time()

    exec_time = 10


    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            
            out.write(frame)

            # bw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            # face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            # faces = face_cascade.detectMultiScale(bw,1.3,5)

            # for (x,y,w,h) in faces:
            #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)            
            #     font = cv2.FONT_HERSHEY_DUPLEX
            #     cv2.putText(frame, name, ((h*2) + 6, (w*2) - 6), font, 1.0, (255, 0, 0), 1)
            
            
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = small_frame[:, :, ::-1]

            face_names=['unknown']
            face_locations = face_recognition.face_locations(rgb_small_frame)
            for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

        # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2) #image, start_point, end_point, color, thickness

        # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                cv2.imshow('frame',frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if time.time() > start + exec_time:
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
vid_capture()
