# Python Program to Print Floyd's Triangle
rows = int(input("Please Enter the total Number of Rows: "))
number = 1

print("Floyd's Triangle")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end='  ')
        number += 1
    print()
