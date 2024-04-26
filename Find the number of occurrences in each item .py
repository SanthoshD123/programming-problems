l1 = ['A', 'B', 'C', 'D', 'A', 'A', 'B']

result = []

for x in l1:
    if x not in result:
        result.append(x)
        count = l1.count(x)
        result.append(count)

print(result)
