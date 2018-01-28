class CountInversion:
	def __init__(self):
		self.INVERSION_COUNT = 0

	def sort_count_inversion(self, input_array):
		if len(input_array) > 1:
			mid = len(input_array) // 2
			left_array = input_array[:mid]
			right_array = input_array[mid:]
			# sort
			self.sort_count_inversion(left_array)
			self.sort_count_inversion(right_array)
			# merge
			self.merge_arrays(input_array, left_array, right_array)

	def merge_arrays(self, input_array, left_array, right_array):
		i = 0
		j = 0
		k = 0
		while (i < len(left_array) and j < len(right_array)):
			if (left_array[i] <= right_array[j]):
				input_array[k] = left_array[i]
				i += 1
				k += 1
			else:
				input_array[k] = right_array[j]
				self.INVERSION_COUNT += len(left_array) - i
				j += 1
				k += 1
		while (i < len(left_array)):
			input_array[k] = left_array[i]
			i += 1
			k += 1
		while (j < len(right_array)):
			input_array[k] = right_array[j]
			j += 1
			k += 1

if __name__ == "__main__":
	### Tests
	# test1 = [1,2,3,4,5]
	# t1 = CountInversion()
	# t1.sort_count_inversion(test1)
	# print("1. answer should be 0, test result is %d" % t1.INVERSION_COUNT)
	# print(test1)
	test2 = [6,5,4,3,2,1]
	t2 = CountInversion()
	t2.sort_count_inversion(test2)
	print("2. answer should be 15, test result is %d" % t2.INVERSION_COUNT)
	print(test2)
	test3 = [1,2,4,3,5,8,9,10,7,6]
	t3 = CountInversion()
	t3.sort_count_inversion(test3)
	print("3. answer should be 8, test result is %d" % t3.INVERSION_COUNT)
	print(test3)


	### Homework
	NUMLIST_FILENAME = "IntegerArray.txt"
	inFile = open(NUMLIST_FILENAME, 'r')
	with inFile as f:
		numList = [int(integers.strip()) for integers in f.readlines()]
	act = CountInversion()
	act.sort_count_inversion(numList)
	print("==> homework solution is 2407905288, test result is: %d" % act.INVERSION_COUNT)




	