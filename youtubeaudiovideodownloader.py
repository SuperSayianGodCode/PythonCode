#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:30:22 2020

@author: rahul
"""
'''Retrieve metadata such as viewcount, duration, rating, author, description.'''
'''import pafy 

# url of video 
url = "https://www.youtube.com/watch?v=Ns4LCeeOFS4&t=320s"

# instant created 
video = pafy.new(url) 

# print title 
print(video.title) 

# print rating 
print(video.rating) 

# print viewcount 
print(video.viewcount) 

# print author & video length 
print(video.author, video.length) 

# print duration, likes, dislikes & description 
print(video.duration, video.likes, video.dislikes, video.description)''' 
############################################################################################################3

'''Download best resolution video regardless of extension'''
import pafy 

url = "https://youtu.be/8rmBYN6HhmM"
video = pafy.new(url) 

streams = video.streams 
for i in streams: 
	print(i) 
	
# get best resolution regardless of format 
best = video.getbest() 

print(best.resolution, best.extension) 

# Download the video 
best.download() 
#################################################################################################################

'''Download video of a particular format specified (let say .mp4)'''
import pafy 

url = "https://youtu.be/8rmBYN6HhmM"
video = pafy.new(url) 

streams = video.streams 
for i in streams: 
	print(i) 
	
# get best resolution of a specific format 
# set format out of(mp4, webm, flv or 3gp) 
best = video.getbest(preftype ="mp4") 

best.download() 
################################################################################################################

'''Download a specific format audio.'''
import pafy 

url = "https://youtu.be/8rmBYN6HhmM"
video = pafy.new(url)

audiostreams = video.audiostreams
for i in audiostreams: 
	print(i.extension, i.get_filesize()) 

audiostreams[3].download() 
##################################################################################################################

'''Download the bestaudio'''
import pafy 

url = "https://youtu.be/8rmBYN6HhmM"
video = pafy.new(url) 

bestaudio = video.getbestaudio() 
bestaudio.download() 
