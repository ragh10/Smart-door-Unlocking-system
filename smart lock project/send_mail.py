from email.message import EmailMessage
import smtplib
import time
import cv2
import face_recognition
from pygame import mixer

#from vid_cap import vid_capture
#from info import contact_info

def sendmail():
    #vid_capture()
    exec(open("vid_cap.py").read())
    #contact_info()
    exec(open("info.py").read())
    email_id='rkaushik514@gmail.com'  #saved as 'test_id' #'environ' is a dictionary
    email_id_password='irlcvnquyqyemnyf'
    
    msg=EmailMessage() #EmailMessage is a class
    msg['From']=email_id
    msg['To']=email_id
    msg['Subject']='Check out, someone is knocking at your door'
    msg.set_content('Here are a video of the visitor recorded, and the contact information.') #Body of the email
    
    
    #attach the visitor's image
    files=['output.mp4']
    for file in files:
        with open(file,'rb') as f:
            file_data=f.read()
            #file_type=imghdr.what(f.name) #returns, for example, 'png' only, which is 'subtype'
            file_name=f.name
            #print(f.name) --> returns image_name.extension
        msg.add_attachment(file_data, maintype='application',subtype='octet-stream',filename=file_name)
    
    
    
    #Attach the document
    files=['visitors_list.txt']
    for file in files:
        with open(file,'rb') as f:
            file_data=f.read()
            file_name=f.name
            #print(f.name) --> returns image_name.extension
    msg.add_attachment(file_data, maintype='application',subtype='octet-string',filename=file_name)
    
    
    #with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #Using the SMTP Class. Secure Sockets Layer (SSL) is a standard security technology for establishing an encrypted link between a server and a client
    #SMTP - Simple Mail Transfer Protocol 
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:    
        smtp.login(email_id,email_id_password)
        smtp.send_message(msg)
        
        try:
            print('The email is sent!')
        except:
            print('Sorry! There was an error!')


sendmail()











