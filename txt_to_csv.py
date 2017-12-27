import os
import numpy as np
import csv

txt_file = open("input.txt", "r")
#output csv. Should change to one huge txt file
song_number = 0

input_text = txt_file.read()
songs = input_text.split('NEWSONG\n')
csv_line = [0, 0, 0, 0, 0, 0]

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
    name = str(song_number) + '.csv'
    output = open("midicsv-1.1/" + name, "w+")
    writer = csv.writer(output)
    offset = 0
    lines = song.split('\n')
    num_tracks = lines[-2].split(',')[0]
    csv_line = [0, 0, ' Header', 1, num_tracks, 120]
    writer.writerow(csv_line)
    write_to_csv(track = 1, time = 0, command = ' Start_track')
    csv_line = [1, 0, ' Tempo', 600000]
    writer.writerow(csv_line)

    prev_command = [1, 0, None, None, None, None]
    command = [None, None, None, None, None, None]
    for line in lines:
        if len(line.split(',')) > 3:
            command = line.split(',')

            if (int(command[0]) - offset) - int(prev_command[0]) > 1:
                offset += 1
            command[0] = int(command[0]) - offset
            temp = command
            #convert time from hex to decimal
            command[1] = int(command[1], 16)
            if len(command[2]) > 3:
                write_to_csv(prev_command[0], prev_command[1], command = ' End_track')
                write_to_csv(command[0], command[1], command = ' Start_track')
                write_to_csv(command[0], command[1], command = ' MIDI_port')
                command[2] = ' Program_c'
                writer.writerow(command)
            elif command[2] == 'On':
                command[2] = ' Note_on_c'
                writer.writerow(command)
            elif command[2] == 'Of':
                command[2] = ' Note_off_c'
                writer.writerow(command)
        prev_command = temp


    write_to_csv(command[0], command[1], ' End_track')
    csv_line = [0, 0, ' End_of_file']
    writer.writerow(csv_line)
    print("song number " + str(song_number) + " converted to csv successfully!")
    song_number += 1
