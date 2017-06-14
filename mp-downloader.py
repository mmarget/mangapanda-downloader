#!/usr/bin/env python3
#Manga downloader for complete chapters or series off of www.mangapanda.com

import requests
from bs4 import BeautifulSoup
import os
import sys

homepage = "http://www.mangapanda.com/"

#Enter Manga here
manga = "dragon-ball"

#Enter your your starting and ending chapter here
min_chapter = 1
max_chapter = 520
filepath = "./" + manga + "/"

#create subfolder for images
if not os.path.exists(filepath):
    os.makedirs(filepath)

for chap in (range(min_chapter, max_chapter + 1)):

    #check for length of chapter
    contents = BeautifulSoup(requests.get(homepage + manga + "/" + str(chap)).content, 'html.parser')
    pages = len(contents.find_all("option"))

    if pages == 0: 
        print("Chapter " + str(chap) + " not found, skipping..")i

    for page in range(1, pages + 1):
        #neat progress bar
        sys.stdout.write('\r')
        sys.stdout.write("Downloading chapter %d of %d [%-50s] page %d/%d" % (chap, max_chapter, '='*int((page/pages)*50), page, pages))
        sys.stdout.flush()

        #get image url
        contents = BeautifulSoup(requests.get(homepage + manga + "/" + str(chap) + "/" + str(page)).content, 'html.parser')
        imgurl = contents.find(id="imgholder").find("img").get("src")

        #save to file
        f = open(filepath + manga + "-" + str(chap).zfill(4) + "-" + str(page).zfill(4) + ".jpg", 'wb')
        f.write(requests.get(imgurl).content)
        f.close()
    sys.stdout.write('\n')
