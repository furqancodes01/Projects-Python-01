def flatten(L):
    for ele in L:
        if hasattr(ele,'__iter__'):
            yield from flatten(ele)
        else:
            yield ele
            
L = [1,2,[3,4,[5,6,7],8],9,[10]]

flat= flatten(L)

flat_list = list(flat)
print(flat_list)