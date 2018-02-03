class CountComparison:
	def __init__(self, pivot_index=0):
		self.ComparisonCount = 0
		self.pivot_index = pivot_index 

	def quick_sort(self, input_array):
		print(input_array)
		if (len(input_array) == 2):
			if (input_array[1] > input_array[0]):
				tmp = input_array[0]
				input_array[0] = input_array[1]
				input_array[1] = tmp
		else:
			div_index = 1
			pivot = input_array[self.pivot_index]
			for i in range(1, len(input_array)):
				if (input_array[i] < pivot): 
					# swap the element with the left most element from the right array
					tmp = input_array[div_index]
					input_array[div_index] = input_array[i]
					input_array[i] = tmp
					# increment the divide index
					div_index += 1
			# else:
				# do nothing

			# swap pivot with the right most element of the left array
			tmp = input_array[div_index-1]
			input_array[div_index-1] = input_array[self.pivot_index]
			input_array[self.pivot_index] = tmp
			# get subarrays
			left_array = input_array[:div_index]
			right_array = input_array[div_index:]

			# recurse 
			if (len(left_array) > 1):
				self.ComparisonCount += len(left_array) - 1
				self.quick_sort(left_array)
			if (len(right_array) > 1):
				self.ComparisonCount += len(right_array) - 1
				self.quick_sort(right_array)


if __name__ == "__main__":
	### Test 1
	# input_array = [2,4,6,1,7,8]
	# sorting = CountComparison()
	# sorting.quick_sort(input_array)
	# print(input_array)
	# print(sorting.ComparisonCount)

	## Homework
	NUMLIST_FILENAME = "QuickSort.txt"
	inFile = open(NUMLIST_FILENAME, 'r')
	with inFile as f:
		numList = [int(integers.strip()) for integers in f.readlines()]
	sorting = CountComparison()
	sorting.quick_sort(numList)
	print("==> homework solution is 162085, test result is: %d" % sorting.ComparisonCount)

