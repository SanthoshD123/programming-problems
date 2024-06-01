#define the function 
def print_heart_pattern(rows):
    #upper part of the heart
    for i in range(rows // 2, rows, 2):
        #prints spaces in the first half
        for j in range(1, rows - i, 2):
            print(" ", end="")
        #prints alphabets in the first half
        for j in range(i):
            print(chr(65 + j), end="")
        #prints spaces in the second half
        for j in range(1, rows - i + 1, 1):
            print(" ", end="")
        #print alphabets in the second half
        for j in range(i):
            print(chr(65 + j), end="")
        print()
 
    #lower part of the heart
    for i in range(rows, 0, -1):
        for j in range(i, rows):
            print(" ", end="")
        for j in range(i * 2):
            print(chr(65 + j), end="")
        print()
 
#size of the heart based on the rows in the lower part
n = 10
 
#call the function 
print_heart_pattern(n)
