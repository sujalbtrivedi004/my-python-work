L1=[1,1,2,2,3,3,4,4]
L2=[1,2,3,1]
L=[]

for i in L1:
    if i not in L:
        L.append(i)
print(L)