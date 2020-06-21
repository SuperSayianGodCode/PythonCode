# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:44:03 2020

@author: BITTU
"""

# importing module 
import youtube_dl
import threading
#import time

ydl_opts = {}
channel = 1

class myThread (threading.Thread):
   zxtlist=[]
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name+"\n")
      for zxt in myThread.zxtlist:
          myThread.dwl_vid(zxt)
      print ("Exiting " + self.name+"\n")
   def dwl_vid(zxt):
       try:
           with youtube_dl.YoutubeDL(ydl_opts) as ydl:
               ydl.download([zxt])
       except:
           print("An exception occurred\nVideo format missing in site.\nAborting... ")        

while (channel == int(1)): 
	link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- ") 
	myThread.zxtlist.append(link_of_the_video.strip()) 
	channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done "))
    
print(myThread.zxtlist)

for i in range(len(myThread.zxtlist)):
    thread = myThread(i, "Thread-"+str(i), i)
    thread.start()