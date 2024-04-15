num = int(input("numbers: "))
psum = 0
nsum = 0
count = 0
while count <num:
    n = int(input("Enter : "))
    if n > 0:
        psum = n+psum
    else:
        nsum = n+nsum
    count = count +1
print(psum)
print(nsum)
