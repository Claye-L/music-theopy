from enum import Enum

'''represents a flat/natural/sharp'''
class Accidental(Enum) :
	TripleFlat = -3
	DoubleFlat = -2
	Flat = -1
	Natural = 0
	Sharp = 1
	DoubleSharp = 2
	TripleSharp = 3
	def toSymbol(self):
		if self.value == -2:
			return 'bb'
		elif self.value == -1:
			return 'b'
		elif self.value == 0:
			return ''
		elif self.value == 1:
			return '#'
		elif self.value == 2:
			return '##'


class NotePitch(Enum) :
	C = 0
	D = 2
	E = 4
	F = 5
	G = 7
	A = 9
	B = 11
# class NotePitch(Enum) :
	# C = 1
	# D = 3
	# E = 5
	# F = 6
	# G = 8
	# A = 10
	# B = 12
'''represents a note name from C to B'''
class NoteName(Enum) :
	C = 0
	D = 1
	E = 2
	F = 3
	G = 4
	A = 5
	B = 6
def mapNameToPitch(notename):
	return NotePitch[notename.name].value
'''represents a note with a pitch value and an opinionated name'''
class Note :
	def __init__(self,note,accidental):
		self.noteName = note
		self.accidental = accidental
	def __str__(self):
		return '{0}{1}'.format(self.noteName.name,self.accidental.toSymbol())
	def __repr__(self):
		return 'Note object {0} {1}'.format(self.noteName,self.accidental)
	def __eq__(self,other):
		self.accidental == other.accidental and self.noteName == other.noteName
		
'''return a musical note (sharp biased) from an absolute pitch value'''
def makeNoteNoFail(num):
	if num in map(lambda x: x.value,list(NoteName)):
		return Note(NoteName(num),Accidental.Natural)
	else:
		return Note(NoteName(num - 1),Accidental.Sharp)

def parse(name, acc = 0):
	return Note(NoteName[name],Accidental(acc))
