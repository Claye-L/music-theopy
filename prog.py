import note as note
import chord as chord


"""returns the notes in common between 2 chords/scales"""
def notesInCommon(c1,c2):
	result = [] 
	for n1 in c1:
		for n2 in c2:
			if n1 == n2:
				print(n1)
				result.append(n1)
	return result

def allNotes():
	result = []
	for n in list(note.NoteName):
		for i in range(0,2):
			result.append(note.Note(n,note.Accidental(i)))
	return result

chordSymbols = ['B min','F# maj','Bb min', 'F maj', 'A min', 'E maj']
chords = list(map(lambda c: chord.parseChord(c),chordSymbols))
uniquenotes = set([item for sublist in chords for item in sublist])
allscales = map(lambda x: chord.majorScale(x), allNotes())
intersects = list(sorted(map(lambda scale: (scale,notesInCommon(scale,uniquenotes)),allscales), key = lambda a : len(a[1])))


print(list(map(lambda c: chord.prettyPrintChord(c),chords)))
print(intersects)