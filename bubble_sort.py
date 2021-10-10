import shutil
columns = shutil.get_terminal_size().columns

def BubbleSort():
	i = 0
	swap = True
	while i < n and swap == True:
		swap = False
		for j in range(n-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
				swap = True
		if swap == False:
			break
		i += 1

	return array


if __name__=="__main__":
	print("BUBBLE SORT".center(columns))
	
	while True:
		array = input("\nPlease type in numbers separated by commas: ").split(",")
		array = [int(x) for x in array]
		n = len(array)

		print(BubbleSort())

		ask = input("\nWanna Continue? [y/n]: ").lower()
		if ask == "y":
			continue
		elif ask == "n":
			exit()

	