email = input("apna email bol beta: ")

# -------- EMAIL CHECK (unlimited) --------
for _ in range(1000):
    email = input("apna email bol beta: ")
    if email == "sujal@gmail.com":
        break
    else:
        print("email fir se likh")

# -------- PASSWORD CHECK (unlimited) --------
for _ in range(1000):
    password = input("apna password bolde: ")

    if password == "123":
        print("welcome")
        break
    else:
        print("password incorrect, fir se likh")

    print("password incorrect, fir se likh")

else:
    print("email incorrect")
