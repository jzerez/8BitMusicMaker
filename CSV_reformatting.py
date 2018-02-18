import os
import numpy as np
import csv
'''
Jonathan Zerez
January 2018

This script takes .CSV files and converts them into a large .txt file called
input.txt, suitable for trainig a machine learning algorithm
'''

#Make all incomming pitches limited to the range of a piano
def octave(pitch):
    while(pitch < 20):
        pitch += 12
    while(pitch > 109):
        pitch -= 12
    return pitch

#offset to put the ascii characters in a good range
ascii_offset = 15
output = open("input.txt", 'w')

for files in os.listdir("Training-CSV"):
    if os.stat("Training-CSV/" + files).st_size >= 200000:
        #output csv. Should change to one huge txt file
        csv_file = open("Training-CSV/" + files)
        csv_py = csv.reader(csv_file)

        array = []
        notes = {}

        #dict for keeping track of which notes are on and when
        for pitch in range(128):
            notes[pitch] = False

        for row in csv_py:
            if row[2] == ' Note_on_c' and int(row[5]) > 0:
                row[4] = octave(int(row[4]))
                array.append([int(row[1]), 'on', row[4], False])
            if row[2] == ' Note_on_c' and int(row[5]) == 0:
                row[4] = octave(int(row[4]))
                array.append([int(row[1]), 'off', row[4], False])
            if row[2] == ' Note_off_c':
                row[4] = octave(int(row[4]))
                array.append([int(row[1]), 'off', row[4], False])
            if row[2] == ' Tempo':
                tempo = int(row[3])
            if row[2] == ' Header':
                pulses = int(row[5])

        #sort the array by time
        array = sorted(array, key = lambda line: line[0])

        #create an absolute 1/20th second time step based on tempo and bitrate
        step = (pulses / (tempo / 1000000)) / 20
        index = 0
        time = 0

        print(array[-1][0])

        #iterate the correct number of times given the # of pulses in a timestep
        for time_step in range(round(int(array[-1][0]) / step) + 1):
            #find how many events are occuring at a given time
            if array[index][0] <= time:
                events = 1
                try:
                    while array[index][0] == array[index + events][0]:
                        events += 1
                except:
                    pass

                for i in range(events):
                    #ensure each event has not yet been visited
                    if not array[index + i][3]:
                        #Based on the command, update the bool value for that
                        #pitch in the dictionary
                        if array[index + i][1] == 'on':
                            notes[array[index + i][2]] = True
                            array[index + i][3] = True
                        else:
                            notes[array[index + i][2]] = False
                            array[index + i][3] = True
                index += events
            #write to the .txt file given current state of dictionary
            for note in notes:
                if notes[note]:
                    char = ascii_offset + note
                    output.write(chr(char))
            output.write('\n')
            #proceed to the next unit of time
            time += step

        output.write("NEWSONG\n")
        print(str(files) + " complete!")
