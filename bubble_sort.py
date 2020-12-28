# bubble_sort.py

# Allow swapping
def swap(num_list, pos_1, pos_2):
	save = num_list[pos_1]
	num_list[pos_1] = num_list[pos_2]
	num_list[pos_2] = save


# Goes in ascending order
def sort(num_list):

	# For some reason i have to use the same for loop more than once so i put it in a while loop and it works (:
	amount = len(num_list)
	while amount != 0:
		for x in range(len(num_list)):
			if x == len(num_list) - 1:
				break

			if num_list[x] > num_list[x + 1]:
				swap(num_list, x, x + 1)
		amount -= 1


# You can put any list but this is just an example one
a = [1, 464, 34, 3727, 44, 344632, 452, 42]
sort(a)
print(a)