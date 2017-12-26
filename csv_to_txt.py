import os
import numpy as np
import csv

#look at each csv in the training folder
for files in os.listdir("Training-CSV"):
    #input csv
    csv_file = open("Training-CSV/" + files)
    #output csv. Should change to one huge txt file
    output = open("Training-CSV-Refined/" + files, "w+")
    writer = csv.writer(output)
    csv_py = csv.reader(csv_file)

    #valid shows whether an instrument is valid or not
    valid = True
    for row in csv_py:
        if row[2] == ' Tempo':
            #convert the time to use 100 bpm
            time_conversion = int(row[3]) / 600000
        if (row[2] == ' Program_c'):
            #check and consolodate instruments based on groupings from wikipedia
            instrument = int(row[4])

            valid = True
            if instrument < 9:
                row[3] = ' 5'
            elif instrument < 17:
                row[3] = ' 12'
            elif instrument < 25:
                row[3] = ' 19'
            elif instrument < 33:
                row[3] = ' 28'
            elif instrument < 41:
                row[3] = ' 39'
            elif instrument < 49:
                row[3] = ' 41'
            elif instrument < 57:
                row[3] = ' 56'
            elif instrument < 65:
                row[3] = ' 63'
            elif instrument < 73:
                row[3] = ' 66'
            elif instrument < 81:
                row[3] = ' 80'
            elif instrument < 89:
                row[3] = ' 81'
            elif instrument < 97:
                row[3] = ' 90'
            elif instrument < 105:
                row[3] = ' 99'
            elif instrument < 113:
                valid = False
            elif instrument < 121:
                row[3] = ' 119'
            else:
                valid = False

            #Need to do: write out to the txt or csv file
            if valid:


        #Need to do: write out to txt file
        if(row[2] == ' Note_on_c' and valid):
            row[1] = ' ' + str(int((int(row[1]) * time_conversion)))
            print(row)
            #writer.writerow(row)

    break
    '''
    for i in range(10):
        print(csv_py[i])
    #print(csv_py)
    '''
