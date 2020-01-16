from enum import Enum

'''represents an interval either by major scale name or pitch value'''
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

	'''returns how to shift note name for interval'''
	def noteOffsetForInterval(self):
		value = self.value
		if value == 0:
			return 0
		elif value in [1,2]:
			return 1
		elif value in [3,4]:
			return 2
		elif value in [5,6]:
			return 3
		elif value == 7:
			return 4
		elif value in [8,9]:
			return 5
		else:
			return 6
	# '''returns how to shift the name of a note for an interval according to major scale rules'''
	# def intervalShift(self):
		# interval = self
		# if interval.value in [0,2,4,5,7,9,11]:
			# return (self.noteOffsetForInterval(),0)
		# elif interval.value in [1,3,6,8,10]:
			# return (self.noteOffsetForInterval(),-1)