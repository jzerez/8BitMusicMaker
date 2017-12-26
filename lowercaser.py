import os
import csv
num_off = 0
counter = 0

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
for files in os.listdir("../Test-Training-CSV"):
    #input csv
    csv_file = open(files)
    #output csv. Should change to one huge txt file
    output = open("new_" + files, "w+")
    writer = csv.writer(output)
    csv_py = csv.reader(csv_file)

    #valid shows whether an instrument is valid or not
    valid = False
    channel = -1
    for row in csv_py:
        temp = int(row[1]) * 2
        row[1] = ' '+ str(temp)
        writer.writerow(row)


    break
    '''
    for i in range(10):
        print(csv_py[i])
    #print(csv_py)
    '''
