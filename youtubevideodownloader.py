#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 23:48:25 2020

@author: rahul
"""

# importing module 
import youtube_dl 

ydl_opts = {} 

def dwl_vid(): 
	with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
		ydl.download([zxt]) 

channel = 1
while (channel == int(1)): 
	link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- ") 
	zxt = link_of_the_video.strip() 

	dwl_vid() 
	channel = int(input("Enter 1 if you want to download more videos \nEnter 0 if you are done ")) 
########################################################################################################

#Downloading a single video
  
#importing the module 
from pytube import YouTube 

#where to save 
SAVE_PATH = "E:/" #to_do 

#link of the video to be downloaded 
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

try: 
	#object creation using YouTube which was imported in the beginning 
	yt = YouTube(link) 
except: 
	print("Connection Error") #to handle exception 

#filters out all the files with "mp4" extension 
mp4files = yt.filter('mp4') 

yt.set_filename('GeeksforGeeks Video') #to set the name of the file 

#get the video with the extension and resolution passed in the get() function 
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
	#downloading the video 
	d_video.download(SAVE_PATH) 
except: 
	print("Some Error!") 
print('Task Completed!') 

##########################################################################################################

#Downloading multiple videos

from pytube import YouTube 

#where to save 
SAVE_PATH = "E:/" #to_do 

#link of the video to be downloaded 
link=["https://youtu.be/uasV7DyblKk", 
	"https://youtu.be/ipm5hDz9zG0"
	]#list of youtube links which need to be downloaded 
for i in link: 
	try: 
		#object creation using YouTube which was imported in the beginning 
		yt = YouTube(i) 
	except: 
		print("Connection Error") #to handle exception 
	
	#filters out all the files with "mp4" extension 
	mp4files = yt.filter('mp4') 

	#get the video with the extension and resolution passed in the get() function 
	d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
	try: 
		#downloading the video 
		d_video.download(SAVE_PATH) 
	except: 
		print("Some Error!") 
print('Task Completed!') 

##########################################################################################################
'''Download multiple videos using File Handling'''
from pytube import YouTube 

#where to save 
SAVE_PATH = "E:/" #to_do 

#link of the video to be downloaded 
link=open('links_file.txt','r') #opening the file 

for i in link: 
	try: 
		#object creation using YouTube which was imported in the beginning 
		yt = YouTube(i) 
	except: 
		print("Connection Error") #to handle exception 
	
	#filters out all the files with "mp4" extension 
	mp4files = yt.filter('mp4') 
	#get the video with the extension and resolution passed in the get() function 
	d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
	try: 
		#downloading the video 
		d_video.download(SAVE_PATH) 
	except: 
		print("Some Error!") 
print('Task Completed!') 
