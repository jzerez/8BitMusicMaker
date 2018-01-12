# 8BitMusicMaker
This project was originally intended to only generate music in the same style as classic retro video games, however, it can be used to generate hypothetically any genre of music.

#How to run:
First download and reformat MIDI files by running the following scripts. As any number of URLs can be passed into midi_grabber.py. If no URLs are passed in, the default case is a series of URLs for MIDI files whose genre is dance.
'''bash
python midi_grabber.py <URL1> <URL2> <URL3>
python txt_to_csv.py
'''
Next, pass input.txt to [Andrej Karpathy's Character Based Recurrent Neural Network](https://github.com/karpathy/char-rnn) in order to generate new text.

With the new text saved in the main folder, run the following scripts
'''bash
python txt_to_csv.py
python generate_midi.py
'''


# How it works:
A web scraper with a user specified list of URLs to pull from downloads all available MIDI files from the specified URLS. It then uses [Fourmuliab's Midicsv](http://www.fourmilab.ch/webtools/midicsv/) to convert MIDI files to CSV files. A reformatting script then converts all CSV files into one text file suitable for training. It reformats it in such a way that makes more sense for the LSTM used for training, and also compresses the file size considerably. The text is then fed into [Andrej Karpathy's Character Based Recurrent Neural Network](https://github.com/karpathy/char-rnn). The output of that is then fed into a script that takes text and converts it back into MIDI.
