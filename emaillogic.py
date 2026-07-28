email = input("apna email bol beta: ")

if email != "sujaltrivedib@gmail.com":
    print("email galat hai")
    email = input("email fir se likh: ")

if email == "sujaltrivedib@gmail.com":
    password = input("apna password bolde: ")

    if password == "123":
        print("welcome")
    else:
        print("password incorrect")
else:
    print("email phir bhi galat hai")

