import subprocess
'''
Jonathan Zerez
January 2018

This script automatically converts csv files into midi files given the format:
<song_#.csv>
'''

num_songs = 2
song_number = 0
#individually convert csv files to midi files
for song in range(num_songs):
    name = 'song_'
    name += str(song_number)
    song_number += 1
    subprocess.call(["midicsv-1.1/csvmidi.exe", name + '.csv', name + '.mid'])
