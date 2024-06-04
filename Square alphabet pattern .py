#define the function
def print_square_pattern(rows):
	#print rows 
	for i in range(rows):
		#print characters in each row 
		for j in range(rows):
			print(chr(65 + i), end=" ")
		print()

#rows to be spanned 
n = 7

#call the function
print_square_pattern(n)
