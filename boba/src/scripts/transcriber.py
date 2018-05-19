import numpy as np
# import matplotlib.pyplot as plt
# import IPython.display as ipd
# from IPython.display import display
# from ipywidgets import interact

import sys
# sys.path.append("../common")
from util import *
from music21 import *

# import fmp

# %matplotlib inline
# %matplotlib notebook
# plt.rcParams['figure.figsize'] = (12, 4)

' System arguments are in the form $python transcriber.py "file_name_here.wav" '
print "name: ", sys.argv[0]
if len(sys.argv) == 2:
	song_name = sys.argv[1]
	print "song name:", song_name
else:
	print "Not correct number of arguments"
	exit


' Load in the song name '
x = load_wav(song_name) #load in the song
sr = 22050 #sample rate
winsize = 2205 #window size

num_win = len(x)/winsize

peaks = []
# peaks = np.zeros(num_win)

for win_idx in range(num_win):
	start = win_idx * winsize
	end = win_idx * winsize + winsize

	' set up, multiply by hanning curve and zpad '
	win = x[start:end]
	x_w = zpad(win * np.hanning(len(win)), winsize*2)

	' perform fft this will return contribution ' 
	ft = np.fft.rfft(x_w)

	' take abs and get rid of negatives '
	magft = np.abs(ft)

	#get max peak
	#working
	# peak = np.argmax(magft)
	# peaks[win_idx] = peak

	' find all peaks that are above certain threshold and return index(es) '
	pks = find_peaks(magft, 0.8)
	peaks.append(pks)
	# peaks[win_idx] = pks
	
peaks = np.array(peaks)
# print peaks


strm = stream.Stream()
for vals in peaks:
	# print vals
	rest = False
	notes_in_chord = []
	' convert the set of peaks to frequencies '
	freqs = bin_to_freq(vals, sr, winsize) #peaks, sr, winsize

	' convert frequencies to pitches'
	pitches = freq_to_pitch(freqs)

	for pitch in pitches:
		print pitch
		'convert pitches to spn and add to chord '
		# print note.Note(pitch_to_spn(int(round(pitch))))
		note_to_add = pitch_to_spn(int(round(pitch)))
		if note_to_add == "-1":
			rest = True
		else:
			notes_in_chord.append(note.Note(note_to_add, quarterLength=1.5))

	if rest == False:
		' make chord and add it to strm '
		chord_value = chord.Chord(notes_in_chord)
		print chord_value
		strm.append(chord_value)
	else:
		strm.append(note.Rest())

' show/write strm '
# strm.show()
fp = strm.write("musicxml", "../sheets/score.xml")



# freqs = bin_to_freq(peaks, sr, winsize) #peaks, sr, winsize
# pitches = freq_to_pitch(freqs)


# strm = stream.Stream()
# for pitch in pitches:
# 	strm.append(note.Note(pitch_to_spn(int(round(pitch)))))

# strm.show()

#for now discard ending part, can add 1 to num_win instead
# print len(x)