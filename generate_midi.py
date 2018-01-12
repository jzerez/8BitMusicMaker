import subprocess
num_songs = 2
song_number = 0
for song in range(num_songs):
    name = 'song_'
    name += str(song_number)
    song_number += 1
    subprocess.call(["midicsv-1.1/csvmidi.exe", name + '.csv', name + '.mid'])
