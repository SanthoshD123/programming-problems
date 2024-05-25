#define the function
def pyramid_pattern(rows):
	for i in range(rows):
		# prints spaces
		for j in range(rows - i - 1):
			print(' ', end='')

		# prints odd number of characters
		for k in range(2 * i + 1):
			print(chr(65 + k), end='')

		print()

#rows to be spanned 
n = 7

#call the function 
pyramid_pattern(n)
