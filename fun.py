def sujal(numberss):
    if numberss % 2 == 0:
        return"even"
    else:
        return"odd"

for i in range(1,11):
    print(sujal(i))

print(sujal.__doc__)
print(__doc__)