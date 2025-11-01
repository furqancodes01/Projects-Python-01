l1 = [1,2,3,4,5,3,2,1,6]
# method 1
l2 = []

for x  in l1:
    if x not in l2:
        l2.append(x)
print(l2)        
    
    
# method 2 
    
# for x in l1:
#     while l1.count(x) >1:
#         l1.remove(x)
# print(l1)