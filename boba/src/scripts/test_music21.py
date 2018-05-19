from music21 import *
# us = environment.UserSettings()
# us.create()

# for key in sorted(us.keys()):
    # print(key)
 #warnings was set to 0 to prevent message, v4 is last version of python2.7
# environment.set('warnings', 0)
# print environment.get('warnings')
# environment.set('lilypondPath', '/Applications/Lilypond.app/Contents/Resources/bin/lilypond')
# print environment.get('lilypondPath')
# print environment.UserSettings()['lilypondPath']
notes = converter.parse("tinynotation: 4/4 a#4 g#4 f#4 g#4 g#4 a#4 a#4 a#4 a#4 b#4 g#4 g#4 a#4 a#4 a#4 a#4")
# notes.write('musicxml.pdf', fp = 'wheretosavethefile.pdf')
# fp = notes.show("musicxml.png")
fp = notes.write("musicxml", "image.xml")
# converter.parse("tinynotation: a#4 g#4 f#4 g#4 g#4 a#4 a#4 a#4 a#4 g#4 g#4 g#4").show()