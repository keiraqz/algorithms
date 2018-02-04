class CountComparison:
	def __init__(self, pivot_index=0):
		self.ComparisonCount = 0
		self.pivot_index = pivot_index 

	def _swap(self, input_array, swap1, swap2):
		tmp = input_array[swap1]
		input_array[swap1] = input_array[swap2]
		input_array[swap2] = tmp

	def quick_sort(self, input_array, beg_index, end_index):
		self.ComparisonCount += end_index - beg_index 
		div_index = beg_index + 1
		pivot = input_array[beg_index]
		for i in range(beg_index, end_index+1):
			if (input_array[i] < pivot): 
				# swap the element with the left most element from the right array
				self._swap(input_array, div_index, i)
				# increment the divide index
				div_index += 1
		# else:
			# do nothing
		# swap pivot with the right most element of the left array
		self._swap(input_array, beg_index, div_index-1)
		# get subarrays and recurse 
		# left_array = input_array[:div_index]
		# right_array = input_array[div_index:]
		if (div_index - beg_index > 1):
			self.quick_sort(input_array, beg_index, div_index-1)
		if (end_index - div_index > 0):
			self.quick_sort(input_array, div_index, end_index)


if __name__ == "__main__":
	### Test 1
	input_array = [2,4,6,1,7,8]
	sorting = CountComparison()
	sorting.quick_sort(input_array, 0, len(input_array)-1)
	print(input_array)
	print(sorting.ComparisonCount)

	## Homework
	NUMLIST_FILENAME = "QuickSort.txt"
	inFile = open(NUMLIST_FILENAME, 'r')
	with inFile as f:
		numList = [int(integers.strip()) for integers in f.readlines()]
	sorting = CountComparison()
	sorting.quick_sort(numList, 0, len(numList)-1)
	print("==> homework solution is 162085, test result is: %d" % sorting.ComparisonCount)
