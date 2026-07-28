email = input("apna email bol beta: ")
if '@' in email:

if email != "sujaltrivedib@gmail.com":
    print("email galat hai")
    email = input("email fir se likh: "
    
    if email == "sujaltrivedib@gmail.com" and password == "123":
        print("welcome")

    elif email == "sujaltrivedib@gmail.com" and password != "123":
        print("password incorrect")
        password = input("password fir se likh: ")

        if password == "123":
            print("finally correct")
        else:
            print("still incorrect")

    else:
        print("incorrect credentials")
else:
    print("email sahi se likh bete")