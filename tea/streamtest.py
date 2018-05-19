from music21 import *
s = stream.Stream()

s.append(chord.Chord(["D", "F#", "A"]))
# s.append(note.Note('B-5'))
# s.append(note.Note('B#'))

# s.append(note.Note('B-'))
# for i in range(100):
	# s.append(note.Note('B-'))

s.show()

# n.show()
# b.show()