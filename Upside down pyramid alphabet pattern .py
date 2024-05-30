#define the function 
def reverse_pyramid(rows):
	for i in range(rows):
		# prints spaces
		for j in range(i):
			print(' ', end='')

		# prints an odd number of characters in each row
		for j in range(2 * (rows - i) - 1):
			print(chr(65 + j), end='')

		print()

#rows to be spanned 
n = 7

#call the function
reverse_pyramid(n)
