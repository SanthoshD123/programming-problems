#define the function 
def right_triangle_pattern(rows):
	#changes lines 
	for i in range(rows):
		#adds spaces
		for j in range(1, rows - i):
			print(" ", end="")
		# prints characters
		for k in range(i + 1):
			print(chr(65 + k), end="")
		print()

#rows to be spanned 
n = 7

#call the function
right_triangle_pattern(n)
