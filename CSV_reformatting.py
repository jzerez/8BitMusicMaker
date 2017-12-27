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


#look at each csv in the training folder
for files in os.listdir("Training-CSV"):
    num_tracks = 0
    #input csv
    csv_file = open("Training-CSV/" + files)
    #output csv. Should change to one huge txt file
    output = open("input.txt", 'a')

    csv_py = csv.reader(csv_file)

    #valid shows whether an instrument is valid or not
    valid = False
    channel = -1
    for row in csv_py:
        if row[2] == ' Header':
            #convert ticks per quater note to 120
            time_conversion_head = 120 / int(row[5])
        if row[2] == ' Tempo':
            #convert the time to use 100 bpm
            time_conversion_tempo = int(row[3]) / 600000

        if (row[2] == ' Program_c'):
            #check and consolodate instruments based on groupings from wikipedia
            instrument = int(row[4])

            valid = True
            if instrument < 9:
                row[4] = '5'
                channel = 0
            elif instrument < 17:
                row[4] = '12'
                channel = 1
            elif instrument < 25:
                row[4] = '18'
                channel = 2
            elif instrument < 33:
                row[4] = '28'
                channel = 3
            elif instrument < 41:
                row[4] = '39'
                channel = 4
            elif instrument < 49:
                row[4] = '41'
                channel = 5
            elif instrument < 57:
                row[4] = '56'
                channel = 6
            elif instrument < 65:
                row[4] = '63'
                channel = 7
            elif instrument < 73:
                row[4] = '66'
                channel = 8
            elif instrument < 81:
                row[4] = '80'
                channel = 9
            elif instrument < 89:
                row[4] = '81'
                channel = 10
            elif instrument < 97:
                row[4] = '90'
                channel = 11
            elif instrument < 105:
                row[4] = '99'
                channel = 12
            elif instrument < 113:
                valid = False
                channel = -1
            elif instrument < 121:
                row[4] = '119'
                channel = 13
            else:
                valid = False
                channel = -1

            #Need to do: write out to the txt or csv file
            if valid:
                num_tracks += 1
                row[0] = str(1 + num_tracks)
                row[1] = str(hex(int((int(row[1]) * time_conversion_tempo * time_conversion_head))).split('x')[-1])
                row[2] = 'Prog'
                row[3] = str(channel)
                row[4] = str(int(row[4]))
                output.write(output_row(row))

        #Need to do: write out to txt file
        if(row[2] == ' Note_on_c' and valid):
            row[0] = str(1 + num_tracks)
            row[1] = str(hex(int((int(row[1]) * time_conversion_tempo * time_conversion_head))).split('x')[-1])
            row[2] = 'On'
            row[3] = str(channel)
            row[4] = str(int(row[4]))
            row[5] = str(int(row[5]))
            output.write(output_row(row))


        if(row[2] == ' Note_off_c' and valid):
            row[0] = str(1 + num_tracks)
            row[1] = str(hex(int((int(row[1]) * time_conversion_tempo * time_conversion_head))).split('x')[-1])
            row[2] = 'Of'
            row[3] = str(channel)
            row[4] = str(int(row[4]))
            row[5] = str(int(row[5]))
            output.write(output_row(row))
            #writer.writerow(row)
    print(str(files) + " complete!")
    output.write("NEWSONG\n")


    '''
    for i in range(10):
        print(csv_py[i])
    #print(csv_py)
    '''
