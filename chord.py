from interval import *
from note import *

def circularWrap(num):
	if num >= 6:
		return num - 12
	else:
		return num
	
'''return the note shifted by the interval'''
def getNoteAtInterval(note, interval):
	notename = NoteName((note.noteName.value + interval.noteOffsetForInterval()) % 7)
	#print(notename)
	newnotepitch = (mapNameToPitch(note.noteName) + note.accidental.value + interval.value) % 12 
	#print(newnotepitch)
	basenotepitch = mapNameToPitch(notename)
	# print(basenotepitch)
	return Note(notename, Accidental(circularWrap(newnotepitch - basenotepitch)))
	
'''return a list of notes that comprise the major chord based on note'''
def majorChord(note):
	return [note,getNoteAtInterval(note, Interval.MajorThird), getNoteAtInterval(note, Interval.Fifth)]
	
aflat = Note(NoteName.A, Accidental.Flat)
fsharp = Note(NoteName.F, Accidental.Sharp)
enatural = Note(NoteName.E, Accidental.Natural)
gnatural = Note(NoteName.G,Accidental.Natural)

# print(majorChord(aflat))
print(getNoteAtInterval(enatural,Interval.Fifth))
print(getNoteAtInterval(enatural,Interval.MajorThird))
#print(majorChord(enatural))

print(aflat)
print(getNoteAtInterval(aflat,Interval.Fifth))
print(getNoteAtInterval(aflat,Interval.MajorThird))
print(getNoteAtInterval(aflat,Interval.MinorSixth))
print(getNoteAtInterval(aflat,Interval.MajorSixth))
print(getNoteAtInterval(aflat,Interval.MinorThird))