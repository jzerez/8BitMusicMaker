import requests
from bs4 import BeautifulSoup
import urllib.request as urllib2
import os
import subprocess

home_urls = ["https://www.vgmusic.com/music/console/nintendo/snes/","https://www.vgmusic.com/music/console/nintendo/gameboy/"]
#Sets basis URL
for home_url in home_urls:
    html = urllib2.urlopen(home_url)
    #puts html code into BeautifulSoup object
    soup = BeautifulSoup(html, "lxml")

    #finds all the links
    for link in soup.find_all('a'):
        url = link.get('href')
        #print(url)
        if url != None:
            url_split = url.split(".")
            #find all the midi files
            if len(url_split) > 1 and url_split[1] == "mid":
                csv_name = url_split[0] + ".csv"
                csv_name = csv_name.lower()
                midi_name = url.lower()
                file_url = home_url + url
                #if the file isn't already in the training data
                if (csv_name not in os.listdir("Training-CSV")) :
                    print(url)
                    #download the midi file
                    urllib2.urlretrieve(file_url, midi_name)
                    #convert to csv using midi csv
                    subprocess.call(["midicsv-1.1\Midicsv.exe", midi_name, csv_name])
                    #moves the midi file and new csv file to proper folders. Avoides git memory issues
                    csv_new_home = "Training-CSV/" + csv_name
                    midi_new_home = "Training-MIDI/" + midi_name
                    os.rename(csv_name, csv_new_home)
                    os.rename(midi_name, midi_new_home)
