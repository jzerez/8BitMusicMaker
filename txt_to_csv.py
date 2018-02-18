import os
import subprocess
import csv

'''
Jonathan Zerez
January 2018

This script takes a text file, output.txt, and converts it into a series of
CSV files, ready to be converted back into MIDI
'''


prefix = '8bit_'
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
    name = "midicsv-1.1/" + prefix + str(song_number)
    output = open(name + '.csv', "w+")
    #initialize csv writer object, writer
    writer = csv.writer(output)
    time = 0

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
    writer.writerow([2, 0, ' Program_c', 0, 81])

    for line in lines:
        #array to keep track of which notes are currently on
        activated = []
        shifted = 0
        for letter in line:
            #convert from ascii to midi pitches
            shifted = ord(letter) - ascii_offset
            #update dictionary notes given current commands
            if not notes[shifted]:
                notes[shifted] = True
                writer.writerow([2, time, ' Note_on_c', 0, shifted, 100])

            activated.append(shifted)

        #write to the csv file given the dictionary of notes
        for note in range(128):
            if (note not in activated) and (notes[note]):
                notes[note] = False
                writer.writerow([2, time, ' Note_off_c', 0, note, 0])
        time += 20

    #final, standardized lines to write to the csv.
    write_to_csv(2, time, ' End_track')
    csv_line = [0, 0, ' End_of_file']
    writer.writerow(csv_line)

    print("song number " + str(song_number) + " converted to csv successfully!")
    song_number += 1
