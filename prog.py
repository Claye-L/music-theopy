import chord as chord
import note as note

bmin = chord.minorChord(note.parse('B'))
fsmaj = chord.majorChord(note.parse('F',1))
bbmin = chord.minorChord(note.parse('B',-1))
fmaj = chord.majorChord(note.parse('F'))
amin = chord.minorChord(note.parse('A'))
emaj = chord.majorChord(note.parse('E'))
chords = [bmin,fsmaj,bbmin,fmaj,amin,emaj]


