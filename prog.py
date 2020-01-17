import note as note
import chord as chord


"""returns the notes in common between 2 chords/scales"""
def notesInCommon(c1,c2):
	result = [] 
	for n1 in c1:
		for n2 in c2:
			if n1 == n2:
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
allscales = [chord.majorScale(x) for x in allNotes()]
intersects = [(scale, notesInCommon(scale,uniquenotes)) for scale in allscales]
srtInte = sorted(intersects, key= lambda x: len(x[1]), reverse= True)[:5]


# print(list(map(lambda c: chord.prettyPrintChord(c),chords)))
print([chord.prettyPrintChord(s)  for (s,c) in srtInte])