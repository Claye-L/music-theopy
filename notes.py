from enum import Enum

class Accidental(Enum) :
	Flat = -1
	Natural = 0
	Sharp = 1
	def toSymbol(self):
		if self.value = -1:
			return 'b'
		elif self.value = 0:
			return ''
		elif self.value = 1:
			return '#'

class NoteName(Enum) :
	A = 0
	B = 2
	C = 3
	D = 5
	E = 7
	F = 8
	G = 10

class Note :
	def __init__(self,note,accidental):
		self.noteName = note
		self.accidental = accidental
	def __str__(self):
		return '{0} {1}'.format(noteName,accidental.toSymbol())

aflat = Note(NoteName.A, Accidental.Flat)
fsharp = Note(NoteName.F, Accidental.Sharp)
enatural = Note(NoteName.E, Accidental.Natural)

print(aflat)
print(fsharp)
print(enatural)