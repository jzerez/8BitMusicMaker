import os
import numpy as np
import csv

txt_file = open("output.txt", "r")
#output csv. Should change to one huge txt file
song_number = 0

input_text = txt_file.read()
songs = input_text.split('NEWSONG\n')
csv_line = [0, 0, 0, 0, 0, 0]
ascii_offset = 15

def write_to_csv(track, time, command):
    if command == ' Start_track':
        csv_line = [track, 0, command]
        writer.writerow(csv_line)
    if command == ' End_track':
        csv_line = [track, time, command]
        writer.writerow(csv_line)
    if command == ' MIDI_port':
        csv_line = [track, 0, command, 0]

for song in songs:
    #initialize dict for pitches
    notes = {}
    for pitch in range(128):
        notes[pitch] = False

    #create csv name and write to file in folder midicsv-1.1
    name = str(song_number) + '.csv'
    output = open("midicsv-1.1/" + name, "w+")
    #initialize csv writer object, writer
    writer = csv.writer(output)
    offset = 0

    #split song into lines (1/20th second intervals)
    lines = song.split('\n')

    #write initial, static header information to the csv
    csv_line = [0, 0, ' Header', 1, 2, 200]
    writer.writerow(csv_line)
    write_to_csv(track = 1, time = 0, command = ' Start_track')
    csv_line = [1, 0, ' Tempo', 500000]
    writer.writerow(csv_line)
    write_to_csv(1, 0, command = ' End_track')
    write_to_csv(2, 0, command = ' Start_track')
    write_to_csv(2, 0, command = ' MIDI_port')
    writer.writerow([2, 0, ' Program_c', 0, 80])

    for line in lines:
        activated = []
        for letter in line:
            shifted = int(letter) - ascii_offset
            if not notes[shifted]:
                notes[shifted] = True
                writer.writerow([2, time, ' Note_on_c', 0, shifted, 100])

            activated.append(shifted)
            for note in range(128):
                if note is not in activated and notes[note]:
                    notes[note] = False
                    writer.writerow([2, time, ' Note_off_c', 0, shifted, 0])

        time += 20

    write_to_csv(2, time, ' End_track')
    csv_line = [0, 0, ' End_of_file']
    writer.writerow(csv_line)
    print("song number " + str(song_number) + " converted to csv successfully!")
    song_number += 1
