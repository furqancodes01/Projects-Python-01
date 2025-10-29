M1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
M2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]
M3 = []
for i in range(3):
    s = []
    for j in range(4):
        r = M1[i][j] + M2[i][j]
        s.append(r)
    M3.append(s)
print(M3)