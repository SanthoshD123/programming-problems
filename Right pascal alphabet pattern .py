#define the function 
def right_pascal_triangle(rows):
	#prints ascending part
	for i in range(1, rows + 1):
		#prints spaces
		print(" " * (rows - i), end="")

		#prints alphabets
		for j in range(1, i + 1):
			print(chr(64 + j), end="")
		print()

	#prints descending part
	for i in range(rows - 1, 0, -1):
		#prints spaces
		print(" " * (rows - i), end="")

		#prints alphabets
		for j in range(1, i + 1):
			print(chr(64 + j), end="")
		print()

#rows to be spanned 
n = 7

#call the function
right_pascal_triangle(n)
