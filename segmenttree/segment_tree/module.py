class SegmentTree(object):
	def __init__(self, size):
		self.size = size
		self.heap = [0] * (size*2)
		self.leftIndices = {}
		self.rightIndices = {}

		self.setIndices()



	def setValue(self, value, index):
		# TODO: return error if index out of range
		heapIndex = len(self.heap) - self.size + index
		# Set the new value
		self.heap[heapIndex] = value
		# Recalculate values upward
		self.recalculateSum((heapIndex - 1) // 2)

	def getSum(self, indexLeft, indexRight):
		# TODO: return error if indexLeft or indexRight are out of range
		
		if(indexLeft < 0 or indexRight > self.size):
			return 0

		return self.getSumR(0, indexLeft, indexRight)

	'''
	Recursive method.
	Checks if the current heap index matches the
	left and right parameters for the range we are 
	looking for. Returns a running sum.
	'''
	def getSumR(self, currentHeapIndex, indexLeft, indexRight):
		if(currentHeapIndex >= len(self.heap)):
			# print('Index ' + str(currentHeapIndex) + ' out of range')
			return 0

		if(self.leftIndices[currentHeapIndex] > indexRight or self.rightIndices[currentHeapIndex] < indexLeft):
			# print('Indices ' + str(self.leftIndices[currentHeapIndex]) + ' and ' + str(self.rightIndices[currentHeapIndex]) + ' invalid')
			return 0
		
		if(self.leftIndices[currentHeapIndex] < indexLeft or self.rightIndices[currentHeapIndex] > indexRight):
			# Recurse on both children
			# print('heap: ', self.heap)
			# print('Recursing on heap index: ', currentHeapIndex)
			# print('left: ', currentHeapIndex * 2 + 1)
			# print('right: ', currentHeapIndex * 2 + 2)
			return self.getSumR(currentHeapIndex * 2 + 1, indexLeft, indexRight) + self.getSumR(currentHeapIndex * 2 + 2, indexLeft, indexRight)

			return 0

		if(self.leftIndices[currentHeapIndex] >= indexLeft and self.rightIndices[currentHeapIndex] <= indexRight):
			return self.heap[currentHeapIndex]

		# Should never reach this point
		print('Fatal error. Self destructing.')
		return 0
		
	'''
	Returns a pair of values representing the children
	of the node with the given heap index.
	'''
	def getChildren(self, heapIndex):
		return self.heap[heapIndex * 2 + 1], self.heap[heapIndex * 2 + 2]

	def setIndices(self):
		level = 0
		width = 2 ** level
		i = 0
		for x in range(len(self.heap) - 1):

			self.leftIndices[x] = (self.size // width) * i
			self.rightIndices[x] = (self.size // width) * (i+1) - 1
			if i >= width - 1:
				i = 0
				level += 1
				width = 2 ** level
			else:
				i += 1

	'''
	Recalculates the sum at the given index and recurses up 
	the tree until it has recalculated the entire tree.
	'''
	def recalculateSum(self, heapIndex):
		# index < 0 means that we have completed the recalculation
		if(heapIndex < 0):
			return True
		# The new value at the current node is the sum of its children
		self.heap[heapIndex] = self.heap[heapIndex * 2 + 1] + self.heap[heapIndex * 2 + 2]
		# Recurse until the recalculation is complete.
		return self.recalculateSum((heapIndex - 1) // 2)
		


class SegmentTreeMax(object):
	def __init__(self, size):
		self.size = size

	def setValue(self, value, index):
		i = 0

	def getMax(self, indexLeft, indexRight):
		i = 5

class SegmentTreeScheduler(object):
	def __init__(self, size):
		self.size = size

	def setMeeting(self, startTime, endTime):
		i = 9

	def numberOfMeetingsTakingPlace(self, time):
		i = 0

	def roomsOccupied(self, startTime, endTime):
		i = 8