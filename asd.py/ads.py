with open(r"E:\python\asd.py\data.txt","r") as f:
    count = 0
    for line in f:
        count += 1

print("Total lines:", count)

files = ["a.txt","b.txt","c.txt"]
for f in files:
    with open(f,"w") as file:
        file.write("hello"+f)

