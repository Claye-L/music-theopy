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
		return self.accidental.value == other.accidental.value and self.noteName.value == other.noteName.value
	def __key(self):
		return (self.noteName, self.accidental)
	def __hash__(self):
		return hash(self.__key())
		

'''return a musical note (sharp biased) from an absolute pitch value'''
def makeNoteNoFail(num):
	if num in map(lambda x: x.value,list(NoteName)):
		return Note(NoteName(num),Accidental.Natural)
	else:
		return Note(NoteName(num - 1),Accidental.Sharp)
"""takes a note and a number for accidental"""
def parse(name, acc = 0):
	return Note(NoteName[name],Accidental(acc))
"""reads a common notation note symbol"""
def parseNote(symbol):
	name = symbol[0]
	acc = 0
	if len(symbol) > 1:
		a = symbol[1:]
		acc += a.count('b') * -1
		acc += a.count('#') * 1
	return parse(name,acc)
