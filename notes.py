from enum import Enum

class Accidental(Enum) :
	Flat = -1
	Natural = 0
	Sharp = 1
	def toSymbol(self):
		if self.value == -1:
			return 'b'
		elif self.value == 0:
			return ''
		elif self.value == 1:
			return '#'

class NoteName(Enum) :
	C = 0
	D = 2
	E = 4
	F = 5
	G = 7
	A = 9
	B = 11
class Interval(Enum):
	Unison = 0
	MinorSecond = 1
	Second = 2
	MinorThird = 3
	MajorThird = 4
	Fourth = 5
	Tritone = 6
	SharpFour = 6
	FlatFive = 6
	Fifth = 7
	MinorSixth = 8
	MajorSixth = 9
	MinorSeventh = 10
	MajorSeventh = 11
	

class Note :
	def __init__(self,note,accidental):
		self.noteName = note
		self.accidental = accidental
	def __str__(self):
		return '{0}{1}'.format(self.noteName.name,self.accidental.toSymbol())
'''return a musical note (sharp biased) from an absolute pitch value'''
def makeNoteNoFail(num):
	if num in map(lambda x: x.value,list(NoteName)):
		return Note(NoteName(num),Accidental.Natural)
	else:
		return Note(NoteName(num - 1),Accidental.Sharp)


'''return the note shifted by the interval'''
def getNoteAtInterval(note, interval):
	notevalue = note.NoteName.value + interval 
	
	
'''return a list of notes that comprise the major chord based on note'''
def majorChord(note):
	thirdvalue = note.NoteName.value + 4 + note.Accidental.value % 12
	fifthvalue = note.NoteName.value + 7 + note.Accidental.value % 12
	
	

aflat = Note(NoteName.A, Accidental.Flat)
fsharp = Note(NoteName.F, Accidental.Sharp)
enatural = Note(NoteName.E, Accidental.Natural)
g = NoteName(7)
dsharp = makeNoteNoFail(3)
fnatural = makeNoteNoFail(5)

print(dsharp)
print(fnatural)