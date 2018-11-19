
from Tkinter import *
import locale
import threading
import time
import requests
import json
import traceback
import feedparser

import os

from PIL import Image, ImageTk
from contextlib import contextmanager

from scripts.vars import *
from opencv.Facerec import *

global person_name
person_name = None

class Camera(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'Face Info'
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)
        self.labelContainer = Frame(self, bg="black")
        self.labelContainer.pack(side=TOP)
        self.do_loop()

    def do_camera(self):
        try:
            # remove all children
            for widget in self.labelContainer.winfo_children():
                widget.destroy()
            # take photo
            os.system("raspistill -o image.png -k -t 0 -p '200,100,600,400'")
            # perform recognition
            result = do_prediction_single("image.png")
            text = Label(self.labelContainer, text=result, font=('Helvetica', medium_text_size), fg="white", bg="black")
            text.pack(side=BOTTOM, anchor=W)

        except Exception as e:
            traceback.print_exc()
            # print "Error: %s. Cannot get news." % e

    def do_loop(self):
        thread1 = threading.Thread(target=do_camera)
        
        #if __name__=="__main__": self = 2
        #self.do_camera
        thread1.start()
        
        # not needed?
        #thread1.join()
        
        self.after(10000, self.do_loop)
        # self.after(10000, self.do_camera)

        
