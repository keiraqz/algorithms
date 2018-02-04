class CountComparison:
	def __init__(self, pivot_index="BEG"):
		self.ComparisonCount = 0
		self.pivot_index = pivot_index 

	def _find_median(self, input_array, beg_index, end_index):
		middle_index = (end_index - beg_index) // 2
		beg_element = input_array[beg_index]
		middle_element = input_array[middle_index]
		last_element = input_array[end_index]
		if (beg_element < middle_element < last_element or
			beg_element > middle_element > last_element ):
			self._swap(input_array, beg_index, middle_element)
		elif (middle_element < last_element < beg_element or
			middle_element > last_element > beg_element):
			self._swap(input_array, beg_index, end_index)


	def _swap(self, input_array, swap1, swap2):
		tmp = input_array[swap1]
		input_array[swap1] = input_array[swap2]
		input_array[swap2] = tmp

	def quick_sort(self, input_array, beg_index, end_index):
		if beg_index >= end_index:
			return
		if (self.pivot_index is "END"):
			self._swap(input_array, beg_index, end_index)
		if (self.pivot_index is "MEDIAN"):
			self._find_median(input_array, beg_index, end_index)
		self.ComparisonCount += end_index - beg_index
		div_index = beg_index + 1
		pivot = input_array[beg_index]
		for i in range(beg_index + 1, end_index+1):
			if (input_array[i] < pivot): 
				# swap the element with the left most element from the right array
				self._swap(input_array, div_index, i)
				# increment the divide index
				div_index += 1
		self._swap(input_array, beg_index, div_index-1)
		# get subarrays and recurse 
		# DON'T include the pivot item
		# left_array = input_array[:div_index]
		# right_array = input_array[div_index:]
		self.quick_sort(input_array, beg_index, div_index-2)
		self.quick_sort(input_array, div_index, end_index)


if __name__ == "__main__":
	### Test 1
	input_array = [2,4,6,1,7,8]
	sorting = CountComparison()
	sorting.quick_sort(input_array, 0, len(input_array)-1)
	print(input_array)
	print(sorting.ComparisonCount)

	### Homework
	NUMLIST_FILENAME = "QuickSort.txt"
	inFile = open(NUMLIST_FILENAME, 'r')
	with inFile as f:
		numList = [int(integers.strip()) for integers in f.readlines()]
	# Q1
	sorting = CountComparison()
	test1 = numList[:]
	sorting.quick_sort(test1, 0, len(test1)-1)
	print("==> homework solution is 162085, test result is: %d" % sorting.ComparisonCount)
	# Q2
	sorting = CountComparison(pivot_index="END")
	test2 = numList[:]
	sorting.quick_sort(test2, 0, len(test2)-1)
	print("==> homework solution is 164123, test result is: %d" % sorting.ComparisonCount)
	# Q3
	sorting = CountComparison(pivot_index="MEDIAN")
	test3 = numList[:]
	sorting.quick_sort(test3, 0, len(test3)-1)
	print("==> homework solution is 138382, test result is: %d" % sorting.ComparisonCount)
