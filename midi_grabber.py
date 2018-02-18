import requests
from bs4 import BeautifulSoup
import urllib.request as urllib2
import os
import subprocess
import sys

'''
Jonathan Zerez
January 2018

This script takes URLs from the command line, or as manual inputs and tries to
scrape MIDI files from them, and convert said files into CSV files.
'''

if len(sys.argv) < 2:
    home_urls = ["http://www.piano-e-competition.com/midi_2002.asp",
                "http://www.piano-e-competition.com/midi_2004.asp",
                "http://www.piano-e-competition.com/midi_2006.asp",
                "http://www.piano-e-competition.com/midi_2008.asp",
                "http://www.piano-e-competition.com/midi_2009.asp",
                "http://www.piano-e-competition.com/midi_2011.asp",
                ]

else:
    home_urls = sys.argv[1:]


num_songs = 0
#Sets basis URL
base_url = "http://www.piano-e-competition.com/"
for home_url in home_urls:
    try:
        html = urllib2.urlopen(home_url)
        #puts html code into BeautifulSoup object
    except urllib2.HTTPError:
        print("file error")
        continue
    soup = BeautifulSoup(html, "lxml")

    #finds all the links
    for link in soup.find_all('a'):
        url = link.get('href')
        print(url)

        if url != None:
            url = base_url + url
            print(url)

            #find all the midi files
            if len(url.split('.')) > 3 and url.split('.')[-1] == "MID":
                print(url)
                num_songs += 1

                csv_name = url.split('/')[-1].split('.')[0] + ".csv"
                csv_name = csv_name.lower()
                midi_name = url.split('/')[-1].lower()
                file_url = url
                #if the file isn't already in the training data
                if (csv_name not in os.listdir("Training-CSV")) :
                    print(url)
                    #download the midi file
                    try:
                        urllib2.urlretrieve(file_url, midi_name)
                    except:
                        continue

                    #convert to csv using midi csv
                    subprocess.call(["midicsv-1.1\Midicsv.exe", midi_name, csv_name])
                    #moves the midi file and new csv file to proper folders. Avoides git memory issues
                    csv_new_home = "Training-CSV/" + csv_name
                    midi_new_home = "Training-MIDI/" + midi_name
                    os.rename(csv_name, csv_new_home)
                    os.rename(midi_name, midi_new_home)

print(str(num_songs) + " songs downloaded!")
