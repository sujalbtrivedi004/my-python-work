word = "how"
with open(r"E:\python\asd.py\data.txt") as f:
    for line in f:
        if word in line:
            print("found:",line.strip())