class SegmentTree(object):
	def __init__(self, size):
		self.LEFT = True
		self.RIGHT = False

		import math
		self.size = size
		self.heap = [0] * (size*2-1)
		
		self.levels = math.ceil(math.log(len(self.heap),2))
		self.leftIndices = {}
		self.rightIndices = {}

		self.setIndices()

	'''
	Sets the leaf node with the given index to the given value.
	'''
	def setValue(self, value, index):
		# Eeturn if index out of range
		if index > self.size:
			return

		heapIndex = self.getHeapIndexOfLeaf(0, index)
		# print('heap index: ' + str(heapIndex))

		# Set the new value
		self.heap[heapIndex] = value

		# Recalculate values upward
		self.recalculateSum((heapIndex - 1) // 2)

	'''
	Recursive function.
	Returns the heap index of the leaf node with the given index.
	'''
	def getHeapIndexOfLeaf(self, currentHeapIndex, index):
		if(currentHeapIndex >= len(self.heap)):
			# print('Index ' + str(currentHeapIndex) + ' out of range')
			return 0

		if(self.leftIndices[currentHeapIndex] > index or self.rightIndices[currentHeapIndex] < index):
			# print('Indices ' + str(self.leftIndices[currentHeapIndex]) + ' and ' + str(self.rightIndices[currentHeapIndex]) + ' invalid')
			return 0

		if(self.leftIndices[currentHeapIndex] == index and self.rightIndices[currentHeapIndex] == index):
			return currentHeapIndex

		return self.getHeapIndexOfLeaf(currentHeapIndex * 2 + 1, index) + self.getHeapIndexOfLeaf(currentHeapIndex * 2 + 2, index)

	'''
	Returns the sum of leaf nodes from indexLeft to indexRight.
	'''
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
		# If the index is out of range there is no sum to return.
		if(currentHeapIndex >= len(self.heap)):
			return 0

		# If the current node indices have no overlap, there is no sum to return.
		if(self.leftIndices[currentHeapIndex] > indexRight or self.rightIndices[currentHeapIndex] < indexLeft):
			# print('Indices ' + str(self.leftIndices[currentHeapIndex]) + ' and ' + str(self.rightIndices[currentHeapIndex]) + ' invalid')
			return 0
		
		# If there is overlap, we need to get the proper sum from the children.
		if(self.leftIndices[currentHeapIndex] < indexLeft or self.rightIndices[currentHeapIndex] > indexRight):
			# Recurse on both children and add them.
			return self.getSumR(currentHeapIndex * 2 + 1, indexLeft, indexRight) + self.getSumR(currentHeapIndex * 2 + 2, indexLeft, indexRight)

		# If the current node's indices are included entirely in the given range, return the 
		# value at the current node.
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

	'''
	Assigns the proper indices to all nodes (in leftIndices and rightIndices).
	'''
	def setIndices(self):
		self.leftIndices[0] = 0
		self.rightIndices[0] = self.size - 1

		# Recurse on children
		self.setChildIndicesR(1, self.leftIndices[0], self.rightIndices[0], self.LEFT)
		self.setChildIndicesR(2, self.leftIndices[0], self.rightIndices[0], self.RIGHT)

	'''
	Assigns the proper indices to a node (in leftIndices and rightIndices)
	and its children.
	'''
	def setChildIndicesR(self, heapIndex, leftIndex, rightIndex, isLeft):
		width = rightIndex - leftIndex
		if isLeft:
			self.leftIndices[heapIndex] = leftIndex
			self.rightIndices[heapIndex] = leftIndex + width // 2
		else: # Right child of parent
			self.leftIndices[heapIndex] = (leftIndex + width // 2) + 1
			self.rightIndices[heapIndex] = rightIndex

		# If not at a leaf node recurse on children
		if self.leftIndices[heapIndex] != self.rightIndices[heapIndex]:
			self.setChildIndicesR(heapIndex * 2 + 1, self.leftIndices[heapIndex], self.rightIndices[heapIndex], self.LEFT)
			self.setChildIndicesR(heapIndex * 2 + 2, self.leftIndices[heapIndex], self.rightIndices[heapIndex], self.RIGHT)

	'''
	Recalculates the sum at the given index and recurses up 
	the tree until it has recalculated the entire tree.
	'''
	def recalculateSum(self, heapIndex):
		# print('Recalculating sum at heap index ' + str(heapIndex))
		# index < 0 means that we have completed the recalculation
		if(heapIndex < 0):
			return True
		if heapIndex * 2 + 1 >= len(self.heap) or heapIndex * 2 + 2 >= len(self.heap):
			# print('No children to change')
			return self.recalculateSum((heapIndex - 1) // 2)
		# The new value at the current node is the sum of its children
		self.heap[heapIndex] = self.heap[heapIndex * 2 + 1] + self.heap[heapIndex * 2 + 2]
		# Recurse until the recalculation is complete.
		return self.recalculateSum((heapIndex - 1) // 2)
		


class SegmentTreeMax(object):
	def __init__(self, size):
		self.LEFT = True
		self.RIGHT = False

		import math
		self.size = size
		self.heap = [0] * (size*2-1)
		
		self.levels = math.ceil(math.log(len(self.heap),2))
		self.leftIndices = {}
		self.rightIndices = {}

		self.setIndices()

	def setValue(self, value, index):
		# Eeturn if index out of range
		if index > self.size:
			return

		heapIndex = self.getHeapIndexOfLeaf(0, index)
		# print('heap index: ' + str(heapIndex))

		# Set the new value
		self.heap[heapIndex] = value

		# Recalculate values upward
		self.recalculateMax((heapIndex - 1) // 2)

	def getMax(self, indexLeft, indexRight):
		
		if(indexLeft < 0 or indexRight > self.size):
			return 0

		return self.getMaxR(0, indexLeft, indexRight)

	'''
	Recursive method.
	Checks if the current heap index matches the
	left and right parameters for the range we are 
	looking for. Returns a running max.
	'''
	def getMaxR(self, currentHeapIndex, indexLeft, indexRight):
		# If the index is out of range there is no sum to return.
		if(currentHeapIndex >= len(self.heap)):
			return 0

		# If the current node indices have no overlap, there is no sum to return.
		if(self.leftIndices[currentHeapIndex] > indexRight or self.rightIndices[currentHeapIndex] < indexLeft):
			# print('Indices ' + str(self.leftIndices[currentHeapIndex]) + ' and ' + str(self.rightIndices[currentHeapIndex]) + ' invalid')
			return 0
		
		# If there is overlap, we need to get the proper sum from the children.
		if(self.leftIndices[currentHeapIndex] < indexLeft or self.rightIndices[currentHeapIndex] > indexRight):
			# Recurse on both children and add them.
			return max(self.getMaxR(currentHeapIndex * 2 + 1, indexLeft, indexRight), self.getMaxR(currentHeapIndex * 2 + 2, indexLeft, indexRight))

		# If the current node's indices are included entirely in the given range, return the 
		# value at the current node.
		if(self.leftIndices[currentHeapIndex] >= indexLeft and self.rightIndices[currentHeapIndex] <= indexRight):
			return self.heap[currentHeapIndex]

		# Should never reach this point
		print('Fatal error. Self destructing.')
		return 0
		
	'''
	Recursive function.
	Returns the heap index of the leaf node with the given index.
	'''
	def getHeapIndexOfLeaf(self, currentHeapIndex, index):
		if(currentHeapIndex >= len(self.heap)):
			# print('Index ' + str(currentHeapIndex) + ' out of range')
			return 0

		if(self.leftIndices[currentHeapIndex] > index or self.rightIndices[currentHeapIndex] < index):
			# print('Indices ' + str(self.leftIndices[currentHeapIndex]) + ' and ' + str(self.rightIndices[currentHeapIndex]) + ' invalid')
			return 0

		if(self.leftIndices[currentHeapIndex] == index and self.rightIndices[currentHeapIndex] == index):
			return currentHeapIndex

		return self.getHeapIndexOfLeaf(currentHeapIndex * 2 + 1, index) + self.getHeapIndexOfLeaf(currentHeapIndex * 2 + 2, index)

	'''
	Assigns the proper indices to all nodes (in leftIndices and rightIndices).
	'''
	def setIndices(self):
		self.leftIndices[0] = 0
		self.rightIndices[0] = self.size - 1

		# Recurse on children
		self.setChildIndicesR(1, self.leftIndices[0], self.rightIndices[0], self.LEFT)
		self.setChildIndicesR(2, self.leftIndices[0], self.rightIndices[0], self.RIGHT)

	'''
	Assigns the proper indices to a node (in leftIndices and rightIndices)
	and its children.
	'''
	def setChildIndicesR(self, heapIndex, leftIndex, rightIndex, isLeft):
		width = rightIndex - leftIndex
		if isLeft:
			self.leftIndices[heapIndex] = leftIndex
			self.rightIndices[heapIndex] = leftIndex + width // 2
		else: # Right child of parent
			self.leftIndices[heapIndex] = (leftIndex + width // 2) + 1
			self.rightIndices[heapIndex] = rightIndex

		# If not at a leaf node recurse on children
		if self.leftIndices[heapIndex] != self.rightIndices[heapIndex]:
			self.setChildIndicesR(heapIndex * 2 + 1, self.leftIndices[heapIndex], self.rightIndices[heapIndex], self.LEFT)
			self.setChildIndicesR(heapIndex * 2 + 2, self.leftIndices[heapIndex], self.rightIndices[heapIndex], self.RIGHT)
	
	'''
	Recalculates the max at the given index and recurses up 
	the tree until it has recalculated the entire tree.
	'''
	def recalculateMax(self, heapIndex):
		# print('Recalculating max at heap index ' + str(heapIndex))
		# index < 0 means that we have completed the recalculation
		if(heapIndex < 0):
			return True
		if heapIndex * 2 + 1 >= len(self.heap) or heapIndex * 2 + 2 >= len(self.heap):
			# print('No children to change')
			return self.recalculateMax((heapIndex - 1) // 2)
		# The new value at the current node is the max of its children
		self.heap[heapIndex] = max(self.heap[heapIndex * 2 + 1], self.heap[heapIndex * 2 + 2])
		# Recurse until the recalculation is complete.
		return self.recalculateMax((heapIndex - 1) // 2)

class SegmentTreeScheduler(object):
	def __init__(self, size):
		self.size = size

	def setMeeting(self, startTime, endTime):
		i = 9

	def numberOfMeetingsTakingPlace(self, time):
		i = 0

	def roomsOccupied(self, startTime, endTime):
		i = 8