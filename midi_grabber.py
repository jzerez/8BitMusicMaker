import requests
from bs4 import BeautifulSoup
import urllib.request as urllib2
import os
import subprocess
import admin
if not admin.isUserAdmin():
        admin.runAsAdmin()

home_url = "https://www.vgmusic.com/music/computer/amstrad/amstradcpc/"
html = urllib2.urlopen(home_url)
soup = BeautifulSoup(html, "lxml")
for link in soup.find_all('a'):
    url = link.get('href')
    #print(url)

    if url != None:
        url_split = url.split(".")
        if len(url_split) > 1 and url_split[1] == "mid":
            print(url)
            csv_name = url_split[0] + ".csv"
            file_name = url_split[0] + ".mid"
            file_url = home_url + url
            urllib2.urlretrieve(file_url, file_name)
            subprocess.call(["C:\\Users\jzerez\Documents\GitHub\8BitMusicMaker-Master\midicsv-1.1", file_name, csv_name])
