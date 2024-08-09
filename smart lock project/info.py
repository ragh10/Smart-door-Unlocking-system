from pygame import mixer
import time
from email.message import EmailMessage
import smtplib


def contact_info():
    
    
    mixer.init()
                    # sound = mixer.Sound('alarm.wav')
                    # sound.play()
    intro=mixer.Sound('intro.wav')
    intro.play()
    time.sleep(8) 
                    
                    #print('Hello, visiter. There seems to be no one at home. Please provide some information, and I will let the owner know.')
    name=mixer.Sound('name.wav')
    name.play()
    time.sleep(4) 
                    
    fo=open("visitors_list.txt",'a+')
    fo.write("\n")
    fo.write(input("Please enter your name: "))
    fo.write("\n")
                    
    contact_number=mixer.Sound('contact.wav')
    contact_number.play()
    time.sleep(4) 
                    
    fo.write((input("Please enter your contact number: ")))
    fo.close()
                    
    goodbye=mixer.Sound('goodbye.wav')
    goodbye.play()
    time.sleep(4)
                    
    print('Thank you for providing the information. Goodbye!')
    time.sleep(3)
    
contact_info()