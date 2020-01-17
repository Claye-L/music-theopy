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
'''return the note shifted by the interval'''
def addInterval(note,interval):
	return getNoteAtInterval(note,interval)
'''apply a list of intervals to a note'''
def applyListIntervals(note,intervals):
	return map(lambda interval: addInterval(note,interval) ,intervals)

'''return a list of notes that comprise the major chord based on note'''
def majorChord(note):
	return applyListIntervals(note, [Interval.Unison, Interval.MajorThird, Interval.Fifth])
def minorChord(note):
	return applyListIntervals(note, [Interval.Unison, Interval.MinorThird, Interval.Fifth])
def majorScale(note):
	return applyListIntervals(note, [Interval.Unison, Interval.Second, Interval.MajorThird, Interval.Fourth, Interval.Fifth, Interval.MajorSixth, Interval.MajorSeventh])
def minorScale(note):
	return applyListIntervals(note, [Interval.Unison, Interval.Second, Interval.MinorThird, Interval.Fourth, Interval.Fifth, Interval.MinorSixth, Interval.MinorSeventh])

