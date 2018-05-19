import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
from IPython.display import display
from ipywidgets import interact

import sys
# sys.path.append("../common")
from util import *
from music21 import *

# import fmp

# %matplotlib inline
# %matplotlib notebook
plt.rcParams['figure.figsize'] = (12, 4)


x = load_wav("thousandyears.wav")
sr = 22050
winsize = 2205

num_win = len(x)/winsize

#peaks
peaks = []
# peaks = np.zeros(num_win)

for win_idx in range(num_win):
	start = win_idx * winsize
	end = win_idx * winsize + winsize
	print start, end
	#set up, mult by hanning
	win = x[start:end]
	x_w = zpad(win * np.hanning(len(win)), winsize*2)

	#perform fft
	ft = np.fft.rfft(x_w)

	#take abs and get rid of negatives
	magft = np.abs(ft)

	#get max peak
	#working
	# peak = np.argmax(magft)
	# peaks[win_idx] = peak

	#testing
	pks = find_peaks(magft,0.8)
	# pks = magft[np.where( magft > 10 )]
	# print pks
	# pks.shape
	peaks.append(pks)
	# peaks[win_idx] = pks
	
peaks = np.array(peaks)
# print peaks


strm = stream.Stream()
for vals in peaks:
	print vals
	notes_in_chord = []
	freqs = bin_to_freq(vals, sr, winsize) #peaks, sr, winsize
	pitches = freq_to_pitch(freqs)
	for pitch in pitches:
		print note.Note(pitch_to_spn(int(round(pitch))))
		notes_in_chord.append(note.Note(pitch_to_spn(int(round(pitch)))))
	chord_value = chord.Chord(notes_in_chord)
	# print chord_value
	strm.append(chord_value)

strm.show()
# fp = strm.write("musicxml", "score.xml")



# freqs = bin_to_freq(peaks, sr, winsize) #peaks, sr, winsize
# pitches = freq_to_pitch(freqs)


# strm = stream.Stream()
# for pitch in pitches:
# 	strm.append(note.Note(pitch_to_spn(int(round(pitch)))))

# strm.show()

#for now discard ending part, can add 1 to num_win instead
# print len(x)