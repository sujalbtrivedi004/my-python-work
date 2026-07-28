email = input("apna email bol beta: ")
password = input("apna password bolde: ")

if email == "sujal@gmail.com":

    if password == "123":
        print("welcome")

    else:
        print("password incorrect")
        password = input("password fir se likh: ")

        if password == "1234":
            print("finally correct")
        else:
            print("still incorrect")

else:
    print("email incorrect")
