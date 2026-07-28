def sujjal(snl,L):
    
    result = 0
    for i in L:
        if snl(i):
            result = result + i
    return result


L = [11,14,21,23,56,78,45,29,28]

x=lambda x:x%2 == 0
y=lambda x:x%2!=0
z=lambda x:x%3==0

print(sujjal(x,L))
print(sujjal(y,L))
print(sujjal(z,L))