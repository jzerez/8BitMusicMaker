import os
import numpy as np
import csv

def output_row(row):
    string = ""
    for element in row:
        string += element + ','
    string = string[:-1]
    string += '\n'

    return string

def octave(pitch):
    while(pitch < 20):
        pitch += 12
    while(pitch > 109):
        pitch -= 12
    return pitch

#offset to put the unicode characters where i want them
ascii_offset = 15
output = open("input.txt", 'w')
#look at each csv in the training folder
for files in os.listdir("Training-CSV"):
    csv_file = open("Training-CSV/" + files)
    #output csv. Should change to one huge txt file

    csv_py = csv.reader(csv_file)

    array = []
    notes = {}

    for pitch in range(128):
        notes[pitch] = False

    for row in csv_py:
        if row[2] == ' Note_on_c' and int(row[5]) > 0:
            row[4] = octave(int(row[4]))
            array.append([int(row[1]), 'on', row[4], False])
            #print(row[4] + ' On!')
        if row[2] == ' Note_on_c' and int(row[5]) == 0:
            row[4] = octave(int(row[4]))
            array.append([int(row[1]), 'off', row[4], False])
            #print(row[4] + ' Off!')
        if row[2] == ' Note_off_c':
            row[4] = octave(int(row[4]))
            array.append([int(row[1]), 'off', row[4], False])
            #print(row[4] + ' Off!')
        if row[2] == ' Tempo':
            tempo = int(row[3])
        if row[2] == ' Header':
            pulses = int(row[5])

    array = sorted(array, key = lambda line: line[0])


    step = (pulses / (tempo / 1000000)) / 20
    index = 0
    time = 0

    print(array[-1][0])

    #iterate the correct number of timestep times
    for time_step in range(round(int(array[-1][0]) / step) + 1):
        if array[index][0] <= time:
            dupes = 1
            try:
                while array[index][0] == array[index + dupes][0]:
                    dupes += 1
            except:
                #print('last')
                pass
            #if the current element has not been visited and is less than the current time
            #print(array[index])
            for i in range(dupes):
                if not array[index + i][3]:

                    if array[index + i][1] == 'on':
                        notes[array[index + i][2]] = True
                        array[index + i][3] = True
                        #print(str(array[index + i]) + 'ONNNNNNNNNNNNNNNNNNNNNNNNN')
                    else:
                        notes[array[index + i][2]] = False
                        array[index + i][3] = True
                        #print(str(array[index + i]) + 'OFF')
            #check to see the next time value to know whether to update time or not
            index += dupes
        for note in notes:
            if notes[note]:
                char = ascii_offset + note
                output.write(chr(char))
        output.write('\n')
        time += step



    output.write("NEWSONG\n")
    print(str(files) + " complete!")

    '''
    for i in range(10):
        print(csv_py[i])
    #print(csv_py)
    '''
