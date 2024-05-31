#define the function 
def print_diamond(rows, is_upright=True):
	if is_upright:
		for i in range(rows):
			for j in range(rows - i - 1):
				print(' ', end='')
			for j in range(2 * i + 1):
				print(chr(65 + j), end='')
			print()
	else:
		for i in range(rows - 1):
			for j in range(i + 1):
				print(' ', end='')
			for j in range(2 * (rows - i - 1) - 1):
				print(chr(65 + j), end='')
			print()

#rows to be spanned 
n = 7

#call the function to print upright triangle 
print_diamond(n, is_upright=True)

#call the function to print reverse triangle 
print_diamond(n, is_upright=False)
