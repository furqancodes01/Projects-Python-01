
n = 5
i = 0
max = float('-inf')
min = float('inf')
print('Enter',n,"Number")
while i<n:
    i = i+1
    x = int(input())
    if x > max:
        max = x 
    if x < min:
        min = x
print('Max: ',max)
print('Min :',min)
