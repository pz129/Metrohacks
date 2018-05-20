from music21 import *
s = stream.Stream()


notes_in_chord = []
notes_in_chord.append(note.Note("C4", quarterLength = 0.25))
# notes_in_chord.append(note.Note("D4", quarterLength = 1))
s.append(chord.Chord(notes_in_chord))
# s.append(note.Note('B-5'))
# s.append(note.Note('B#'))

# s.append(note.Note('B-'))
# for i in range(100):
	# s.append(note.Note('B-'))

s.show()

# n.show()
# b.show()