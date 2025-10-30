L1 = ['A','B','C','D','B','C','A','D','A']
result = []

for item in L1:
    if item not in result:
        result.append(item)
        count = L1.count(item)
        result.append(count)
print(result)