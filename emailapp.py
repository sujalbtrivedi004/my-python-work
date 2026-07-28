email = input("apna email bol beta")
password = input("apna password bolde")

if email == "sujal@gmail.com" and password =="123":
    print("welcome")
    
elif email == "sujal@gmail.com" and password != "123":
    print("password incorrect")
    password = input("password fari thi lakh")
    
    if password == "1234":
        print("finally correct")
    else:
        print("still incorrect")

if email == "sujal@gmail.com" and password != "123":
    print("password incorrect")
    password = input("password galat hai biru")
    
    if password == "1234":
        print("finally correct")

if email != "sujal@gmail.com" and password == "123":
    print("gmail incorrect")
    password = input("gmail fari thi lakh")
    
    if gmail == "sujal@gmail.com":
        print("finally correct")
    else:
        print("still incorrect")
        
if email != "sujal@gmail.com" and password == "123":
    print("gmail incorrect")
    password = input("gmail fari thi lakh")
    
    if gmail == "sujal@gmail.com":
        print("finally correct")
    else:
        print("still incorrect")


else:
    print("incorrect creditancials")