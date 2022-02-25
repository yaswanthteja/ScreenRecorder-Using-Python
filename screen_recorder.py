#To create a simple screen recorder using python

from PIL import ImageGrab
import cv2
import numpy as np
from tkinter import *

def record_screen():
    #Obtain image dimensions
    #Screen capture 
    image = ImageGrab.grab()
    #Convert the object to numpy array
    img_np_arr = np.array(image)
    #Extract and print shape of array
    shape = img_np_arr.shape
    print(shape)

    #Create a video writer
    screen_cap_writer = cv2.VideoWriter('screen_recorded.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 50, (shape[1], shape[0]))   # You can use .mp4 instead of .avi

    #To View the screen recording in a separate window (OPTIONAL)
    #This is optional. Use the aspect ratio scaling if you wish to view the screen recording simultaneously
    #Low scale_by_percent implies smaller window
    scale_by_percent = 50 
    width = int(shape[1] * scale_by_percent / 100)
    height = int(shape[0] * scale_by_percent / 100)
    new_dim = (width, height)
    #Record the screen
    #Condition to keep recording as a video
    while True:
        #Capture screen
        image = ImageGrab.grab()
        #Convert to array
        img_np_arr = np.array(image)
        #OpenCV follows BGR and not RGB, hence we convert
        final_img = cv2.cvtColor(img_np_arr, cv2.COLOR_RGB2BGR)
        #Write to video 
        screen_cap_writer.write(final_img)
        #OPTIONAL: To view your screen recording in a separate window, resize and use imshow()
        '''
            If you choose to view the screen recording simultaneously,
            It will be displayed and also recorded in your video. 
        '''
        image = cv2.resize(final_img, (new_dim))
        cv2.imshow("image", image)
        #Stop and exit screen recoding if user presses 'e' (You can put any letter)
        if cv2.waitKey(1) == ord('e'):
            break
        
    #Release the created the objects
    screen_cap_writer.release()
    cv2.destroyAllWindows()


#Define the user interface
screen_recorder  = Tk()
screen_recorder.geometry("340x220")
screen_recorder.title("Screen Recorder")

bg_img = PhotoImage(file = "images/outputbackground.png")
  
# Show image using label
label1 = Label( screen_recorder, image = bg_img, bd=0)
label1.pack()
  
#Create and place the components
title_label = Label(screen_recorder, text=" Screen Recorder",font=("Ubuntu Mono", 16), bg="#02b9e5")
title_label.place(relx=0.5,rely=0.1, anchor=CENTER)
info_label = Label(screen_recorder, text="Enter 'e' to exit screen recording", bg="#02b9e5")
info_label.place(relx=0.5,rely=0.3, anchor=CENTER)
screen_button = Button(screen_recorder, text="Record Screen", command=record_screen, relief= RAISED)
screen_button.place(relx=0.5,rely=0.6, anchor=CENTER)

screen_recorder.mainloop()
